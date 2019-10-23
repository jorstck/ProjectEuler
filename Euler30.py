def separate_digits(number):                #solved
    L = [int(n) for n in str(number)]
    return L

def exponentiateArray(array):
    sum = 0
    for x in range(len(array)):
        sum += array[x]**5
    return sum

answer = 0
j = 0
k = 2
while j<1000000:
    if k == exponentiateArray(separate_digits(k)):
        answer += k
        print(k)
        j=0
    else:
        j+=1
    k+=1


print(answer)