import re
from collections import defaultdict

def draw_line_on_board(b,l,p2=False):
    if l[0][0] == l[1][0] or l[0][1] == l[1][1]: # if the line is horizontal or vertical
        for x in range(min(l[0][0], l[1][0]), max(l[0][0],l[1][0])+1):
            for y in range(min(l[0][1], l[1][1]), max(l[0][1],l[1][1])+1):
                b[(x,y)]+=1
    elif p2: # if the line is slanted
        left_point = l[0] if l[0][0] < l[1][0] else l[1]
        right_point = l[0] if l[0][0] > l[1][0] else l[1]
        slope = int((left_point[0]-right_point[0])/(left_point[1]-right_point[1]))
        y = left_point[1]
        for x in range(left_point[0],right_point[0]+1):
            b[(x,y)]+=1
            y+=slope
    return b

def init_board(n=0):
    board = defaultdict(lambda: n)
    return board

def init_lines(f):
    for l in f.readlines():
        matches = re.match(r"([0-9]+),([0-9]+) -> ([0-9]+),([0-9]+)", l)
        p1 = int(matches.groups()[0]),int(matches.groups()[1])
        p2 = int(matches.groups()[2]),int(matches.groups()[3])
        lines.append((p1,p2))
    return l

def part(b, lines, part2=False):
    for l in lines:
        b = draw_line_on_board(b,l,part2)
    count = 0
    for _,v in b.items():
        if v >= 2:
            count+=1
    return count

if __name__ == "__main__":
    lines = None
    with open("./python/day5/day5_input.txt", "r") as f:
        lines = init_lines(f)
    
    # part 1
    board = init_board()
    print(part(board,lines))

    # part 2
    board = init_board()
    print(part(board,lines,True))