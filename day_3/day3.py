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
        self.contents_string = contents_string
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

# open file and make each line into Rucksack object
with open('input.txt') as input:
    rucksacks = [Rucksack(contents_string.strip('\n')) for contents_string in input.readlines()]

total_priorities = 0
for rucksack in rucksacks:
    total_priorities += rucksack.in_both_priority

print(total_priorities)

# part 2
groups_of_3 = [rucksacks[x:x+3] for x in range(0, len(rucksacks), 3)]

badge_priority_total = 0

for group in groups_of_3:
    # find letter from first rucksack that is in other two
    for letter in group[0].contents_string:
        if letter in group[1].contents_string and letter in group[2].contents_string:
            badge_priority_total += Rucksack.priorities[letter]
            break

print(badge_priority_total)