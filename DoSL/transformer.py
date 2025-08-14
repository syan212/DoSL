from lark import Transformer, Tree, Token
from lark.exceptions import UnexpectedToken
from .attack import Attack
import json
import time

class DoSLTransformer(Transformer):
    def __init__(self):   
        self.attacks = {}
    def start(self, commands):
        for cmd in commands:
            '''
            cmd.children[0].data: Top level command name
            cmd.children[0].children[1].value: Top level command data, i.e. def-attack `Num1`
            cmd.children[0].children[2]: def-attack tree
            attack_def.children[0].data: Attack_def type. 
                                         Use for attack_def in cmd.children[0].children[2:]
            attack_def.children[0].children[1:]: Attack_def command arguments, Tree or Token. 
                                                 Use for attack_def in cmd.children[0].children[2:]
            attack_def.children[0].children[1].value: Attack_def commands arguements, as a string
                                                 Use for attack_def in cmd.children[0].children[2:]
            attack_command.children[0]: Unwrapped attack_command tree. 
                                        Use for attack_def in cmd.children[0].children[2:] and 
                                            for attack_command in attack_def.children[0].children[1:]
            attack_command.children[0].data: Attack command type
                                        Use for attack_def in cmd.children[0].children[2:] and 
                                            for attack_command in attack_def.children[0].children[1:]
            attack_command.children[0].children[1:]: Attack command tree
                                        Use for attack_def in cmd.children[0].children[2:] and 
                                            for attack_command in attack_def.children[0].children[1:]
            param.children: Attack commands params like [Token('__ANON_6', '-url'), Token('STRING', '"example.com"')]
                                        Use for attack_def in cmd.children[0].children[2:] and 
                                            for attack_command in attack_def.children[0].children[1:] and
                                            for param in attack_command.children[0].children[1:]
            '''
            top_command_name = cmd.children[0].data
            # Def-attack block
            if top_command_name == 'def_attack':
                # Initialize attack object
                attack_name = cmd.children[0].children[1].value
                attack = Attack(attack_name, executor)
                # Work through Attack Def Tree
                for attack_def in cmd.children[0].children[2:]:
                    # If the attack children is a Tree, meaning attack-seq
                    if type(attack_def.children[0].children[1]) == Tree:
                        # Go throughs commands and params
                        for attack_command in attack_def.children[0].children[1:]:
                            params = {}
                            for param in attack_command.children[0].children[1:]:
                                # String or JSON
                                if param.children[1].type == 'STRING':
                                    params[param.children[0].value] =  param.children[1].value[1:-1]
                                elif param.children[1].type == 'JSON':
                                    params[param.children[0].value] =  json.loads(param.children[1].value)
                            if attack_command.children[0].data == 'get_command':
                                attack.add_command('GET', params)
                            elif attack_command.children[0].data == 'post_command':
                                attack.add_command('POST', params)
                    # Simply threads or requests
                    elif type(attack_def.children[0].children[1]) == Token:
                        # Set threads or requests
                        if attack_def.children[0].data == 'threads':
                            attack.set_threads(int(attack_def.children[0].children[1].value))
                        elif attack_def.children[0].data == 'requests':
                            attack.set_requests(int(attack_def.children[0].children[1].value))
            # Start attack
            elif top_command_name == 'start_attack':
                attack_name = cmd.children[0].children[1].value
                attack = self.attacks[attack_name]
                attack.start_attack()
            elif top_command_name == 'sleep':
                delay = float(cmd.children[0].children[1].value)
                print(f'Sleeping for {delay} seconds')
                time.sleep(delay)
                print(f'Finished sleeping for {delay} seconds')
            else:
                raise Exception(f'Commands recognised by parser but not by transformer: {top_command_name}')

executor = DoSLTransformer()