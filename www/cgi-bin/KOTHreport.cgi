#!/usr/bin/env python2.6
import cgitb
cgitb.enable()

import datetime
from xml.sax import saxutils

from xscore.scores import query

print 'Content-Type: application/xml'
print

boxes = list(query("""SELECT description, state FROM scores.challenges WHERE state != 'x'""")) 
#states = list(query("""SELECT state FROM scores.challenges WHERE category=k AND state=x"""))


kothip = {}
kothown = {}
ip = []
i = 0
#print len(boxes), boxes
for box in boxes:
	ip = box[0].split(':',1)
	#print i,' ', box
	kothip[i] = ip[0]
	if box[1] == 'b':	
		kothown[i] = 'BLUE'
	if box[1] == 'r':
		kothown[i] = 'RED'
	#print kothip[i], " ", kothown[i], 
	i += 1
##################################################

print '<KOTHBOXES',
for j, box in enumerate(boxes):
    print kothip[j]+" "+kothown[j]+":",
print '>'
print '</KOTHBOXES>'
