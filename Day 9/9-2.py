with open("input.txt") as f:
    data = f.read().splitlines()


class Point:
    def __init__(self, X: int, Y: int):
        self.X = X
        self.Y = Y

    def __copy__(self):
        return Point(self.X, self.Y)


class Rope:
    def __init__(self, x: int, y: int):
        self.head = Point(x, y)
        self.tail = Point(x, y)

    def move_head(self, direction: str, distance: int):
        match direction.upper():
            case "U":
                self.head.Y += distance
            case "D":
                self.head.Y -= distance
            case "L":
                self.head.X -= distance
            case "R":
                self.head.X += distance
            case _:
                print("Error, direction string [ %s ] not valid" % direction)

    def move_tail(self):
        # Tail is same X, and within 1 Y, do nothing
        if (self.head.X - self.tail.X == 0) and (abs(self.head.Y - self.tail.Y) < 2):
            pass
        # Tail is same Y, within 1 X, do nothing
        elif (self.head.Y - self.tail.Y == 0) and (abs(self.head.X - self.tail.X) < 2):
            pass
        # Tail is same X, more than 1 Y different, move tail 1 closer in Y direction
        elif (self.head.X - self.tail.X == 0) and (abs(self.head.Y - self.tail.Y) >= 2):
            if self.tail.Y < self.head.Y:
                self.tail.Y += 1
            else:
                self.tail.Y -= 1
        # Tail is same Y, more than 1 X different, move tail 1 closer in X direction
        elif (self.head.Y - self.tail.Y == 0) and (abs(self.head.X - self.tail.X) >= 2):
            if self.tail.X < self.head.X:
                self.tail.X += 1
            else:
                self.tail.X -= 1
        # Tail is diagonally out, but touching. Do nothing.
        elif (abs(self.head.X - self.tail.X) < 2) and (
            abs(self.head.Y - self.tail.Y) < 2
        ):
            pass
        # Tail is diagonally out and not touching. Move tail 1 diagonally toward head.
        else:
            if self.tail.X < self.head.X:
                self.tail.X += 1
            else:
                self.tail.X -= 1
            if self.tail.Y < self.head.Y:
                self.tail.Y += 1
            else:
                self.tail.Y -= 1


def simulate_rope(ropes):
    for rope in ropes:
        rope.move_tail()


# Generate 9 'ropes', each rope's head being the tail of the rope before. In the context of the question, we can treat the array of ropes as the question's longer rope, and the head of each rope in the array, as well as the tail of the final rope, as a knot.
# The tail of the rope (as written in the question) is the final knot (ropes[-1].tail)
ropes = [Rope(0, 0) for i in range(0, 9)]
for i in range(1, 9):
    ropes[i].head = ropes[i - 1].tail
positions = set()
positions.add((0, 0))

for dir, dst in [move.split() for move in data]:
    for i in range(0, int(dst)):
        ropes[0].move_head(dir, 1)
        simulate_rope(ropes)
        positions.add((ropes[-1].tail.X, ropes[-1].tail.Y))
print(len(positions))
