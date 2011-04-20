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
#  %(status)   Status of the service (UP | DOWN | PWNED)
#  %(hacker)   If `status' is PWNED this contains the hacker's name.
#  %(reason)   If `status' is DOWN this describes why.
#


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
    'FTP-HACKED':    -10,
    
    'SSH-UP':        20,
    'SSH-DOWN':      0,
    'SSH-HACKED':    -10,
    
    'MYSQL-UP':      25,
    'MYSQL-DOWN':    0,
    'MYSQL-HACKED':  -10,

    'KOTH-UP': 25,
    }


database = {
    'connect': {
        'user': 'xscore', 
        'passwd': 'xscorepass',
        'db': 'scores'
        },
    }

koth_nodes = (
    ('10.0.0.11',  21),
    ('10.0.0.12',  21),
    ('10.0.0.13',  21),
    ('10.0.0.14',  21),
)

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

        'black-box': '10.0.1.15',
        
        'HTTP': (('10.0.1.10', 80),
                 ('10.0.1.11', 80),
                 ('10.0.1.12', 80),
            	  ('10.0.1.13', 80),
            	  ('10.0.1.14', 80)
			),
            
        'SSH': (
             ('10.0.1.10', 22, 'scoringserver', 'Gourdis!7A69'),
             ('10.0.1.11', 22, 'score', 'Gourdis!7A69'),
             ('10.0.1.12', 22, 'score', 'Gourdis!7A69'),
		   ('10.0.1.13', 22, 'score', 'Gourdis!7A69'),
             ('10.0.1.14', 22, 'score', 'Gourdis!7A69')
            ),

        'FTP': (
            ('10.0.1.10', 21, 'score', 'Gourdis!7A69'),
            ('10.0.1.11', 21, 'score', 'Gourdis!7A69'),
            ('10.0.1.12', 21, 'score', 'Gourdis!7A69'),
            ('10.0.1.13', 21, 'score', 'Gourdis!7A69'),
            ('10.0.1.14', 21, 'score', 'Gourdis!7A69')
            ),
#                ('10.0.0.11', 21, 'anonymous', ''),
#                ('10.0.0.13', 21, 'anonymous', ''),
#                ('10.0.0.21', 21, 'anonymous', 'user@host.com')),

        'MYSQL': (
		  ('10.0.1.10', 3306, 'score', 'Gourdis!7A69'),
            ('10.0.1.11', 3306, 'scoringserver', 'Gourdis!7A69'),
            ('10.0.1.12', 3306, 'score', 'Gourdis!7A69'),
            ('10.0.1.13', 3306, 'score', 'Gourdis!7A69'),
            ('10.0.1.14', 3306, 'score', 'Gourdis!7A69')
		 ),
        },
            
    ###################### Blue Team #######################
    {
        'color': 'Blue',
        'name': 'Jedi',

        'subnet': '10.0.2.0/24',
        'netmask': '255.255.255.0',
        'gateway': '10.0.2.1',

        'black-box': '10.0.2.15',

        'HTTP': (
            ('10.0.2.10', 80),
            ('10.0.2.11', 80),
            ('10.0.2.12', 80),
            ('10.0.2.13', 80),
            ('10.0.2.14', 80)
            ),
            
        'SSH': (
            ('10.0.2.10', 22, 'White', 'H3r3U&0'),
            ('10.0.2.11', 22, 'white', 'H@ya0^^1az@k!'),
            ('10.0.2.12', 22, 'white', 'Q4re97BdsT'),
            ('10.0.2.13', 22, 'white', 'Q4re97BdsT'),
            ('10.0.2.14', 22, 'white', 'Q4re97BdsT')
            ),

        'FTP': (
            ('10.0.2.10', 21, 'White', 'H3r3U&0'),
            ('10.0.2.11', 21, 'white', 'H@ya0^^1az@k!'),
            ('10.0.2.12', 21, 'white', 'Q4re97BdsT'),
            ('10.0.2.13', 21, 'white', 'Q4re97BdsT'),
            ('10.0.2.14', 21, 'white', 'Q4re97BdsT')
#                ('10.0.0.12', 21, 'anonymous', ''),
#                ('10.0.0.14', 21, 'anonymous', ''),
#                ('10.0.0.22', 21, 'anonymous', 'user@host.com')),
            ),


        'MYSQL': (
		  ('10.0.2.10', 3306, 'White', 'H3r3U&0'),
        	  ('10.0.2.11', 3306, 'White', 'H@ya0^^1az@k!'),
            ('10.0.2.12', 3306, 'White', 'Q4re97BdsT'),
            ('10.0.2.13', 3306, 'White', 'Q4re97BdsT'),
            ('10.0.2.14', 3306, 'White', 'Q4re97BdsT')
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
