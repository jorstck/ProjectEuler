import random
k = 10 #how many attempts                   #not solved
expectedValue = 0

a = random.random()
b = random.random()

for x in range(1,k):
    if k == round(((k*a+1)**2+(k*b+1)**2)**.5):
        print(k)    
        expectedValue += k


print(expectedValue)
