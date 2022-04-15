class Game:
    def __init__(self, player_one_choice, player_two_choice):
        self.player_one_choice = player_one_choice
        self.player_two_choice = player_two_choice
        self._winner = ""
        self._winner_choice = ""

    def play_game(self, player_one, player_two):
        if player_one.choice == player_two.choice:
            self._winner = None
            return f'It is a draw since both players choose {player_one.choice}'

        if player_one.choice == "rock":
            if player_two.choice == "scissors":
                self._winner = player_one.name
                self._winner_choice = player_one.choice
            else:
                self._winner = player_two.name
                self._winner_choice = player_two.choice

        if player_one.choice == "scissors":
            if player_two.choice == "paper":
                self._winner = player_one.name
                self._winner_choice = player_one.choice
            else:
                self._winner = player_two.name
                self._winner_choice = player_two.choice

        if player_one.choice == "paper":
            if player_two.choice == "rock":
                self._winner = player_one.name
                self._winner_choice = player_one.choice
            else:
                self._winner = player_two.name
                self._winner_choice = player_two.choice

        return f'{self._winner} wins by playing {self._winner_choice}' 
