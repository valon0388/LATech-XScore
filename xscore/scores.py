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


def new_challenge(challenge_name, pts, msg):
    '''
    Create a new challenge.
    '''
    query('''insert into scores.challenges set challenge_name = %s,
                                               points = %s,
                                               message = %s''', 
          (challenge_name, pts, msg))
    add_announcement(msg)
    logger.info("New-Challenge [name: %s] [pts: %s] [msg: %s]"
                % (challenge_name, pts, msg))


def end_challenge(id, winner):
    '''
    Declare a winner for an existing challenge.
    '''
    rows = query('''select * from scores.challenges where id = %s''',
                 (id,))
    assert rows, 'No open challenges'
    id, c_name, winr, pts, msg, ts = rows[0]
    assert winr is None, 'Challenge already closed'
    add_event(winner, c_name, pts, 'Challenge Won!')
    add_announcement('%s wins %s challenge!' % (winner, c_name))
    query('''update scores.challenges set winner = %s
                                       where id = %s''', 
          (winner, id))
    query('''update scores.teams set challenges_won = challenges_won + 1
                                  where team_name = %s''',
          (winner,))
    logger.info("Challenge-Ended: [id: %s] [name: %s] [winner: %s]"
                % (id, c_name, winner))
