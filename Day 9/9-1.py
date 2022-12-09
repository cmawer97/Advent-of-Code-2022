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
        self.move_tail()

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


r = Rope(0, 0)
positions = set()
positions.add((r.tail.X, r.tail.Y))
for dir, dst in [move.split() for move in data]:
    for i in range(0, int(dst)):
        r.move_head(dir, 1)
        positions.add((r.tail.X, r.tail.Y))

    if abs(r.head.X - r.tail.X) > 1 and abs(r.head.Y - r.tail.Y) > 1:
        print(
            "Error - Head and tail are not touching (Head: %i,%i | Tail: %i,%i)"
            & (r.head.X, r.head.Y, r.tail.X, r.tail.Y)
        )
print(len(positions))
