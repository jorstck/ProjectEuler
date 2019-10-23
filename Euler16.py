def addDigits(n):                      #From problem 20
    a = 0
    L = [int(a) for a in str(n)]
    for x in range (0, len(L)):
        a = a + L[x]
    return a


print (addDigits(2**1000))