with open("input.txt") as f:
    data = f.read().splitlines()


class CPU:
    def __init__(self):
        self.cycle = 0
        self.x = 1
        self.total = 0

    def do_cycle(self):
        self.cycle += 1
        if self.cycle in [20, 60, 100, 140, 180, 220]:
            print(
                "Signal strength: %i at cycle %i with X: %i"
                % (self.cycle * self.x, self.cycle, self.x)
            )
            self.total += self.cycle * self.x


cpu = CPU()

while data:
    i = data[0][:4]
    match i:
        case "noop":
            cpu.do_cycle()
        case "addx":
            cpu.do_cycle()
            cpu.do_cycle()
            cpu.x += int(data[0].split()[1])
        case _:
            print("ERROR - UNKNOWN INPUT: %s" % data[0])
    data = data[1:]

print(cpu.total)
