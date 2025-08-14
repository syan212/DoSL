from lark import Lark

grammar = r"""
start: command*

command: def_attack
       | threads
       | requests
       | attack_seq
       | start_attack
       | stop_attack
       | sleep

def_attack: /(?i)DEF-ATTACK/ NAME "{" attack_def* "}" ";"

attack_def: threads
          | requests
          | attack_seq

threads: /(?i)THREADS/ NUMBER ";"
requests: /(?i)REQUESTS/ NUMBER ";"

attack_seq: /(?i)ATTACK-SEQ/ "{" attack_command+ "}" ";"

attack_command: get_command
              | post_command

get_command: /(?i)GET/ get_param* ";"
post_command: /(?i)POST/ post_param* ";"

post_param: /(?i)-url/ STRING
          | /(?i)-data/ STRING
          | /(?i)-json/ JSON
          | /(?i)-proxies/ STRING
          | /(?i)-referer/ STRING

get_param: /(?i)-url/ STRING
         | /(?i)-proxies/ STRING
         | /(?i)-referer/ STRING
     
start_attack: /(?i)START-ATTACK/ NAME ";"
stop_attack: /(?i)STOP-ATTACK/ NAME ";"
sleep: /(?i)SLEEP/ (FLOAT | NUMBER) ";"

NAME: /[A-Za-z_][A-Za-z0-9_]*/
FLOAT: /\d+\.\d+/
NUMBER: /\d+/
STRING: ESCAPED_STRING
JSON: /(?s)\{(?:[^{}"]|"(?:\\.|[^"\\])*"|\{(?:[^{}"]|"(?:\\.|[^"\\])*")*\})*\}/

%import common.ESCAPED_STRING
%import common.WS
%ignore WS
"""

parser = Lark(grammar)   