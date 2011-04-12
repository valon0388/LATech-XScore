#!/usr/bin/env python2.6

import cgi, cgitb, sys
cgitb.enable()

print 'Content-Type: text/html'
print

from xscore import scores


form = cgi.FieldStorage()
try:
    action = form['type'].value
    if action == 'scoringevent':    
        team = form['teamName'].value
        etype = form['eventType'].value
        points = int(form['points'].value)
        message = form['message'].value
        scores.add_event(team, etype, points, message)
        print 'Score Added!'
        
    elif action == 'announcement':
        message = form['message'].value
        scores.add_announcement(message, 10)
        print 'Announcement Made!'
        
    elif action == 'newchallenge':
        ch_name = form['challengeName'].value
        points = int(form['points'].value)
        message = form['message'].value
        state = 'i'
        scores.new_challenge(ch_name, points, message, state)
        print 'Challenge Started!'
        
    elif action == 'updatechallenge':
        _id = form['id'].value
        winner = form['winner'].value
        scores.update_challenge(_id, winner) ######
        print 'Challenge Updated!'
    else:
        raise Exception("Unknown request!")
    sys.exit()
except KeyError as e:
    print '''
<p><blink>Error</blink>  No entry for %s.</p>
''' % cgi.escape(str(e).strip())
    
except Exception as e:
    print '''
<p><blink>Error</blink>  <nobr>%s.</nobr></p>
''' % cgi.escape(str(e).strip())
