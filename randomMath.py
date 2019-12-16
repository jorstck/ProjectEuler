from mpmath import mp 
mp.dps = 5000
print(mp.quad(lambda x: mp.exp(-x**2), [-mp.inf, mp.inf]) ** 2)

