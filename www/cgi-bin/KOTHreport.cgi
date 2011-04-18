#!/usr/bin/env python2.6
import cgitb
cgitb.enable()

import datetime
from xml.sax import saxutils

from xscore.scores import query

print 'Content-Type: text/html\n'
print

boxes = list(query("""SELECT description, state FROM scores.challenges WHERE category = 'k'""")) 
#states = list(query("""SELECT state FROM scores.challenges WHERE category=k AND state=x"""))


kothip = {}
kothown = {}
ip = []
for i, box in enumerate(boxes):
	ip = box[0].split(':', 1)
	kothip[i] = ip[0]
	if box[1] == 'b':	
		kothown[i] = 'BLUE'
	elif box[1] == 'r':
		kothown[i] = 'RED'
	else :
		kothown[i] = 'UNOWNED'
##################################################
i
#print '<KOTHBOXES',
for j, box in enumerate(boxes):
    print kothip[j]
    print " "
    print kothown[j]
    print ":",
#print '>'
#print '</KOTHBOXES>'
