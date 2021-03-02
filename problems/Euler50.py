def is_prime(n: int) -> bool:          # not solved
    """ Determines whether or not a number is prime
    @param n: the number in question
    @return true if n is prime, false if it isn't
    """
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n % 3 == 0 or n == 1:
        return False
    else:
        for i in range(2, int(n**.5) + 1):
            if n % i == 0:
                return False
        return True


list_primes = []
for x in range(1000):
    if is_prime(x):
        list_primes.append(x)

for i in range(len(list_primes)):
    for j in range(len(list_primes), i, -1):
        # print(j)
        sum = 0
        for k in range(i, j):
            sum += list_primes[k]
        if is_prime(sum):
            print(sum)
