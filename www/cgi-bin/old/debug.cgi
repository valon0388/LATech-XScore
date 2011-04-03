#!/usr/bin/env python2.6

import cgi, cgitb, sys
cgitb.enable()

print 'Content-Type: text/html'
print

from xscore import scores

print '<table border="3" style="padding: 10px;"><tr>'

for team in ('Red', 'Blue'):
    print '<td>'
    t = scores.query('''select team_name, color, score from scores.teams where color = %s ''',
                              (team,))
    print '<h3>%s (%s): %s</h3>' % (t[0][0], t[0][1], t[0][2])
    rows = scores.query('''select * from scores.events where team_name = %s order by id desc limit 20''', (t[0][0],))
    
    colheaders = ('ID', 'Team', 'Type', 'Points', 'Message')
    rows = [[cgi.escape(str(r)) for r in row][:-1] for row in rows]

    print '''
<table border="1" style="font-size: 0.8em">
        <thead>
                <tr>
                        <th>''' + '</th><th>'.join(colheaders) + '''</th>
                </tr>
        </thead>
        <tbody>'''
    for row in rows:
        print '''\
                <tr>
                        <td>''' + '</td><td>'.join(row) + '''</td>
                </tr>'''
    print '''
        </tbody>
</table>
'''
    print '</td>'

print '</tr></table>'
