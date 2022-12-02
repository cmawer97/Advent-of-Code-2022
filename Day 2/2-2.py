with open("input.txt") as f:
    data = f.read().splitlines()

'''
Opponent's picks:
A = Rock
B = Paper
C = Scissors

Your picks:
X = Lose
Y = Draw
Z = Win

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
    match line[0]:
        case 'A':
            match line[1]:
                case 'X':
                    roundscore += 3
                case 'Y':
                    roundscore += 4
                case 'Z':
                    roundscore += 8
        case 'B':
            match line[1]:
                case 'X':
                    roundscore += 1
                case 'Y':
                    roundscore += 5
                case 'Z':
                    roundscore += 9
        case 'C':
            match line[1]:
                case 'X':
                    roundscore += 2
                case 'Y':
                    roundscore += 6
                case 'Z':
                    roundscore += 7
        case _:
            print("ERROR - 1ST LETTER")
            break

    total += roundscore

print(total)