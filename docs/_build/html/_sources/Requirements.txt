
Requirements
************

To implement the infrastructure needed for the Cyber Storm competition, XScore
will need to provide two main services: network service checking and a 
point based scoring system to rank the opposing teams.  This document 
describes the requirements of this system.


Network Service Checking
========================

Throughout the competition, each team will be expected to maintain a number of 
machines that provide a set of network services.  XScore will check the status 
of these services on a regular interval to determine if another team has
successfully `hacked` or disabled this service.  Support for checking the 
following services will be provided:

* HTTP - Hyper Text Transfer Protocol
* FTP - File Transfer Protocol
* MySQL - Database Server
* SSH - Secure SHell


Scoring
=======

To determine a winner of the competition, XScore will need to provide 
a system that awards each team points based on the status of the services
they are able to maintain.  XScore is to provide an automated system that
will check these services and then award the given team an appropriate number 
of points.

To establish a well-defined method concerning when points are awarded, we will
define the status of a service as one of the following states:

#. Service is up and operates as expected.
#. Service has been successfully hacked by an opposing team.
#. Service is down or does not operate as expected.

Each of these states will be recognized by XScore and will be the basis on which
points are awarded.  The value of the points can be specified for each of the services
checked and configurable as needed.

In addition to this process of checking services and awarding points, XScore is to 
provide the officials of the competition's with the ability to manually adjust 
the scores.  This is intended to provide a fallback in case if the scoring server
incorrectly awards a team points.  In addition, this will allow the officials to
handle unforeseen events during the competition.  For example, if a team attempts to 
`hack` XScore and modify the scores, officials may want to remove these points.


User Interface to XScore
========================

To allow officials to easily run the scoring server and manage the compeititoin,
XScore will provide the appropriate software.  Running the scoring server will
be handled by a command-line program and will schedule when and how often services
are checked.  To monitor the status of the competition and provide a friendly user
interface to the scoring server, a web-based application will be included.  This 
program can be used by officials to create new challenges and announce important messages.
In addition, this program will provide the officials with access to manually adjust the
scores as needed.
