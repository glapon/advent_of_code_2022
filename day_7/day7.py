class File:
    def __init__(self, name, size):
        self.name = name
        self.size = size

    def __repr__(self):
        return 'file'
    
    def get_size(self):
        return self.size
    
    def check_same(self, other):
        if self.name == other.name and self.size == other.size:
            return True
        else: return False

class Directory:
    def __init__(self, name, contents=[], parent=None):
        self.name = name
        self.contents = contents
        self.update_size()
        self.parent = parent

    def __repr__(self):
        return 'dir'
    
    def update_size(self):
        self.size = 0
        for item in self.contents:
            if repr(item) == 'dir':
                self.size += item.update_size()
            else:
                self.size += item.get_size()
        return self.size

    def check_same(self, other):
        if self.name == other.name and self.size == other.size:
            return True
        else: return False

    def already_in_dir(self, item):
        for existing in self.contents:
            if item.name == existing.name and item.size == existing.size:
                return True
        return False
    
    def add_to_dir(self, item):
        if not self.already_in_dir(item):
            self.contents.append(item)
            self.update_size()

    def get_size(self):
        return self.size

    def get_parent(self):
        return self.parent



with open('input.txt') as input:
    for line in input.readlines():
        