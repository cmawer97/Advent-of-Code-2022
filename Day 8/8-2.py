with open("input.txt") as f:
    data = [list(map(int, list(row))) for row in f.read().splitlines()]

total = 0


def check_tree_visible(data, x, y):
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


def check_tree_score(data, x, y):
    tree_height = data[y][x]
    # Look left
    left_score = 0
    left = data[y][:x][::-1]
    for tree in left:
        left_score += 1
        if not tree < tree_height:
            break
    # Look right
    right_score = 0
    right = data[y][x + 1 :]
    for tree in right:
        right_score += 1
        if not tree < tree_height:
            break
    # Look up
    up_score = 0
    up = [row[x] for row in data[:y][::-1]]
    for tree in up:
        up_score += 1
        if not tree < tree_height:
            break
    # Look down
    down_score = 0
    down = [row[x] for row in data[y + 1 :]]
    for tree in down:
        down_score += 1
        if not tree < tree_height:
            break

    return left_score * right_score * up_score * down_score


top = 0

for index_y, row in enumerate(data):
    for index_x, tree in enumerate(row):
        top = max(top, check_tree_score(data, index_x, index_y))

print(top)
