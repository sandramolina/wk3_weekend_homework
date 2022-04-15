class Rock():
    def __init__(self):
        self.name = "rock"
    def fight(self, opponent):
        return opponent.fight_against_rock()
    def fight_against_rock(self):
        return None
    
    def fight_against_scissors(self):
        return self

    def fight_against_paper(self, opponent):
        return opponent

class Scissors():
    def __init__(self):
        self.name = "scissors"
    def fight(self, opponent):
       return opponent.fight_against_scissors()
    
    def fight_against_rock(self, opponent):
        return opponent

    def fight_against_scissors(self):
        return None

    def fight_against_paper(self):
        return self

class Paper():
    def __init__(self):
        self.name = "paper"
    def fight(self, opponent):
        return opponent.fight_against_paper()

    def fight_against_rock(self):
        return self
    
    def fight_against_scissors(self, opponent):
        return opponent

    def fight_against_paper(self):
        return None

class Player():
    def __init__(self, input_name, input_choice):
        self.name = input_name
        self.choice = input_choice

scissors = Scissors()
rock = Rock()
paper = Paper()

# print(rock.fight(paper))

player_2 = Player("San", scissors)
player_1 = Player("Fede", rock)

class Game:
    def __init__(self, player_one, player_two):
        self.player_one_choice = player_one.choice
        self.player_two_choice = player_two.choice
        self._winner = ""
        self._winner_choice = ""
    
    def play_game(self):
        return self.player_one_choice.fight(self.player_two_choice)

game1 = Game(player_1, player_2)
print(game1.play_game())
