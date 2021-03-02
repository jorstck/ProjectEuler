import math

def factorial(n):                           #Find the sum of the digits in the number 100!
    if n == 2:                              #This uses two recursive functions
        return 2
    
    else:
        return n*factorial(n-1)
    
r = 0

def addDigits(n):                   #This recursive function that add digits of a number doesn't work for something
    if n == 0:
        return 0
    return(n%10 + addDigits(int(n/10)))

def addDigits2(n):                      #This non-recursive does work
    a = 0
    L = [int(a) for a in str(factorial(100))]
    for x in range (0, len(L)):
        a = a + L[x]
    return a


#print(addDigits(factorial(100)))
print(addDigits2(factorial(100)))


