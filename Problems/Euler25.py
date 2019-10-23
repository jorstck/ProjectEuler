def num_digits(number):
    return len(str(number))


Fib = [1, 1]
x = 1

while num_digits(Fib[x]) < 1000:
    Fib.append(Fib[x] + Fib[x])
    x += 1
    print(Fib[x], num_digits(Fib[x]))

print(x)

#print(num_digits(1), num_digits(10), num_digits(100))


#                       NOT SOLVED FOR SOME REASON IDK
