
Design
******

The XScore system is divided into multiple components in order to provide a modular design
that is easy to extend while also satisfying the neccessary requirements of Cyber Storm.
This document is intended to provide an overview of how XScore is designed and implemented.


Overview
========

XScore consists of two main components: the scoring server and a visual front-end.
The scoring server is responsible for scheduling when services are checked and the
registering of the appropriate scoring events.  In addition, the scoring server handles
passing data to the scoring client via an HTTP server.

The visual front-end is a web-based application that provides an
adminstrative interface to the scoring server.  It provides the
ability to monitor the progress of the competition as well manage
various competition related events.


User Interfaces
===============

Scoring Server
--------------
The scoring server is the command-line program ``xscored`` which is used to initialize
and run the server.

Front-end
---------


Programming Environment
=======================
XScore utilizes a number of different software systems to implement the scoring server.
Although primarily written in Python, it also makes use of Bash shell scripts and the front-end
makes extensive use of Javascript.  Since this system is intended to be used on Linux based servers,
little concern was given to portability on non Posix systems.  This allowed us to simplify the 
implementation of the scoring server and prevented us from having to test on other platforms.
It does however imply that additional development would be required if this feature were wanted in
the future.

Other systems used and required by XScore include a MySQL database server and a HTTP server used
to communicate with the scoring client and host the front-end.  Refer to the README file included
with the distrubution for the specific versions of the programs used by XScore.


Scoring Server
==============

The scoring server is divided into four main components: 

#. Network Service Checkers.
#. Scheduling of Service Checks.
#. Scores and Events Handeling.
#. Communication with the client.

These components are discussed in the following sections.


Network Service Checkers
------------------------
The network service checkers are used to determine the status of a team's network service.

FTP
~~~

HTTP
~~~~

SSH
~~~

MySQL
~~~~~

Scheduling of Service Checks
----------------------------

Scores and Events Handeling
---------------------------
Record and manage the scores for each team and the events that occur during the competition.


Communication with the Client
-----------------------------
