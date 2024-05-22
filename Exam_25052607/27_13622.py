with open('27B.txt') as f:
    k = int(f.readline())
    n = int(f.readline())
    A = sorted([int(x) for x in f.readlines()])[::-1]

    l = 0
    r = n - 1
    m = 0
    while l < r:
        if A[l] + A[r] > k:
            l += 1
            r -= 1
            m += 2
        else:
            r -= 1
    print(m)