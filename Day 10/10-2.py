with open("input.txt") as f:
    data = f.read().splitlines()


class Device:
    def __init__(self):
        self.cycle = 0
        self.x = 1
        self.total = 0
        self.screen = list("." * 240)

    def do_cycle(self):
        pixel_x_pos = self.cycle % 40
        if abs(pixel_x_pos - self.x) <= 1:
            self.screen[self.cycle] = "#"
        self.cycle += 1

        # if self.cycle in [20, 60, 100, 140, 180, 220]:
        #     print(
        #         "Signal strength: %i at cycle %i with X: %i"
        #         % (self.cycle * self.x, self.cycle, self.x)
        #     )
        #     self.total += self.cycle * self.x

    def print_screen(self):
        self.screen = "".join(self.screen)
        print(" ".join(self.screen[0:40]))
        print(" ".join(self.screen[40:80]))
        print(" ".join(self.screen[80:120]))
        print(" ".join(self.screen[120:160]))
        print(" ".join(self.screen[160:200]))
        print(" ".join(self.screen[200:240]))
        self.screen = list(self.screen)


device = Device()


while data:
    i = data[0][:4]
    match i:
        case "noop":
            device.do_cycle()
        case "addx":
            device.do_cycle()
            device.do_cycle()
            device.x += int(data[0].split()[1])
        case _:
            print("ERROR - UNKNOWN INPUT: %s" % data[0])
    data = data[1:]

device.print_screen()
