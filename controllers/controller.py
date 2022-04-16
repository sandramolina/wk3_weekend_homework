from flask import render_template, request
from app import app
from models.game import Game
from models.machine import Machine
from models.player import Player

@app.route('/')
def home():
    return render_template("index.html", title="Home")

@app.route('/<player_one_choice>/<player_two_choice>', methods=['GET', 'POST'])
def game_result(player_one_choice, player_two_choice):
    player_one_name = request.form["name1"]
    player_one_choice = request.form["choice1"]

    player_two_name = request.form["name2"]
    player_two_choice = request.form["choice2"]

    player_one = Player(player_one_name, player_one_choice)
    player_two = Player(player_two_name, player_two_choice)

    game = Game(player_one, player_two)
    game_result = game.play_game()
    
    return render_template("result.html", title="result", result=game_result)
    
@app.route('/play', methods=["GET", "POST"])
def play_against_the_machine():    
    if request.method == "POST":
        player_name = request.form.get("user_name", False)
        player_choice = request.form.get("choice", False)
        player_one = Player(player_name, player_choice)

        the_machine = Machine("The Machine")
        
        game = Game(player_one, the_machine)
        game_result = game.play_game()

        return render_template("play.html", title="Play", result=game_result)
    
    else:
        return render_template("play.html", title="Play")