'''
Module that handles checking the current status of SQL, FTP,
SSH, and HTTP services for each team.
'''

import os, sys, re
import urllib2, ftplib
import StringIO
import signal
import random

import MySQLdb
import pexpect


import logging
class NullHandler(logging.Handler):
    def emit(self, record):
        pass
logging.getLogger('paramiko').addHandler(NullHandler())
import paramiko


import config, scores
from logger import logger

DEBUG = 1


class TimeOutException(Exception):
    '''
    Triggered when a service takes too long to respond.
    '''
    pass


def timeout(seconds, func, *args, **kwargs):
    '''
    Executes the function 'func' with the given arguments.  If it
    does not return within the time specified by 'seconds', a
    TimeOutException is raised.
    '''
    # Define a callback to raise the exception
    def _raise(*ignored):
        raise TimeOutException()
    signal.signal(signal.SIGALRM, _raise)
    signal.alarm(seconds)
    try:
        return func(*args, **kwargs)
    finally:
        # Turn the alarm off
        signal.alarm(0)


class Service(object):
    '''
    Service class extended by all Network Services, contains facilities
    to check status of itself and format a response message.
    '''
    timeout = 5

    def __init__(self, team, ip, port, usr=None, passwd=None, timeout=30, koth=False):
        '''
        Create a new Service instance.
        
        -team    Name of the controlling team
        -ip      IP address
        -usr     Optional user name to use
        -passwd  Optional password for `usr'
        '''
        self.team = team
        self.ip = ip
        self.port = port
        self.usr = usr
        self.passwd = passwd
        self.timeout = timeout
        self.koth = koth


    def check(self):
        '''
        Check the status of this service.

        Returns the status and a descriptive message.
        '''
        self.status = 'DOWN'
        try:
            self.status = timeout(self.timeout, self.stat)
        except TimeOutException:
            self.reason = 'Timed out'
        except Exception as e:
            self.reason = e
        self.message = self.format()
        return self.status, self.message


    def stat(self):
        '''
        HTTP Service class
        
        Get the status of this service. 
        
        Returns 'UP', 'DOWN', or 'PWNED'
        '''
        owner = self.team
        hackrs = [t['name'] for t in config.teams]
        hackrs.remove(owner)
        regexp = lambda s: re.sub(r'\W|_', r'.?', s)
        motd = self.get()
        if re.search(regexp(owner), motd, re.I):
            return 'UP'
        for i, hackr in enumerate(hackrs):
            m = re.search(regexp(hackr), motd, re.I)
            if m:
                self.hacker =  hackrs[i]
                return 'PWNED'
        self.reason = 'Team name not found in motd'
        return 'DOWN'


    def format(self, fmt=None):
        '''
        Construct a fancy message describing this service.
        
        `fmt' can contain the following %-style mapping keys which are 
        replaced with the appropriate values.
        
          %(team)     Team name
          %(ip)       IP address
          %(port)     Port
          %(service)  The service checked
          %(status)   Status of the service (UP | DOWN | PWNED)
          %(hacker)   If `status' is PWNED this contains the hacker's name.
          %(reason)   If `status' is DOWN this describes why.
        '''
        keys = {'service': self.__class__.__name__, 'hacker': '', 
                'status': '?', 'reason': ''}
        keys.update(self.__dict__)
        if self.koth:
            keys['service'] = 'KOTH'
        if not fmt:
            fmt = config.messages[self.status]
        return fmt % keys


    def __str__(self):
        return self.format(
            '%(service)-6s %(team)-13s %(ip)-14s %(port)-4s %(status)s '
            'hacker:%(hacker)s reason:%(reason)s')


class HTTP(Service):
    '''
    HTTP Service class
    '''    
    def get(self):
        '''Connects to http URL and returns server response.'''
        url = "http://%s:%s/" % (self.ip, self.port)
        return urllib2.urlopen(url).read()


class SSH(Service):
    '''
    SSH Service class
    '''   
    def get(self):
        '''Attempt a SSH connection to ip and return MOTD from server.'''
        ssh = paramiko.SSHClient()
        try:           
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            try:
                ssh.connect(self.ip, port=self.port, username=self.usr, password=self.passwd)
            except Exception, e:
                print e
                return self.get2()
            channel = ssh.invoke_shell()
            channel.setblocking(1)
            fn = channel.makefile()
            channel.sendall('exit #SENTINEL\r\n')
            motd = fn.read()
            fn.close(); channel.close()    
            # Return everything before the prompt
            regexp = '^.*?exit #SENTINEL\r\n'
            m = re.search(regexp, motd, re.M)
            if not m: return motd
            return motd[:m.start()]
        finally:
            ssh.close()

    def get2(self):
        # Work around to ignore timeout that's already going
        def get3():
            x = pexpect.spawn("ssh -p %s %s@%s" % (self.port, self.usr, self.ip))
            try:
                x.expect("[pP]assword: ")
                x.sendline(self.passwd)
                x.expect("[$#] ")
                return x.before
            finally:
                x.close()
        return timeout(self.timeout, get3)
    

class FTP(Service):
    '''
    FTP Service class
    '''   
    def get(self):
        '''Attempt a connection to FTP server and return welcome message from server.'''
        ftp = ftplib.FTP()
        try:
            ftp.connect(self.ip, self.port)
            ftp.login(self.usr, self.passwd)
            return ftp.getwelcome()
        finally:
            ftp.close()


class MYSQL(Service):
    '''
    MYSQL Service class
    '''   
    def get(self):
        '''Attempt a connection to MYSQL server and return list of all databases.'''
        con = MySQLdb.connect(host=self.ip, user=self.usr, 
                              passwd=self.passwd, port=self.port, connect_timeout=self.timeout)
        cur = con.cursor()
        cur.execute('SHOW DATABASES')
        rows = cur.fetchall()
        con.close()
        return '\n'.join(r[0] for r in rows)


def check(team, service, ip, port, usr='', passwd='', timeout=30):
    '''Checks the status of a service and appropriates points accordingly.'''
    if os.fork() != 0:
        return
    koth = service == 'KOTH'
    if koth:
        klass = FTP
    else:
        klass = eval(service.upper())
    checker = klass(team, ip, port, usr, passwd, timeout, koth)

    logger.info('Checking...  %s' % checker)
    stat, msg = checker.check()
    logger.info('Checked      %s' % checker)
    
    if not koth or stat == 'UP':
        event_type = "%s-%s" % (service.upper(), stat)
        points = config.points[event_type]
        scores.add_event(team, event_type, points, msg)
    sys.exit()
