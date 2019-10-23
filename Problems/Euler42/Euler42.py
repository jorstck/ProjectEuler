# SOLVED
def main():
    f = open("E:\Jordan\Documents\VisualStudioCode\Euler42\words.txt")
    L = f.read().split(',')
    for x in range(len(L)):
        L[x] = L[x][1:len(L[x])-1]
        L[x] = [s.lower() for s in L[x]]
    ans = 0
    for x in L:
        if is_triangle_word(x):
            ans += 1
    print(ans)


def is_triangle_word(list):  # returns true if the word_sum is a triangular number
    word_sum = 0
    for x in list:
        word_sum += (ord(x)-96)
    trinum = 0
    found = False
    while not found:
        trinum += 1
        triangle = int((.5)*trinum*(trinum+1))
        if triangle == word_sum:
            found = True
        elif triangle > word_sum:
            break
    return found


if __name__ == "__main__":
    main()
