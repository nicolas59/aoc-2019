import re
from math import fabs

def move(grid, direction, stepSize, coord):
    sign =  -1 if direction == 'L' or direction == 'D' else 1
    (x, y) = (coord[0], coord[1])
    for i in range(1, stepSize+1):
        if direction == "R" or direction == "L":
            grid[coord[1]][coord[0] + sign*i] += 1
            (x, y) = (coord[0]+ sign*i, y )
        else:
            grid[coord[1] + sign * i][coord[0]] += 1
            (x, y) = (x, coord[1]+ sign * i)
    return (grid, (x,y) )

def display (grid):
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            print(grid[i][j], end=" ")
        print("\n")

def drawWire(grid, wire):
    print("Prepare grid")
    pattern = re.compile("([R|L|U|D]{1})([0-9]+)")
    currentX = int(len(grid) / 2);
    currentY = int(len(grid) / 2);

    for item in wire:
        matcher = pattern.match(item)@
        (direction, stepSize) = matcher.group(1,2)
        (x,y) = (currentX, currentY)
        result = move(grid,direction,int(stepSize), (x,y) )
        grid = result[0]
        (currentX, currentY) = result[1]
    return grid

def intersect(grid1, grid2):
    print("Intersept")
    ret = [[0 for _ in range(len(grid1))] for _ in range(len(grid1))]
    print("compute intercept")
    for i in range(len(grid1)):
        for j in range(len(grid1[i])):
            if grid1[i][j] == 1 and grid2[i][j]==1:
                ret[i][j] = 2
            elif grid1[i][j] == 1 or grid2[i][j]==1:
                ret[i][j] = 1
    return ret



def run(wire1, wire2, n):
    pattern = re.compile("([R|L|U|D]{1})([0-9]+)")

    grid1  = [[0 for _ in range(n)] for _ in range(n)]
    grid2 = [[0 for _ in range(n)] for _ in range(n)]

    currentX = int(n/2);
    currentY = int(n/2);
    grid1[currentY][currentX] = 1;
    grid2[currentY][currentX] = 1;

    grid1 = drawWire(grid1, wire1)
    grid2 = drawWire(grid2, wire2)

    #display(grid1 )
    #display(grid2)

    cross = intersect(grid1, grid2)
    cross[int(n/2)][int(n/2)] =1


    ret = 999999999
    print("Compute manhattan")
    for i in range(len(cross)):
        for j in range(len(cross[i])):
            if cross[i][j] == 2:
                r = fabs(i - int(n/2))+ fabs(j - int(n/2))
                if r < ret:
                    ret = r

    return int(ret)

#run(["R8","U5","L5","D3"], ["U7","R6","D4","L4"], 20)

#print(run(["R8","U5","L5","D3"], ["U7","R6","D4","L4"], 20) )

#assert run(["R8","U5","L5","D3"], ["U7","R6","D4","L4"], 20) == 6

#assert run(["R75","D30","R83","U83","L12","D49","R71","U7","L72"],["U62","R66","U55","R34", "D71","R55","D58","R83"], 1000) == 159
#assert run(["R98","U47","R26","D63","R33","U87","L62","D20","R33","U53","R51"],["U98","R91","D20","R16","D67","R40","U7","R15","U6","R7"], 1000) == 135

f = open("data/puzzle3.txt", "r")
lines = f.readlines()

print(run(lines[0].split(","), lines[1].split(","), 20000))