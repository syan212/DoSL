import threading
import requests
import os
from threading import Thread, Lock, Event

class Attack:
    def __init__(self, name, executor):
        self.name = name
        self.commands = []
        self.threads = None
        self.requests = None
        self.threads = []
        self.stop_event = Event()
        executor.attacks[name] = self

    def set_threads(self, num):
        self.threads = num

    def set_requests(self, num):
        self.requests = num

    def add_command(self, method, params):
        self.commands.append((method, params))
    
    def start_attack(self):
        proxy_lock = Lock()

        # Change working directory to the script's directory
        os.chdir(os.path.dirname(os.path.abspath(__file__)))
        print(f'Starting Attack: {self.name}')
        print(f'Threads: {self.threads}')
        print(f'Requests: {self.requests}')
        for command in self.commands:
            print(f'{command[0]}: {command[1:]}')