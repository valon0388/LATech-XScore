#!/usr/bin/env python2.6

import cgi, cgitb
cgitb.enable()

print 'Content-Type: text/xml'
print

import time, datetime
from random import *

print '<attackList timestamp="%s">' % time.time()

for i in xrange(randint(1, 20)):
    src = '555.55.555.%s' % randint(10, 99)
    srcteam = choice(('blue', 'red'))
    destip = '555.55.555.%s' % randint(10, 99)
    destteam = 'red' if srcteam == 'blue' else 'blue'
    type = choice(('nessus', 'unknown', 'Denial of Service'))
    t = str(datetime.datetime.now())
    ttd = int(time.time() + 10)
    print '''
<attack src="%s" srcteam="%s" destIP="%s" destTeam="%s" Type="%s" Time="%s" TimetoDie="%s" />
''' % (src, srcteam, destip, destteam, type, t, ttd)
    
print '</attackList>'
