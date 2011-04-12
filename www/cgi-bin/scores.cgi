#!/usr/bin/env python2.6

import cgitb
cgitb.enable()

import datetime
from xml.sax import saxutils

from xscore.scores import query

quoteattr = lambda s: saxutils.quoteattr(str(s))


print 'Content-Type: application/xml'
print

teams = list(query("""select team_name, color, score, challenges_won 
                                             from scores.teams"""))

# Why does order matter?
teams[0], teams[1] = teams[1], teams[0]


# Get the Events
events = []
for team in teams:
    evnts = query("""select * from scores.events
                                               where team_name= %s
                                               order by id desc
                                               limit 5""", 
                        (team[0],))
    evnts = [list(l) for l in evnts]
    for lst in evnts:
        lst[1] = team[1]
        events.append(tuple(lst))

# Sort events on id
events.sort(key=lambda e: e[0], reverse=True)
# Get Announcements, check display time
announcement = query("""select * from scores.announcements
                                           order by id desc
                                           limit 1""")
announcement = announcement or ''
if announcement:
    id, msg, start, stop_after = announcement[0]
    now = datetime.datetime.now()
    diff = now - start
    if diff.seconds > stop_after:
        announcement = ''
    else:
        announcement = msg

##################################################

print '<scores',
for team in teams:
    print '%s="%s" %s_challenges_won="%s"' % (team[1], team[2], team[1], team[3]),
print '>'

for event in events:
#    id, t, type, pts, msg, ts = map(quoteattr, event)
    print '''\
\t<event id=%s team=%s type=%s points=%s message=%s time=%s />
''' % tuple(map(quoteattr, event))

print '\t<announcement msg=%s />' % quoteattr(announcement)
print '</scores>'
