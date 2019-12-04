import re

pattern = re.compile(".*(11|22|33|44|55|66|77|88|99)+.*")
pattern2 = re.compile("1{3,}|2{3,}|3{3,}|4{3,}|5{3,}|6{3,}|7{3,}|8{3,}|9{3,}")

matchExp = lambda exp: pattern.match(exp)
only_double = lambda exp: matchExp(pattern2.sub('', exp))

def check_increase(exp):
    for index in range(len(exp)-1):
        if int(exp[index]) > int(exp[index+1]):
            return False
    return True

assert matchExp("11111111")
assert not matchExp("12131415")

assert check_increase("123456")
assert check_increase("11111111")
assert not check_increase("1243456")


part1 = list(filter( lambda password: matchExp(password) and check_increase( password), (str(index) for index in range(136818, 685979))))
assert len(part1) == 1919

part2 = list(filter( lambda password: only_double(password), part1))
assert len(part2) == 1291
