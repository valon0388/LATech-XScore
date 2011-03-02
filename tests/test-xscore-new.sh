#!/bin/bash

set -e
SCORES="curl -GET http://localhost:1337/cgi-bin/scores.cgi "

xscore-new announcement "A-$$"
$SCORES 2> /dev/null | egrep -q "A-$$"

xscore-new score 'Bruce Lee' "B-$$" -42 "C-$$"
$SCORES 2> /dev/null | egrep -q "B-$$"
$SCORES 2> /dev/null | egrep -q "C-$$"
