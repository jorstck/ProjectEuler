namesArray = open(
    "Euler/Euler22/names.txt").read().replace('"', '').split(',')
namesArray.sort()

sum = 0


def nameValue(string, x):
    sum = 0
    for s in string:
        sum += (ord(s) - 64)
    return sum * x


for x in range(len(namesArray)):
    sum += nameValue(namesArray[x], x+1)

print(sum)


#                                       SOLVED
