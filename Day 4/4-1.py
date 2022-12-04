def input_to_ranges(pair: str):
    section1, section2 = pair.split(",")

    section1 = list(map(int, section1.split("-")))
    section2 = list(map(int, section2.split("-")))

    section1 = range(section1[0], section1[1] + 1)
    section2 = range(section2[0], section2[1] + 1)

    return section1, section2


with open("input.txt") as f:
    data = f.read().splitlines()

total = 0

for pair in data:
    section1, section2 = input_to_ranges(pair)

    if all(item in section1 for item in section2) or all(item in section2 for item in section1):
        total += 1

print(total)