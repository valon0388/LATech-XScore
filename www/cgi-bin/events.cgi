#!/usr/bin/env python2.6

import cgi, cgitb, sys
cgitb.enable()

print 'Content-Type: text/html'
print

from xscore import scores

tables = {
    'teams': ('Team', 'Color', 'Score', 'Challenges Won'),
    'events':  ('ID', 'Team', 'Type', 'Points', 'Message', 'Time'),
    'challenges': ('ID', 'Name', 'Winner', 'Points', 'Message', 'Start Time'),
    'announcements': ('ID', 'Message', 'Time', 'Display Time'),
    }

for arg in sys.argv[1:]:
    if arg not in tables:
        print '<h1><blink>Error: Bad request!</blink></h1>'
        sys.exit(1)

    colheaders = tables[arg]
    if arg == 'events':
        rows = scores.query('select * from scores.' + arg + ' order by id desc limit 1000')
    elif arg == 'challenges':
	rows = scores.query('select * from scores.' + arg + ' where state = "i"')
    else:
        rows = scores.query('select * from scores.' + arg)

    colheaders = [cgi.escape(h) for h in colheaders]
    rows = [[cgi.escape(str(r)) for r in row] for row in rows]
    
    print '''
<table class="ui-widget">
    <thead class="ui-widget-header">
        <tr>
            <th>''' + '</th><th>'.join(colheaders) + '''</th>
        </tr>
    </thead>
    <tbody class="ui-widget-content">'''
    for row in rows:
        print '''\
         <tr>
             <td>''' + '</td><td>'.join(row) + '''</td>
         </tr>'''
    print '''
    </tbody>
</table>
'''
