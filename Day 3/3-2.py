with open("input.txt") as f:
    data = f.read().splitlines()

total = 0
for i in range(0, int(len(data)/3)):
    sack1 = data[i*3]
    sack2 = data[i*3 + 1]
    sack3 = data[i*3 + 2]
    shared = [ord(i) for i in sack1 if (i in sack2) and (i in sack3)]
    print("Sack 1: %s\nSack 2: %s\nSack 3: %s\nShared: %s\n" % (sack1, sack2, sack3, chr(shared[0])))

    if shared[0] in range(65,91):
        p = shared[0] - 38
    else:
        p = shared[0] - 96
    total += p

print(total)