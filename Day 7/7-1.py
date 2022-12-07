with open("input.txt") as f:
    data = f.read().splitlines()


class Directory:
    def __init__(self, name, parent, contents):
        self.name = name
        self.parent = parent
        self.contents = contents

    def add_item(self, item):
        if item not in self.contents:
            self.contents.append(item)

    def calculate_size(self):
        return (sum([f.size for f in self.contents if isinstance(f, File)])) + (
            sum([d.calculate_size() for d in self.contents if isinstance(d, Directory)])
        )

    def append_dirs_to_list(self, list):
        for i in self.contents:
            if isinstance(i, Directory):
                list.append(i)
                i.append_dirs_to_list(list)


class File:
    def __init__(self, name: str, size: int):
        self.name = name
        self.size = size


filesys = Directory("/", None, [])
currentdir = filesys
for line in data:
    if line == "$ cd /":
        currentdir = filesys
    elif line == "$ cd ..":
        currentdir = currentdir.parent
    elif line[:4] == "$ cd":
        currentdir = [
            dir
            for dir in currentdir.contents
            if isinstance(dir, Directory) and dir.name == line[5:]
        ][0]
    elif line[:3] == "dir":
        currentdir.add_item(Directory(line[4:], currentdir, []))
    elif line == "$ ls":
        continue
    else:  # We have a file!
        size, name = line.split()
        currentdir.add_item(File(name, int(size)))

dirlist = []
filesys.append_dirs_to_list(dirlist)
print(sum([d.calculate_size() for d in dirlist if d.calculate_size() <= 100000]))
