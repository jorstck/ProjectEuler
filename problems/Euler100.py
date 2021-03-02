def quadFormula(a,b,c): #wrong
    plus = (-b+(b**2-4*a*c)**.5)/(2*a)
    minus = (-b-(b**2-4*a*c)**.5)/(2*a)
    return plus, minus

print(quadFormula(1,-1,-((10**24-10**12)/2))[0])
print(quadFormula(1,-1,-((10**24-10**12)/2))[1])
