'''
Configuration data for the competition.
'''

#
# Messages can contain the following Python %-style mapping keys which are 
# replaced with the appropriate values.
#
#  %(service)  The service checked
#  %(team)     Team name
#  %(ip)       IP address
#  %(port)     Port
#  %(status)   Status of the service (UP | DOWN | HACKED)
#  %(hacker)   If `status' is PWNED this contains the hacker's name.
#  %(reason)   If `status' is DOWN this describes why.
#

REDwinUSER=''
REDubuUSER=''
REDcenUSER=''
REDbsdUSER=''
REDbbxUSER=''

REDwinPASS=''
REDubuPASS=''		
REDcenPASS=''
REDbsdPASS=''
REDbbxPASS=''














BLUEwinUSER=''
BLUEubuUSER=''
BLUEcenUSER=''
BLUEbsdUSER=''
BLUEbbxUSER=''

BLUEwinPASS=''
BLUEubuPASS=''
BLUEcenPASS=''
BLUEbsdPASS=''
BLUEbbxPASS=''

messages = {
    # Status: Message
    'UP': '%(ip)s is %(status)s',
    'DOWN':  '%(ip)s is %(status)s!',
    'HACKED': '%(ip)s hacked by %(hacker)s!',
}


points = {
    'HTTP-UP':       15, 
    'HTTP-DOWN':     0,
    'HTTP-HACKED':   -15,
    
    'FTP-UP':        20,
    'FTP-DOWN':      0,
    'FTP-HACKED':    -20,
    
    'SSH-UP':        20,
    'SSH-DOWN':      0,
    'SSH-HACKED':    -20,
    
    'MYSQL-UP':      25,
    'MYSQL-DOWN':    0,
    'MYSQL-HACKED':  -25,

    'BBX-HTTP-UP': 15,
    'BBX-HTTP-DOWN': -15,
    'BBX-HTTP-HACKED':  -20,

    'BBX-FTP-UP':       20,
    'BBX-FTP-DOWN':    -20,
    'BBX-FTP-HACKED':  -25,

    'BBX-SSH-UP': 20,
    'BBX-SSH-DOWN': -20,
    'BBX-SSH-HACKED':  -25,

    'BBX-MYSQL-UP': 25,
    'BBX-MYSQL-DOWN': -25,
    'BBX-MYSQL-HACKED':  -30,
    }


database = {
    'connect': {
        'user': 'xscore', 
        'passwd': 'xscorepass',
        'db': 'scores'
        },
    }

services = (	
			{
				'name': 'HTTP',
				'port': 80	
			},

			{
				'name': 'SSH',
				'port': 22	
			},

			{
				'name': 'FTP',
				'port': 21	
			},

			{
				'name': 'MySQL',
				'port': 3306	
			},
		 )


#########################
## Teams Configuration ##
#########################

