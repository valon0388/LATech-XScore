#!/usr/bin/env python2.6

import cgi, cgitb
cgitb.enable()

print 'Content-Type: text/xml'
print

import time, datetime
from random import *

print '<Statistics>'

for i in xrange(randint(1, 20)):
    x = ['100', '200', '300', '400', '500'] * 10
    shuffle(x)
    print '''
<stat BluetoRed="%s" RedtoBlue="%s" White="%s" RedtoWhite="%s" BluetoWhite="%s"/>
''' % tuple(x[:5])

print '</Statistics>'
