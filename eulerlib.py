''' 
This is a library that contains commonly used functions when solving Project Euler problems
GitHub: https://github.com/jorstck/ProjectEuler
Created by Jordan Stack
'''

from fractions import Fraction


# Checks if a number is a perfect square
def is_square(x: int) -> bool:
    if x < 0:
        return False
    return int(x**.5)**2 == x


# Checks if a number is prime
def is_prime(x: int) -> bool:
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
def list_prime_factors(number: int) -> list:
    list_factors = []
    while number != 1 or number != 1:
        for x in range(2, int(num**.5)):
            if number % x == 0 and is_prime(x):
                number /= x
                list_factors.append(x)
    return(list_factors)


# Returns sum of the digits of a number. Ex:    1234 -> 1 + 2 + 3 + 4 = 10
def digital_sum(number: int) -> int:
    return sum([int(s) for s in str(number)])


# Returns the number of digits of a number. Ex: 1 -> 1, 11 -> 2, 111 -> 3
def num_digits(number: int) -> int:
    return len(str(number))


# Returns true if the numerator of a number has more digits than denominator. Ex: 123/12 -> True, 1/12 -> False, 3/4 -> False
def more_digits_numerator(number: float) -> bool:
    frac = Fraction(number).limit_denominator()
    numLength = len(str(frac.numerator))
    denLength = len(str(frac.denominator))
    return numLength > denLength


# Returns true if the denominator of a number has more digits than numerator. Ex: 123/12 -> False, 1/12 -> True, 3/4 -> False
def more_digits_denomator(number: float) -> bool:
    frac = Fraction(number).limit_denominator()
    numLength = len(str(frac.numerator))
    denLength = len(str(frac.denominator))
    return numLength < denLength