teams = (
    ####################### Red Team #######################
    {
        'color': 'Red',
        'name': 'Sith',

        'subnet': '10.0.1.0/24',
        'netmask': '255.255.255.0',
        'gateway': '10.0.1.1',

#        'black-box': '10.0.1.15',
        
        'HTTP':(
				('10.0.1.10', 80),
                 	('10.0.1.11', 80),
                 	('10.0.1.12', 80),
            	  	('10.0.1.13', 80)
			),
            
        'SSH': (
             		('10.0.1.10', 22, REDwinUSER, REDwinPASS),
             		('10.0.1.11', 22, REDubuUSER, REDubuPASS),
             		('10.0.1.12', 22, REDcenUSER, REDcenPASS),
		   		('10.0.1.13', 22, REDbsdUSER, REDbsdPASS)
            	),

        'FTP': (
            		('10.0.1.10', 21, REDwinUSER, REDwinPASS),
            		('10.0.1.11', 21, REDubuUSER, REDubuPASS),
            		('10.0.1.12', 21, REDcenUSER, REDcenPASS),
            		('10.0.1.13', 21, REDbsdUSER, REDbsdPASS)
            	),

        'MYSQL':(
		  		('10.0.1.10', 3306, REDwinUSER, REDwinPASS),
            		('10.0.1.11', 3306, REDubuUSER, REDubuPASS),
            		('10.0.1.12', 3306, REDcenUSER, REDcenPASS),
            		('10.0.1.13', 3306, REDbsdUSER, REDbsdPASS)
		 	),

	   'BBX': (
					('10.0.1.14', 80, REDbbxUSER, REDbbxPASS),
					('10.0.1.14', 22, REDbbxUSER, REDbbxPASS),
					('10.0.1.14', 21, REDbbxUSER, REDbbxPASS),
					('10.0.1.14', 3306, REDbbxUSER, REDbbxPASS)
			),
        },
            
    ###################### Blue Team #######################
    {
        'color': 'Blue',
        'name': 'Jedi',

        'subnet': '10.0.2.0/24',
        'netmask': '255.255.255.0',
        'gateway': '10.0.2.1',

#        'black-box': '10.0.2.15',

        'HTTP':(
            		('10.0.2.10', 80),
            		('10.0.2.11', 80),
            		('10.0.2.12', 80),
            		('10.0.2.13', 80)
            	),
            
        'SSH':	(
            		('10.0.2.10', 22, BLUEwinUSER, BLUEwinPASS),
            		('10.0.2.11', 22, BLUEubuUSER, BLUEubuPASS),
            		('10.0.2.12', 22, BLUEcenUSER, BLUEcenPASS),
            		('10.0.2.13', 22, BLUEbsdUSER, BLUEbsdPASS)
            	),

        'FTP':	(
            		('10.0.2.10', 21, BLUEwinUSER, BLUEwinPASS),
            		('10.0.2.11', 21, BLUEubuUSER, BLUEubuPASS),
            		('10.0.2.12', 21, BLUEcenUSER, BLUEcenPASS),
            		('10.0.2.13', 21, BLUEbsdUSER, BLUEbsdPASS)
            	),


        'MYSQL': (
		  			('10.0.2.10', 3306, BLUEwinUSER, BLUEwinPASS),
        	  			('10.0.2.11', 3306, BLUEubuUSER, BLUEubuPASS),
            			('10.0.2.12', 3306, BLUEcenUSER, BLUEcenPASS),
            			('10.0.2.13', 3306, BLUEbsdUSER, BLUEbsdPASS)
			  ),

	   'BBX': (
					('10.0.2.14', 80, BLUEbbxUSER, BLUEbbxPASS),
					('10.0.2.14', 22, BLUEbbxUSER, BLUEbbxPASS),
					('10.0.2.14', 21, BLUEbbxUSER, BLUEbbxPASS),
					('10.0.2.14', 3306, BLUEbbxUSER, BLUEbbxPASS)
			),
        },
    ) 


## Team configuration example / test
# 
# teams = (
#     ####################### Red Team #######################
#     {
#         'color': 'Red',
#         'name': 'Chuck Norris',
# 
#         'subnet': '?',
#         'netmask': '?',
#         'gateway': '?',
# 
#         'black-box': '?',
#         
#         'HTTP': (('138.47.102.34', 1337),
#                  ('138.47.102.34', 1337),
#                  ('138.47.102.34', 1337)),
#             
#         'SSH': (('138.47.102.34', 1338, 'red', 'red'),
#                 ('138.47.102.34', 1338, 'red', 'red'),
#                 ('138.47.102.34', 1338, 'red', 'red')),
# 
#         'FTP': (('138.47.102.34', 1339, 'red', 'red'),
#                 ('138.47.102.34', 1339, 'red', 'red'),
#                 ('138.47.102.34', 1339, 'red', 'red')),
#  
#         'MYSQL': (('localhost', 3306, 'root', 'secret'),
#                   ('localhost', 3306, 'root', 'secret'),
#                   ('localhost', 3306, 'root', 'secret')),
#         },
#     
#         
#     ###################### Blue Team #######################
#     {
#         'color': 'Blue',
#         'name': 'Bruce Lee',
# 
#         'subnet': '?',
#         'netmask': '?',
#         'gateway': '?',
# 
#         'black-box': '?',
# 
#         'HTTP': (('138.47.102.34', 1337),
#                  ('138.47.102.34', 1337),
#                  ('138.47.102.34', 1337)),
#             
#         'SSH': (('138.47.102.34', 1338, 'blue', 'blue'),
#                 ('138.47.102.34', 1338, 'blue', 'blue'),
#                 ('138.47.102.34', 1338, 'blue', 'blue')),
# 
#         'FTP': (('138.47.102.34', 1339, 'blue', 'blue'),
#                 ('138.47.102.34', 1339, 'blue', 'blue'),
#                 ('138.47.102.34', 1339, 'blue', 'blue')),
#  
#         'MYSQL': (('localhost', 3306, 'root', 'secret'),
#                   ('localhost', 3306, 'root', 'secret'),
#                   ('localhost', 3306, 'root', 'secret')),
#         },
#     )
