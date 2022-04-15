from flask import redirect, render_template
from app import app
from models.game import Game
from models.player import Player

@app.route('/')
def home():
    return render_template("index.html", title="Home")

@app.route('/<player_one_choice>/<player_two_choice>', methods=['GET', 'POST'])
def game_result(player_one_choice, player_two_choice):
    player_one = Player("Player One", player_one_choice)
    player_two = Player("Player Two", player_two_choice)
    first_game = Game(player_one_choice, player_two_choice)
    game_result = first_game.play_game(player_one, player_two)
    
    return render_template("result.html", title="result", result=game_result)
    
