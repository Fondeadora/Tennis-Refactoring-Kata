class TennisGame3:
    SCORE_DESCRIPTIONS = ["Love", "Fifteen", "Thirty", "Forty"]

    def __init__(self, player1_name, player2_name):
        self.player_one_name = player1_name
        self.player_two_name = player2_name
        self.player_one_score = 0
        self.player_two_score = 0

    def won_point(self, player_name):
        if player_name == "player1":
            self.player_one_score += 1
        else:
            self.player_two_score += 1

    def score(self):
        if self.is_early_game():
            return self.get_early_game_score()

        return self.get_end_game_score()

    def is_win(self):
        return abs(self.player_one_score - self.player_two_score) > 1

    def get_end_game_score(self):
        if self.is_tied():
            return "Deuce"

        leading_player = self.get_leading_player()

        if self.is_win():
            return "Win for " + leading_player

        return "Advantage " + leading_player

    def get_leading_player(self):
        if self.player_one_score > self.player_two_score:
            return self.player_one_name

        return self.player_two_name

    def get_early_game_score(self):
        game_stage = self.SCORE_DESCRIPTIONS[self.player_one_score]

        if self.is_tied():
            return game_stage + "-All"

        return game_stage + "-" + self.SCORE_DESCRIPTIONS[self.player_two_score]

    def is_tied(self):
        return self.player_one_score == self.player_two_score

    def is_early_game(self):
        return (self.player_one_score < 4 and self.player_two_score < 4) and (
            self.player_one_score + self.player_two_score < 6
        )
