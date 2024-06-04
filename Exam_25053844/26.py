with open('26_16390.txt') as f:
    s, n = map(int, f.readline().split())
    A = sorted([int(x) for x in f.readlines()])

    sum_p = 0
    i = 0
    while sum_p <= s:
        # print(i, sum_p)
        sum_p += A[i]
        i += 1
    sum_p = sum_p - A[i-1] - A[i-2]
    r = 1
    while s - sum_p < A[-r]:
        r += 1
    sum_p = sum_p + A[-r]
    print(i-1, A[-r])