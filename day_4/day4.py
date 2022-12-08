class Assignment:
    def __init__(self, sections):
        section_list = sections.split('-')
        self.start = int(section_list[0])
        self.end = int(section_list[1])
    
    # check if one is fully contained with other
    def fully_contains(self, other):
        # other contains self
        if self.start >= other.start and self.end <= other.end:
            return True
        elif other.start >= self.start and other.end <= self.end:
            return True
        else: return False

# list of pairs of assignments
pairs = []
# open file and make each line into Rucksack object
with open('input.txt') as input:
    for pair in input.readlines():
        pair_list = pair.strip('\n').split(',')
        first_elf = Assignment(pair_list[0])
        second_elf = Assignment(pair_list[1])
        pairs.append([first_elf, second_elf])

fully_contain_count = 0
for pair in pairs:
    fully_contain_count += int(pair[0].fully_contains(pair[1]))

print(fully_contain_count)