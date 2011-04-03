#!/usr/bin/env python2.6

import cgi, cgitb
cgitb.enable()

print 'Content-Type: text/xml'
print

from random import *

print '<IPList>'

for i in xrange(randint(1, 10)):
    address = '10.0.%s.%s' % (randint(1, 2), randint(10, 19))
    team = choice(('BLUE', 'RED'))
    os = choice(('Linux 2.x.x', 'FreeBSD 1.xx', 'Windows 95'))
    nodetype = "NodeServer"
    print '''
<IP Address="%s" Team="%s" OS="%s" NodeType="%s">''' % (address, team, os, nodetype)
    print '<ServiceList>'
    if randint(0, 4):
        for t in ('ftp', 'ssh', 'http', 'mysql'):
            status = choice(("UP", "DOWN"))
            print '<Service type="%s" status="%s" />' % (t, status)
    print '''</ServiceList>
</IP>'''

if not randint(0, 3):
    print '''
<IP Address="10.0.0.10" Team="WHITE" OS="Linux 2.6.X" NodeType="NodeKoTH">
  <ServiceList>
  </ServiceList>
</IP>
'''

print "</IPList>"
