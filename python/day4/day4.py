from copy import deepcopy
from time import perf_counter as pc

def check_board(b):
    won = False
    col_results = []
    for i in range(5):
        col_results.append([True for x in [b[i] for i in range(i,25,5)] if x == "x"])
    row_results = []
    for i in range(0,len(b),5):
        row_results.append([True for y in [b[i] for i in range(i,i+5)] if y == "x"])
    if any([len(x) == 5 for x in col_results]) or any([len(y) == 5 for y in row_results]):
        return True
    
    return False

def check_off(b,n):
    for i in range(len(b)):
        if(b[i]==n):
            b[i]="x"

def sum_board(b):
    sum = 0
    for n in b:
        try:
            sum+=int(n)
        except:
            pass
    return sum

def part1(boards,nums):
    for n in nums:
        for b in boards:
            check_off(b,n)
        for b in boards:
            if(check_board(b)):
                return int(n)*sum_board(b)

def part2(boards,nums):
    for n in nums:
        for b in boards:
            check_off(b,n)
        boards_cp = deepcopy(boards)
        for i in range(len(boards)):
            if(check_board(boards[i])):
                if (len(boards) == 1):
                    return int(n)*sum_board(b)
                boards_cp[i] = []
        boards = [b for b in boards_cp if b]



if __name__ == "__main__":
    p1_start = pc()
    nums = []
    boards = []
    lines = []

    with open("./python/day4/day4_input.txt", "r") as f:
        lines = f.readlines()

    nums = [x.replace("\n","") for x in lines.pop(0).split(",")]

    working_board = []
    while lines:
        line = lines.pop(0).replace("\n","")
        if not line:
            boards.append(working_board)
            working_board = []
            continue
        for n in line.split(" "):
            if(n):
                working_board.append(n)
    boards.append(working_board)
    boards = [b for b in boards if b] # Get rid of empty boards

    print(part1(deepcopy(boards),nums))
    p1_stop = pc()
    p2_start = pc()
    print(part2(deepcopy(boards),nums))
    p2_stop = pc()
    print("Times:")
    print(f"Part 1: {p1_stop-p1_start}")
    print(f"Part 2: {p2_stop-p2_start}")