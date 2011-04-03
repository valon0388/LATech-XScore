#!/usr/bin/env python

import pexecpt, sys

ip = '10.0.2.10'
port = 22
usr = 'White'
passwd = 'H3r3U&0'

def check():
    sh = pexecpt.spawn("ssh -p %s %s@%s" % (port, usr, ip))
    sh.
