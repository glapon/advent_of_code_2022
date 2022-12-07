class Elf:
    def __init__(self, list_of_calories):
        self.list_of_calories = list_of_calories
        self.total_calories = 0
        if len(list_of_calories) > 0:
            for calorie in list_of_calories:
                self.total_calories += calorie
    
    def get_total_cals(self):
        return self.total_calories

elves = []

temp_list = []
# open file and add each line to calories
with open('input.txt') as input:
    for calories in input.readlines():
        # create new elf from previous list of calories if empty line
        if calories == '\n':
            elves.append(Elf(temp_list))
            temp_list = []
        else:
            temp_list.append(int(calories.strip('\n')))
    # at end, create one last elf with what is left, if any are left (assuming input has no blank line at end)
    if len(temp_list) > 0:
        elves.append(Elf(temp_list))
            
most_calories = 0
for elf in elves:
    cals = elf.get_total_cals()
    if cals > most_calories:
        most_calories = cals

# calories of elf with most
print(most_calories)