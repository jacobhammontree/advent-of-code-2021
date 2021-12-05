from copy import deepcopy
from time import perf_counter as pc

def part1(diag_nums, diag_num_length):
    gamma_rate = []
    for i in range(diag_num_length):
        one_count = len([n[i] for n in diag_nums if n[i]=="1"])
        if(one_count>len(diag_nums)/2):
            gamma_rate.append("1")
        else:
            gamma_rate.append("0")
    gamma_rate = int("".join(gamma_rate),2)
    epsilon_rate = gamma_rate^(2**diag_num_length-1)
    power_consumption = gamma_rate*epsilon_rate
    return power_consumption

def part2(diag_nums,diag_num_length):
    ox_gen_candidates = deepcopy(diag_nums)
    co2_scrub_candidates = deepcopy(diag_nums)
    for i in range(diag_num_length):
        one_count = len([n[i] for n in ox_gen_candidates if n[i]=="1"])
        if(one_count>=len(ox_gen_candidates)/2):
            ox_gen_candidates = [x for x in ox_gen_candidates if x[i] == "1"]
        else:
            ox_gen_candidates = [x for x in ox_gen_candidates if x[i] == "0"]
        if len(ox_gen_candidates) == 1:
                break
    
    for i in range(diag_num_length):
        one_count = len([n[i] for n in co2_scrub_candidates if n[i]=="1"])
        if(one_count>=len(co2_scrub_candidates)/2):
            co2_scrub_candidates = [x for x in co2_scrub_candidates if x[i] == "0"]
        else:
            co2_scrub_candidates = [x for x in co2_scrub_candidates if x[i] == "1"]
        if len(co2_scrub_candidates) == 1:
                break

        
    ox_gen = int("".join(ox_gen_candidates[0]),2)
    co2_scrub = int("".join(co2_scrub_candidates[0]),2)
    life_support_rating = ox_gen * co2_scrub
    return life_support_rating

if __name__ == "__main__":
    p1_start = pc()
    diagnostic_nums = []
    with open("./python/day3/day3_input.txt") as f:
        for l in f.readlines():
            diagnostic_nums.append([c for c in l if c != '\n'])
    print(part1(diagnostic_nums,len(diagnostic_nums[0])))
    p1_stop = pc()
    p2_start = pc()
    print(part2(diagnostic_nums,len(diagnostic_nums[0])))
    p2_stop = pc()

    print("Times:")
    print(f"Part 1: {p1_stop-p1_start}")
    print(f"Part 2: {p2_stop-p2_start}")