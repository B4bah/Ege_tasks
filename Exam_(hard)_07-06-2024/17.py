with open('17_8373.txt') as f:
    A = [int(x) for x in f.readlines()]
    min_even = min(x for x in A if x % 2 == 0)

    M = []
    for i in range(len(A)-1):
        if A[i] % min_even == 0:
            M.append([A[i-1], A[i+1]])
    k = 0
    min_p = 100000
    for p in M:
        if (p[0] % 2 == 0) ^ (p[1] % 2 == 0):
            print(p)
            k += 1
            min_p = min(min_p, sum(p))
    print(k, min_p)