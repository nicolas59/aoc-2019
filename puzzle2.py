def run(data):
    index = 0;
    while True:
        op = data[index]
        if op == 99:
            break
        accPos = data[index+3]
        data[accPos] = data[data[index+1]] + data[data[index+2]] if op == 1 else data[data[index+1]] * data[data[index+2]]
        index+=4
    return data

assert run([1,9,10,3,2,3,11,0,99,30,40,50]) == [3500,9,10,70,2,3,11,0,99,30,40,50]
assert run([1,1,1,4,99,5,6,0,99]) == [30,1,1,4,2,5,6,0,99]

strToInt = lambda d: int(d)

f = open("data/puzzle2.txt", "r")
lines = f.readline().split(",");

intcodes = list(map(strToInt, lines ))
intcodes[1] = 12
intcodes[2] =  2
result = run(intcodes)
print(intcodes[0])

for noun in range(0, 99):
    for verb in range(0, 99):
        intcodes = list(map(strToInt, lines))
        intcodes[1] = noun
        intcodes[2] = verb
        result = run(intcodes);
        if intcodes[0] == 19690720:
            break
    else:
        continue
    break

print(noun * 100 + verb)

