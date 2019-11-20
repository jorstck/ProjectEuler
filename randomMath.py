# claim: for small theta, sin(theta) = theta (approx)
import math, numpy
for x in numpy.arange(0,1, 0.01):
    print(x, math.sin(x))