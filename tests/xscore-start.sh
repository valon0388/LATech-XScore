#!/bin/bash

# Continuous loop of mini-competitions

WAIT=5

while true; do
    echo "xscore: Starting new competition:" `date`
    xscore-reset-db.sh -u root -psecret
    for ((i = 0; i < 100; i++)); do
	echo
	for service in http ftp ssh mysql; do
	    echo "xscore[$i]: Checking $service"
	    xscore-check.py $service
	    echo "xscore[$i]: Sleeping for ${WAIT} secs"
	    sleep $WAIT
	done
	if (( $i % 7 == 0 )); then
	    xscore-new.py announcement "`fortune -s`"
	    sleep 10
	fi
    done
    echo "xscore: Finished competition:" `date`
done
