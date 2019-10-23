import random  # not solved


def game():
    c = random.randint(1, 7)
    p = random.randint(1, 5)
    if c > p:
        return 0
    elif p > c:
        return 1
    else:
        return 2


cWins = 0
pWins = 0
draws = 0
for x in range(100000000):
    a = game()
    if a == 0:
        cWins += 1
    elif a == 1:
        pWins += 1
    else:
        draws += 1
print("ans: " + str(pWins / (cWins+pWins+draws)))
