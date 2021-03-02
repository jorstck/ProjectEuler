dict1 = {0: 0, 1: 3, 2: 3, 3: 5, 4: 4, 5: 4, 6: 3, 7: 5, 8: 5, 9: 4,
         10: 3, 11: 6, 12: 6, 13: 8, 14: 8, 15: 7, 16: 7, 17: 9, 18: 8, 19: 8}

dict2 = {0: 0, 1: 3, 2: 6, 3: 6, 4: 6, 5: 5, 6: 5, 7: 7, 8: 6, 9: 6}
#                                                                       UNSOLVED


def num_chars(number, place):
    def addAnd(andBool):
        if not andBool:
            return 3
        else:
            return 0
    andBool = True
    if number == 0:
        return 0
    if place == 1 and str(number)[-2:] == "00" and len(str(number)) > 2:
        andBool = False
    if place == 1 and number % 100 < 20 and number % 100 > 9:
        return num_chars(number//100, 3) + dict1[number % 100] + addAnd(andBool)
    if place == 1:
        return num_chars(number//10, 2) + dict1[number % 10] + addAnd(andBool)
    if place == 2:
        return num_chars(number//10, 3) + dict2[number % 10]
    if place == 3:
        return dict1[number % 10] + 18


s = 0
for x in range(1001):
    s += num_chars(x, 1)
print(s)
