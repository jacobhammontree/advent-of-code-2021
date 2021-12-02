def part1(instructions = [[]]):
    x_pos = 0
    depth = 0
    for i in instructions:
        direction = i[0]
        if direction == "up":
            depth-=i[1]
        elif direction == "down":
            depth+=i[1]
        elif direction == "forward":
            x_pos+=i[1]
    return x_pos * depth    

def part2(instructions = [[]]):
    aim = 0
    x_pos = 0
    depth = 0
    for i in instructions:
        direction = i[0]
        if direction == "up":
            aim-=i[1]
        elif direction == "down":
            aim+=i[1]
        elif direction == "forward":
            x_pos+=i[1]
            depth+=i[1]*aim
    return x_pos * depth

if __name__ == "__main__":
    instructions = []
    with open("day2_input.txt", "r") as f:
        for l in f.readlines():
            instructions.append(l.split(' '))
            instructions[-1][1] = int(instructions[-1][1])
    print(part1(instructions))
    print(part2(instructions))