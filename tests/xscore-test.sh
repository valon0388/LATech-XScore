#!/bin/bash

# Continuous loop of mini-competitions
WAIT=5

while true; do
    xscore-reset-db.sh -u root -psecret
    for ((i = 1; i < 10000; i++)); do
        echo $i
	red_pts=$(( 1 + `mysql --skip-column-names -B -u root -psecret scores -e "select score from teams where team_name = 'Red'"` ))
        xscore-new.py score Red test 1 "`date +%T`:    Points: $red_pts"
	blue_pts=$(( 1 + `mysql --skip-column-names -B -u root -psecret scores -e "select score from teams where team_name = 'Blue'"` ))
        xscore-new.py score Blue test 1 "`date +%T`:    Points: $blue_pts"
        sleep $WAIT
    done
    # for ((j = 49; j > -1; j--)); do
    #     echo $i
    #     xscore-new.py score Red test -1 "`date +%T`:    Points: $j"
    #     xscore-new.py score Blue test -1 "`date +%T`:    Points: $j"
    #     sleep $WAIT
    # done
done