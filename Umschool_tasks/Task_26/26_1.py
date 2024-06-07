with open('26.1.txt') as f:
    # n = int(f.readline())
    # A = sorted([int(x) for x in f.readlines()])
    n = 5
    A = sorted([43, 38, 32, 40, 30])
    D = [A[0]]
    D = [A[0]] + [x for x in A if x - D[-1] >= 5]
    print(len(D), D[0])