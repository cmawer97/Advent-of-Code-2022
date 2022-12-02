with open("input.txt") as f:
    data = f.read().splitlines()

'''
Opponent's picks:
A = Rock
B = Paper
C = Scissors

Your picks:
X = Rock
Y = Paper
Z = Scissors

Score:
Rock = 1
Paper = 2
Scissors = 3

Loss = 0
Draw = 3
Win = 6
'''

total = 0

for line in data:
    roundscore = 0
    line = line.split()

    match line[1]:
        case 'X':
            roundscore += 1
            match line[0]:
                case 'A':
                    roundscore += 3
                case 'B':
                    roundscore += 0
                case 'C':
                    roundscore += 6
        case 'Y':
            roundscore += 2
            match line[0]:
                case 'A':
                    roundscore += 6
                case 'B':
                    roundscore += 3
                case 'C':
                    roundscore += 0
        case 'Z':
            roundscore += 3
            match line[0]:
                case 'A':
                    roundscore += 0
                case 'B':
                    roundscore += 6
                case 'C':
                    roundscore += 3
        case _:
            print("ERROR - 2ND LETTER")
            break

    total += roundscore

print(total)