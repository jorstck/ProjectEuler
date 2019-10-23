import math

def separate_digits(number):                #solved
    L = [int(n) for n in str(number)]
    return L

def factorialArray(array):
    sum = 0
    for x in range(len(array)):
        sum += math.factorial(array[x])
    return sum

answer = 0
j = 0
k = 3
while j<100000:
    if k == factorialArray(separate_digits(k)):
        answer += k
        print(k)
        j=0
    else:
        j+=1
    k+=1


print(answer)