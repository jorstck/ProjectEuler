''' 
This is a library that contains commonly used functions when solving Project Euler problems
GitHub: https://github.com/jorstck/ProjectEuler
Created by Jordan Stack
'''


# Checks if a number is a perfect square
def is_square(x):
    if x < 0:
        return False
    return floor(x**.5)**2 == x


# Checks if a number is prime
def is_prime(x):
    if x <= 1:
        return False
    elif x <= 3:
        return True
    elif x % 2 == 0 or x % 3 == 0:
        return False
    else:
        for i in range(5, int(x**.5), 2):
            if x % i == 0:
                return False
        return True


# Returns a list of the prime factors of a number
def list_prime_factors(num):
    list_factors = []
    while num != 1 or num != 1:
        for x in range(2, int(num**.5)):
            if num % x == 0 and is_prime(x):
                num /= x
                list_factors.append(x)
    return(list_factors)


# Returns sum of the digits of a number. Ex:    1234 -> 1 + 2 + 3 + 4 = 10
def digital_sum(number):
    return sum([int(s) for s in str(number)])
