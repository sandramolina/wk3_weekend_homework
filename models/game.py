class Game:
    def __init__(self, player_one, player_two):
        self.player_one_name = player_one.get_name()
        self.player_one_choice = player_one.get_choice()
        self.player_two_name = player_two.get_name()
        self.player_two_choice = player_two.get_choice()
        self._winner = ""
        self._winner_choice = ""

    def play_game(self):
        if self.player_one_choice == "Select your choice for the game":
            return f'{self.player_one_name} should chose a correct option'
        
        if self.player_two_choice == "Select your choice for the game":
            return f'{self.player_two_name} should chose a correct option'
            
        if self.player_one_choice == self.player_two_choice:
            self._winner = None
            return f'It is a draw since both players choose {self.player_one_choice}'

        if self.player_one_choice == "rock":
            if self.player_two_choice == "scissors":
                self._winner = self.player_one_name
                self._winner_choice = self.player_one_choice
            else:
                self._winner = self.player_two_name
                self._winner_choice = self.player_two_choice

        if self.player_one_choice == "scissors":
            if self.player_two_choice == "paper":
                self._winner = self.player_one_name
                self._winner_choice = self.player_one_choice
            else:
                self._winner = self.player_two_name
                self._winner_choice = self.player_two_choice

        if self.player_one_choice == "paper":
            if self.player_two_choice == "rock":
                self._winner = self.player_one_name
                self._winner_choice = self.player_one_choice
            else:
                self._winner = self.player_two_name
                self._winner_choice = self.player_two_choice
        
        return f'{self._winner} wins by playing {self._winner_choice}' 
