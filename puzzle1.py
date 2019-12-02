from math import floor

def calcul(nb):
    return floor(nb/3) - 2

def calul_with_mass(nb):
    if nb == 0:
        return 0
    else:
        acc = calcul(nb)
        if acc<0:
            acc = 0
        return acc + calul_with_mass(acc)


print(calcul(12))
print(calcul(14))
print(calcul(1969))
print(calcul(100756))

f = open("data/puzzle1.txt", "r")
f1 = f.readlines()
acc = 0
for nb in f1:
    acc += calcul(int(nb.replace("\n", "")))

print(acc)
f.close();


print(calul_with_mass(12))
print(calul_with_mass(14))
print(calul_with_mass(1969))
print(calul_with_mass(100756))
acc = 0
for nb in f1:
    acc += calul_with_mass(int(nb.replace("\n", "")))

print(acc)