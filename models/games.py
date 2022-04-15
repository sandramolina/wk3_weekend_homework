from game import *
from player import *

player_one = Player("Spongebob Squarepants", "Scissors")
player_two = Player("Patrick Star", "Scissors")

first_game = Game(player_one.choice, player_two.choice)
print(first_game.play_game(player_one, player_two))