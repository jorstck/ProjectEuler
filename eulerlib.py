''' 
This is a library that contains commonly used functions when solving Project Euler problems
GitHub: https://github.com/jorstck/ProjectEuler
Created by Jordan Stack
'''

from fractions import Fraction


def is_square(x: int) -> bool:
    '''
    x: number that is being checked to see if its a perfect square
    returns true if x is a perfect square, false if not
    '''
    if x < 0:
        return False
    return int(x**.5)**2 == x


def is_prime(x: int) -> bool:
    '''
    x: number whose primality is being checked
    returns true if x is prime, false if not
    '''
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


def list_primes_under_n(n: int) -> list:
    '''
    n: an integer
    returns a list of primes under n
    Ex: list_primes_under_n(10) -> [2,3,5,7]
    '''
    return [x for x in range(n) if is_prime(x)]


def list_prime_factors(number: int) -> list:
    '''
    number: an integer
    returns a list of prime factors for the given number
    '''
    list_factors = []
    while number != 1 or number != 1:
        for x in range(2, int(number**.5)):
            if number % x == 0 and is_prime(x):
                number /= x
                list_factors.append(x)
    return(list_factors)


def digital_sum(number: int) -> int:
    '''
    number: an integer
    returns a sum of the digits of the given number
    Ex: 1234 -> 1 + 2 + 3 + 4 = 10

    '''
    return sum([int(s) for s in str(number)])


def num_digits(number: int) -> int:
    '''
    number: an integer
    returns the number of digits in the number
    Ex: 1 -> 1, 11 -> 2, 111 -> 3
    '''
    return len(str(number))


def more_digits_numerator(number: float) -> bool:
    '''
    number: the number in question
    returns true if number of digits in numerator is larger than number of digits in denominator
    Ex: 123/12 -> True, 1/12 -> False, 3/4 -> False
    '''
    frac = Fraction(number).limit_denominator()
    numLength = num_digits(frac.numerator)
    denLength = num_digits(frac.denominator)
    return numLength > denLength


def more_digits_denomator(number: float) -> bool:
    '''
    number: the number in question
    returns true if number of digits in denominator is larger than number of digits in numerator
    Ex: 123/12 -> False, 1/12 -> True, 3/4 -> False
    '''
    frac = Fraction(number).limit_denominator()
    numLength = num_digits(frac.numerator)
    denLength = num_digits(frac.denominator)
    return numLength < denLength


def lattice_paths(m: int, n: int) -> int:
    '''
    m, n: the size of the lattice grid
    returns the number of routes from top left of grid to bottom of grid, when you can only move down and right. 
    This can be used for the number of combinations of 2n items taken n at a time
    '''
    return math.factorial(m+n)//((math.factorial(m))*(math.factorial(n)))

