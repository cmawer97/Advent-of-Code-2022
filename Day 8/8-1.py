with open("input.txt") as f:
    data = [list(map(int, list(row))) for row in f.read().splitlines()]

total = 0


def checktree(data, x, y):
    tree_height = data[y][x]
    # print("Checking tree of height %i at co-ordinates (%i,%i)" % (tree_height, x, y))
    # Perimeter trees are always visible
    if x == 0 or x == len(data[0]) - 1:
        return True
    elif y == 0 or y == len(data) - 1:
        return True
    else:
        # Left
        if tree_height > max(data[y][:x]):
            return True
        # Right
        if tree_height > max(data[y][x + 1 :]):
            return True
        # Top
        if tree_height > max([row[x] for row in data[:y]]):
            return True
        # Bottom
        if tree_height > max([row[x] for row in data[y + 1 :]]):
            return True
    return False


total = 0

for index_y, row in enumerate(data):
    for index_x, tree in enumerate(row):
        if checktree(data, index_x, index_y):
            total += 1

print(total)
