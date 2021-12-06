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

if __name__ == "__main__":
    fish_d = defaultdict(lambda:0)
    with open("./python/day6/day6_input.txt", "r") as f:
        for l in f.readlines():
            for x in [int(x) for x in l.split(",")]:
                fish_d[x]+=1
    fish_d_cp = deepcopy(fish_d)
    for i in range(256):
        progress_one_day(fish_d)
        progress_one_day_2(fish_d_cp)
    count = 0
    for _,v in fish_d.items():
        count+=v
    count2 = 0
    for _,v in fish_d_cp.items():
        count2+=v
    print(count)
    print(count2)
