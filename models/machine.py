from random import choice

class Machine:
    def __init__(self, machine_name):
        self.name = machine_name
        self.choice = ""
    
    def get_name(self):
        return self.name

    def get_choice(self):
        self.choice = choice(['rock', 'scissors', 'paper'])
        return self.choice