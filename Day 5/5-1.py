with open("input.txt") as f:
    data = f.read().splitlines()

# Get initial crate stacks
datastacks = data[:data.index([i for i in data if i[:2] == " 1"][0])]
datamoves = [list(map(int, move.split()[1::2])) for move in data[data.index("") + 1:]]

stacks = []

for stack in range(0, len(datastacks) + 1):
    stacks.append(list())

for line in datastacks:
    for stack in range(1, len(datastacks[0]), 4):
        if line[stack] != " ":
            stacks[int(stack/4)].insert(0, line[stack])

for instruction in datamoves:
    for move in range(0, instruction[0]):
        crane_contents = stacks[instruction[1] - 1].pop()
        stacks[instruction[2] - 1].append(crane_contents)

answer_string = ""

for stack in stacks:
    answer_string += stack[-1]

print(answer_string)