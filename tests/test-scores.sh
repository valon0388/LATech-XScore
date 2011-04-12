#!/bin/bash

MYSQL="mysql --skip-column-names -u xscore -pxscorepass scores "

for team in "Bruce Lee" "Chuck Norris"; do
    points=`$MYSQL -e "select points from events where team_name = '$team';"`
done
