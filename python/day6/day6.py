from collections import defaultdict
from copy import deepcopy

def progress_one_day(fish=defaultdict(lambda:0), n=8):
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

# Same as above, but a bit more extensible with looping
def progress_one_day_2(fish=defaultdict(lambda:0), n=8):
    n_zero = fish[0]
    for i in range(0,n+1):
        if i == n:
            fish[i] = n_zero
        elif i == 6:
            fish[i] = fish[7]+n_zero
        else:
            fish[i] = fish[i+1]
    return fish

def process_days(fish,days=256,n=8,progress=progress_one_day):
    for i in range(days):
        progress(fish,n)
    return fish

def count_fish(f):
    count = 0
    for v in f.values():
        count+=v
    return count

if __name__ == "__main__":
    fish_d = defaultdict(lambda:0)
    with open("./python/day6/day6_input.txt", "r") as f:
        for l in f.readlines():
            for x in [int(x) for x in l.split(",")]:
                fish_d[x]+=1
    process_days(fish_d,days=80,progress=progress_one_day_2)
    count = count_fish(fish_d)
    print(count)