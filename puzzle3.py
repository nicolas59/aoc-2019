import re
from math import fabs
from dataclasses import dataclass

@dataclass(init=True, repr=True, eq=True, unsafe_hash=True)
class Point:
    x:int
    y:int

vectors = {
    'R': Point(x=1, y=0),
    'L': Point(x=-1, y=0),
    'U': Point(x=0, y=1),
    'D': Point(x=0, y=-1)
}

def compute_positions(wire):
    pattern = re.compile("([R|L|U|D]{1})([0-9]+)")
    visited_points = {}
    last_location = Point(x=0, y=0)
    steps = 0
    for item in wire:
        matcher = pattern.match(item)
        (direction, stepSize) = matcher.group(1,2)
        vector = vectors[direction]
        for _ in range(int(stepSize)):
            steps += 1;
            last_location = Point(last_location.x + vector.x, last_location.y + vector.y)
            if visited_points.get(last_location) == None:
                visited_points[last_location] = steps
    return visited_points

def get_manhattan(p1, p2):
    ret = 999999999
    for key in p1.keys():
        if p2.get(key) != None:
            r = fabs(key.x) + fabs(key.y)
            ret = r if r<ret else ret
    return int(ret)

def get_min_step(p1, p2):
    min_step = 99999999999
    for key in p1.keys():
        if p2.get(key) != None:
            r = p1[key] + p2[key]
            min_step = r if r < min_step  else min_step
    return int(min_step)

assert get_manhattan(compute_positions(["R8","U5","L5","D3"]), compute_positions(["U7","R6","D4","L4"])) == 6
assert get_manhattan(compute_positions(["R75","D30","R83","U83","L12","D49","R71","U7","L72"]),compute_positions(["U62","R66","U55","R34", "D71","R55","D58","R83"])) == 159
assert get_manhattan(compute_positions(["R98","U47","R26","D63","R33","U87","L62","D20","R33","U53","R51"]),compute_positions(["U98","R91","D20","R16","D67","R40","U7","R15","U6","R7"])) == 135

f = open("data/puzzle3.txt", "r")
lines = f.readlines()

assert get_manhattan(compute_positions(lines[0].split(",")), compute_positions(lines[1].split(","))) == 721

assert get_min_step(compute_positions(["R8","U5","L5","D3"]), compute_positions(["U7","R6","D4","L4"])) == 30
assert get_min_step(compute_positions(["R75","D30","R83","U83","L12","D49","R71","U7","L72"]),compute_positions(["U62","R66","U55","R34", "D71","R55","D58","R83"])) == 610
assert get_min_step(compute_positions(["R98","U47","R26","D63","R33","U87","L62","D20","R33","U53","R51"]),compute_positions(["U98","R91","D20","R16","D67","R40","U7","R15","U6","R7"])) == 410
assert(get_min_step(compute_positions(lines[0].split(",")), compute_positions(lines[1].split(",")))) == 7388
