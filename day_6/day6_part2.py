# read file as string
with open('input.txt') as input:
    data = input.read()

def all_unique(string):
    for letter in string:
        if string.count(letter) > 1: return False
    return True

letters_read = 13
while letters_read < len(data):
    letters_read += 1
    if all_unique(data[letters_read - 14:letters_read]):
        print(letters_read)
        break