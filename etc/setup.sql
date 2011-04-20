
DROP DATABASE IF EXISTS scores;
CREATE DATABASE scores;

CREATE TABLE scores.teams
       (team_name VARCHAR(100),
       color VARCHAR(100) UNIQUE,
       score BIGINT DEFAULT 0,
       challenges_won INT DEFAULT 0,
       PRIMARY KEY (team_name));

CREATE TABLE scores.events 
       (id INT NOT NULL AUTO_INCREMENT,
       team_name VARCHAR(100), 
       event_type VARCHAR(100),
       points BIGINT,
       message TEXT,
       ts TIMESTAMP,
       PRIMARY KEY (id));

CREATE TABLE scores.challenges
	(id INT,
	challenge_name VARCHAR(50),
	difficulty INT,
	state TEXT,
	hidden TEXT,
	category TEXT,
	description VARCHAR(200),
	points_possible INT,
	blue_points INT,
	red_points INT,
	PRIMARY KEY (id));       

CREATE TABLE scores.announcements
       (id INT NOT NULL AUTO_INCREMENT,
       message TEXT,
       start TIMESTAMP,
       stop_after INT,
       PRIMARY KEY (id));

INSERT INTO scores.teams SET color='Blue', team_name='Jedi';
INSERT INTO scores.teams SET color='Red', team_name='Sith';
INSERT INTO scores.teams SET color='White', team_name='The Force';
