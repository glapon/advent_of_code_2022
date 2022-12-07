class Rock:
    def __init__(self):
        self.name = 'rock'
        self.score = 1
        self.beats = 'scissors'

class Paper:
    def __init__(self):
        self.name = 'paper'
        self.score = 2
        self.beats = 'rock'

class Scissors:
    def __init__(self):
        self.name = 'scissors'
        self.score = 3
        self.beats = 'paper'

class Game:
    def __init__(self, opponent, player):
        self.total_score = player.score
        #beat them you get 6
        if player.beats == opponent.name:
            self.total_score += 6
        # they don't beat you, draw, you get 3
        elif player.name != opponent.beats:
            self.total_score += 3
    
    def score_game(self):
        return self.total_score

def make_move(letter):
    if letter in ['A', 'X']: return Rock()
    elif letter in ['B', 'Y']: return Paper()
    elif letter in ['C', 'Z']: return Scissors()        

games = []
# open file and make each game into objects
with open('input.txt') as input:
    for game in input.readlines():
        game_split = game.strip('\n').split(' ')
        games.append(Game(make_move(game_split[0]), make_move(game_split[1])))

total_score = 0
for game in games:
    total_score += game.score_game()

print(total_score)