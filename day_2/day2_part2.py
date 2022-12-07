class Rock:
    def __init__(self):
        self.name = 'rock'
        self.score = 1
        self.beats = 'scissors'
    #what to choose to achieve result against rock
    def win(self):
        return Paper()
    
    def lose(self):
        return Scissors()

    def draw(self):
        return Rock()

class Paper:
    def __init__(self):
        self.name = 'paper'
        self.score = 2
        self.beats = 'rock'
    #what to choose to achieve result against rock
    def win(self):
        return Scissors()
    
    def lose(self):
        return Rock()

    def draw(self):
        return Paper()

class Scissors:
    def __init__(self):
        self.name = 'scissors'
        self.score = 3
        self.beats = 'paper'
    #what to choose to achieve result against rock
    def win(self):
        return Rock()
    
    def lose(self):
        return Paper()

    def draw(self):
        return Scissors()

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
    if letter == 'A': return Rock()
    elif letter == 'B': return Paper()
    elif letter == 'C': return Scissors()

def your_move(letter, their_move):
    if letter == 'X': return their_move.lose()
    elif letter == 'Y': return their_move.draw()
    elif letter == 'Z': return their_move.win()
       
games = []
# open file and make each game into objects
with open('input.txt') as input:
    for game in input.readlines():
        game_split = game.strip('\n').split(' ')
        their_move = make_move(game_split[0])
        games.append(Game(their_move, your_move(game_split[1], their_move)))

total_score = 0
for game in games:
    total_score += game.score_game()

print(total_score)