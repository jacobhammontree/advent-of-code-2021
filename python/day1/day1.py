def part1(depths=[]):
    count = 0
    for i in range(1,len(depths)):
        count = count + 1 if depths[i]>depths[i-1] else count
    return count

def part2(depths=[]):
    count = 0
    for i in range(0,len(depths)-2):
        count = count + 1 if sum(depths[i+1:i+4]) > sum(depths[i:i+3]) else count
    return count

if __name__ == "__main__":
    depths = []
    with open("day1_input.txt") as f:
        depths = [int(l) for l in f.readlines()]
    print(part1(depths))
    print(part2(depths))