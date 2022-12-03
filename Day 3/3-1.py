with open("input.txt") as f:
    data = f.read().splitlines()

total = 0
for rucksack in data:
    comp1 = rucksack[ : int(len(rucksack)/2) ]
    comp2 = rucksack[ int(len(rucksack)/2) : ]
    shared = [ord(i) for i in comp1 if i in comp2]
    if shared[0] in range(65,91):
        p = shared[0] - 38
    else:
        p = shared[0] - 96
    total += p
    print("Char " + chr(shared[0]) + " found with priority " + str(p))

print(total)