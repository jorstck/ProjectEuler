import eulerlib as el

max_sum = 1
for a in range(100):
    for b in range(100):
        if el.digital_sum(a ** b) > max_sum:
            max_sum = el.digital_sum(a ** b)

print(max_sum)

# SOLVED
