import eulerlib as el
from fractions import Fraction

sum = 0
addition = 0
for x in range(1001):
    expansion = 1 + 1 / (2 + addition)
    addition = expansion - 1
    if el.more_digits_numerator(expansion):
        sum += 1
    frac = Fraction(expansion).limit_denominator(1000000)
    print(frac, el.more_digits_numerator(expansion))

print(sum)


# NOT SOLVED
