from collections import defaultdict

def progress_one_day(fish=defaultdict(lambda:0)):
    new_zero = fish[1]
    new_one = fish[2]
    new_two = fish[3]
    new_three = fish[4]
    new_four = fish[5]
    new_five = fish[6]
    new_six = fish[7] + fish[0]
    new_seven = fish[8]
    new_eight = fish[0]

    fish[0] = new_zero
    fish[1] = new_one
    fish[2] = new_two
    fish[3] = new_three
    fish[4] = new_four
    fish[5] = new_five
    fish[6] = new_six
    fish[7] = new_seven
    fish[8] = new_eight
    return fish

if __name__ == "__main__":
    fish_d = defaultdict(lambda:0)
    with open("./python/day6/day6_input.txt", "r") as f:
        for l in f.readlines():
            for x in [int(x) for x in l.split(",")]:
                fish_d[x]+=1
    for i in range(500):
        progress_one_day(fish_d)
    count = 0
    for _,v in fish_d.items():
        count+=v
    print(count)

