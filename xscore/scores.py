'''
Database Facilities to handle creation and management of events, 
announcements, and challeneges.
'''

import MySQLdb
from config import database, teams
import datetime

from logger import logger

def query(sql, sql_args=None):
    '''
    Executes query and returns resultset.
    '''
    db = MySQLdb.connect(**database['connect'])
    c = db.cursor() # returns a list of rows as a tuple
    try:
        c.execute(sql, sql_args) # Executes query on the set
        return c.fetchall() # returns all available rows from the cursor
    finally:
        c.close()
        db.close()
        
'''def getScores():
    red = query("""select score from scores.teams where color = "red""")
    blue = query("""select score from scores.teams where color = "blue""")
    scores = red[0] + "," + blue[0]
    return scores        
'''


def add_announcement(msg, secs_to_display=10):
    '''
    Add a new announcement to the database.
    '''
    query("""insert into scores.announcements set message = %s,
                                                  stop_after = %s""", 
          (msg, secs_to_display))
    logger.info("New-Announcement [msg: %s] [display-for: %s]"
                % (msg, secs_to_display))


def add_event(team, etype, pts, msg):
    '''
    Submits new event to database.
    '''
    assert any(t['name'] == team for t in teams), "Unknown team `%s'" % team
    pts = int(pts)
    # Add new event
    query('''insert into scores.events set team_name = %s,
                                           event_type = %s,
                                           points = %s,
                                           message = %s''', 
          (team, etype, pts, msg))
    # Update team's score
    query('''update scores.teams set score = score + %s
                                     where team_name = %s''', 
          (pts, team))    
    logger.info("%-13s %-13s %s\t%s" \
                    % (etype, team, pts, msg))


<<<<<<< HEAD
def new_challenge(id, challenge_name, difficulty, state, hidden, category, description ):
	'''
	Create a new challenge.
    	''' # We should calculate scores now instead of having the points sent to us.
	if id == 0:
		ids = {} 
		ids = query('''SELECT id FROM scores.challenges''')
		id = ids.pop() + 1

    	query('''INSERT INTO scores.challenges SET id = %d, challenge_name = %s, difficulty = %d, state = %s, hidden = %s, category = %s,description = %s,''', 
          (id, challenge_name, difficulty, state, hidden, category, description))
    	add_announcement(description)
	fullHidden = NULL
	if hidden == 'h':
		fullHidden = 'Hidden from all.'
	elif hidden == 't':
		fullHidden = 'Hidden from teams.'
	elif hidden == 'v':
		fullHidden = 'Visible to all.'

	fullCategory = NULL
	if category == 'p':
		fullCategory = 'Penetration'
	elif category == 'k':
		fullCategory = 'King of the Hill'
	elif category == 's':
		fullCategory = 'Scavenger Hunt'
	elif category == 'r':
		fullCategory = 'Riddle'
		
    	logger.info("New-Challenge [Name: %s] [Difficulty: %d] [Hidden: %s] [Category: %s] [Description: %s]"
                	% (challenge_name, difficulty, fullHidden, fullCategory, description))
=======
def new_challenge(challenge_name, pts, msg, winner):
    '''
    Create a new challenge.
    ''' 
    query('''insert into scores.challenges set challenge_name = %s,
                                               points = %s,
                                               message = %s,
                                               winner = %s''', 
          (challenge_name, pts, msg, winner))
    add_announcement(msg)
    logger.info("New-Challenge [name: %s] [pts: %s] [msg: %s]"
                % (challenge_name, pts, msg))
>>>>>>> blackdragon0688-master


def update_challenge(id, winner, points):
    '''
    Declare a winner for an existing challenge.
    '''
    rows = query('''select * from scores.challenges where id = %s''',
                 (id,))
    assert rows, 'No open challenges'
    id, challenge_name, difficulty, state, hidden, category, description, blue_points, red_points = rows[0]
    assert state is not 'x', 'Challenge already closed'
    add_event(winner, challenge_name, points, 'Challenge Won!')
    add_announcement('%s wins %s challenge!' % (winner, challenge_name))
    query('''update scores.challenges set %s_points = %d
                                       where id = %s''', 
          (winner, points, id))
    query('''update scores.teams set challenges_won = challenges_won + 1
                                  where team_name = %s''',
          (winner,))
    logger.info("Challenge-Updated: [id: %s] [name: %s] [winner: %s]"
                % (id, challenge_name, winner))
