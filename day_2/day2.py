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

games = []
# open file and add each line to calories
with open('input.txt') as input:
    for game in input.readlines():
        games.append(game.strip('\n').split(' '))

print(games)