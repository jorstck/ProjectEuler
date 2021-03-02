def num_solutions(p):  # solved
    sum = 0
    for x in range(p):
        for y in range(p):
            z = p - x - y
            if x**2 + y**2 == z**2 and y > x and z > y:
                # print_solution(x,y,z)
                sum += 1
    return sum


def print_solution(x, y, z):
    print("[" + str(x) + "," + str(y) + "," + str(z) + "]")


ans = 1

for x in range(1, 1001):
    print(x)
    if num_solutions(x) > num_solutions(ans):
        print(str(x) + " ----> " + str(num_solutions(x)))
        ans = x

print(ans)
