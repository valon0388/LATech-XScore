#!/usr/bin/env python


# import pxssh
# class SSH:

#     def get(self):
#         s = pxssh.pxssh()
#         s.force_password = True
#         s.login(self.ip, self.usr, self.passwd, self.port, login_timeout=self.timeout)
        
#         for i in xrange(10):
#             s.sendline()
#         return s.before

import pexpect


class Foo:
    pass

s = Foo()
s.ip = '10.0.2.10'
s.port = 22
s.usr = 'White'
s.passwd = 'H3r3U&0'
s.timeout = 100

x = pexpect.spawn("ssh -p %s %s@%s" % (s.port, s.usr, s.ip))
x.expect("[pP]assword: ")
x.sendline(s.passwd)
for i in xrange(10):
    x.sendline()
x.send("#XSCORE")
x.expect("#XSCORE")

print x.before


# import logging 

# class NullHandler(logging.Handler):
#     def emit(self, record):
#         pass
# h = NullHandler()
# logging.getLogger('paramiko').addHandler(h)

# import paramiko

# ssh = paramiko.SSHClient()
# ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# ssh.connect(ip, port=port, username=usr, password=passwd, timeout=100)
# print "Connected"
# channel = ssh.invoke_shell()
# channel.setblocking(1)

# fn = channel.makefile()

# channel.sendall('exit #SENTINEL\r\n')

# motd = fn.read()

# fn.close(); channel.close()    

# # Return everything before the prompt
# regexp = '^.*?exit #SENTINEL\r\n'
# m = re.search(regexp, motd, re.M)
# # if not m: 
# #     return motd
# # print motd[:m.start()]
# print motd
# ssh.close()
