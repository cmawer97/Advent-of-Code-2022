with open("input.txt") as f:
    data = f.read().splitlines()

maxcals = 0
topelves = [0, 0, 0]
elftotal = 0

for i in data:
    if i == '':
        if min(topelves) < elftotal:
            topelves.remove(min(topelves))
            topelves.append(elftotal)
        elftotal = 0
    else:
        elftotal += int(i)

print(sum(topelves))