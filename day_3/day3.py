class Rucksack:
    # set priority key/value pairs for each letter a-zA-Z
    priorities = {}
    for letter in 'abcdefghijklmnopqrstuvwxyz':
    # ord() returns Unicode code point for each letter
    # ord(a) = 97, ord(A) = 65 and increase by 1 for b/B, etc
    # so subtract 96 to assign a-z to 1-26 and 64 to assign A-Z to 27-52
    # since A starts at 27, subtract (64-26) = 38
        priorities[letter] = ord(letter) - 96
        priorities[letter.upper()] = ord(letter.upper()) - 38

    def __init__(self, contents_string):
        half_length = int(len(contents_string) / 2)
        # divide string into two compartments
        self.compartment_1 = contents_string[:half_length]
        self.compartment_2 = contents_string[half_length:]
        # find single character in common
        for character in self.compartment_1:
            if character in self.compartment_2:
                self.in_both = character
                self.in_both_priority = Rucksack.priorities[character]
                break

rucksacks = []
# open file and make each line into Rucksack object
with open('input.txt') as input:
    for contents_string in input.readlines():
        rucksacks.append(Rucksack(contents_string.strip('\n')))

total_priorities = 0
for rucksack in rucksacks:
    total_priorities += rucksack.in_both_priority

print(total_priorities)