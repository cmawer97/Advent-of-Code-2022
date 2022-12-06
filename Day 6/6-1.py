with open("input.txt") as f:
    data = f.read().splitlines()[0]

# Takes a string and returns True if all characters of the string are unique, otherwise returns False
def start_of_packet(s: str):
    while s:
        if s[0] in s[1:]:
            return False
        s = s[1:]
    return True


PACKET_SIZE = 4

for i in range(0, len(data) - PACKET_SIZE):
    if start_of_packet(data[i : i + PACKET_SIZE]):
        print(i + PACKET_SIZE)
        break
