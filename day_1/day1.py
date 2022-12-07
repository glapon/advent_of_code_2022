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
top_3 = []

for elf in elves:
    cals = elf.get_total_cals()
    if cals > most_calories:
        most_calories = cals
    if len(top_3) < 3:
        top_3.append(cals)
        top_3.sort()
    else:
        # replace the smallest one its bigger than, then sort again
        for i in range(3):
            if cals > top_3[i]:
                top_3[i] = cals
                top_3.sort()
                break

# calories of elf with most (part 1 answer)
print(most_calories)
sum_top_3 = 0
for num in top_3:
    sum_top_3 += num
print(sum_top_3)