# create
class Node:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node

    def set_next_node(self, next_node):
        self.next_node = next_node

    def get_next_node(self):
        return self.next_node

    def get_value(self):
        return self.value

# create a simplified stack data structure (no need to worry about max size)
class Stack:
    def __init__(self, head=None):
        self.head = head
    
    # set head as next node of current head, return removed item
    def remove(self):
        removed_item = self.head
        self.head = self.head.get_next_node()
        return removed_item

    def add(self, item):
        former_head = self.head
        self.head = item
        self.head.set_next_node(former_head)
    
    def peek(self):
        return self.head.get_value()

# how to process input of current state of stacks
# load each into a list, one for each stack
# reverse each list
# add list into Stack objects in a list (index will be offset by 1)
# stop when we hit numbers

num_stacks = 0
# find number of stacks by counting spacers plus 1
# then parse moves
with open('input.txt') as input:
    for line in input.readlines():
        if '1' in line:
            num_stacks = line.count('  ') + 1
            break

# turn directions into list - first is number of moves, second is from/to
# subtract one from stack numbers since list indexes start at 0
directions = []
with open('input.txt') as input:
    for line in input.readlines():
        if 'move' in line:
            new_line = line.lstrip('move ').rstrip('\n').split(' from ')
            new_line[0] = int(new_line[0])
            new_line[1] = [int(stack) - 1 for stack in new_line[1].split(' to ')]
            directions.append(new_line)

stack_lists = [[] for x in range(num_stacks)]

# add item to list (one for each stack) from top to bottom
with open('input.txt') as input:
    for line in input.readlines():
        if '1' in line: break
        stack_index = 0
        for i in range(1, num_stacks * 4 - 2, 4):
            if line[i] != ' ':
                stack_lists[stack_index].append(line[i])
            stack_index += 1

#reverse stack lists to add as nodes starting from the bottom

for list in stack_lists:
    list.reverse()

stacks = []
for stack in stack_lists:
    new_stack = Stack()
    for item in stack:
        new_stack.add(Node(item))
    stacks.append(new_stack)

# repeat the following specified number of times:
# remove stack from from, add to to
for move in directions:
    for time in range(move[0]):
        from_stack = stacks[move[1][0]]
        to_stack = stacks[move[1][1]]
        to_stack.add(from_stack.remove())

final_top_items = ''
for stack in stacks:
    final_top_items += stack.peek()

print(final_top_items)