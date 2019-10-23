def numFactors(n):
    k = 2
    for x in range(2, int(n**.5)):
        if n%x == 0:
            k = k + 2
    return k

h = True
t = 1
i = 2
while(h):
    t = t + i
    i = i + 1
    if numFactors(t) > 500:
        h = False
        
print(t)