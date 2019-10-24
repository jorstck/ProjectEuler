import math

# Solved. My solution that I found on my own for m x n works but was too inefficient. The second function I found online and is much more efficient


def lattice_paths(m, n):
    if m == 1 or n == 1:
        return m+n
    else:
        return lattice_paths(m - 1, n) + lattice_paths(m, n - 1)


def efficient_lattice_paths(m, n):
    return math.factorial(m+n)//((math.factorial(m))*(math.factorial(n)))


print(efficient_lattice_paths(20, 20))
