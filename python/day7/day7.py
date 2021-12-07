from collections import defaultdict

lookup = dict()

def part2(crabs):
    fuel_cost = defaultdict(lambda:0)
    for i in range(min(crabs), max(crabs)+1):
        for c in crabs:
            if abs(c-i) in lookup:
                fuel_cost[i]+=lookup[abs(c-i)]
            else:
                lookup[abs(c-i)] = sum([j for j in range(1,abs(c-i)+1)])
                fuel_cost[i]+=sum([j for j in range(1,abs(c-i)+1)])
    return min(fuel_cost.values())

def part1(crabs):
    fuel_cost = defaultdict(lambda:0)
    for i in range(min(crabs), max(crabs)+1):
        for c in crabs:
            fuel_cost[i]+=abs(c-i)
    return min(fuel_cost.values())

if __name__ == "__main__":
    crabs = list()
    with open("./python/day7/day7_input.txt", "r") as f:
        for l in f.readlines():
            if l:
                crabs = [int(c) for c in l.split(",")]
    print(part1(crabs))
    print(part2(crabs))