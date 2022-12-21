class File:
    def __init__(self, name, size, parent):
        self.name = name
        self.size = size
        self.parent = parent

    def __repr__(self):
        return 'file'
    
    def get_size(self):
        return self.size

class Directory:
    def __init__(self, name, parent=None, children=[]):
        self.name = name
        self.children = children
        self.update_size()
        self.parent = parent

    def __repr__(self):
        return 'dir'
    
    def update_size(self):
        self.size = 0
        for item in self.children:
            self.size += item.get_size()
        return self.size

    def check_same(self, other):
        if self.name == other.name and self.parent == other.parent:
            return True
        else: return False

    def already_in_dir(self, item):
        for existing in self.children:
            if self.check_same(item):
                return True
        return False
    
    def add_to_dir(self, item):
        if not self.already_in_dir(item):
            self.children.append(item)
            self.update_size()

    def get_size(self):
        return self.size

    def get_parent(self):
        return self.parent

    def get_children(self):
        return self.children

home_dir = Directory('/')
current_dir = home_dir

with open('input.txt') as input:
    for line_raw in input.readlines():
        line = line_raw.lstrip('$ ')
        if line == 'cd /':
            current_dir = home_dir
        elif line == 'ls': pass
        else:
            commands = line.split(' ')
            if commands[0] == 'cd' and commands[1] == '..':
                current_dir = current_dir.get_parent()
            # if cd and dir name, add new dir with current dir as parent and change current dir
            elif commands[0] == 'cd':
                # create new dir with parent as current_dir
                new_dir = Directory(commands[1], current_dir)
                current_dir.add_to_dir(new_dir)
                current_dir = new_dir
            # if number first, it's a file from ls. add file to current dir
            elif commands[0].isnumeric():
                new_file = File(commands[1], int(commands[0]), current_dir)
                current_dir.add_to_dir(new_file)
            elif commands[0] == 'dir':
                new_dir = Directory(commands[1], current_dir)
                current_dir.add_to_dir(new_dir)

all_dirs = [home_dir]

def add_children_all_dirs(dir):
    for child in dir.get_children():
        print(child)
        all_dirs.append(child)
        if len(child.get_children()) > 0:
            add_children_all_dirs(child)

for child in home_dir.get_children():
    if repr(child) == 'dir':
        add_children_all_dirs(child)

total_size = 0

for dir in all_dirs:
    size = dir.get_size()
    if size <= 100000: total_size += size

print(total_size)