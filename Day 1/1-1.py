with open("input.txt") as f:
    data = f.read().splitlines()

maxcals = 0
elftotal = 0

for i in data:
    if i == '':
        maxcals = max(maxcals, elftotal)
        elftotal = 0
    else:
        elftotal += int(i)

print(maxcals)