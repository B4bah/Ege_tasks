with open('26_1275.txt') as f:
    s, n = map(int, f.readline().split())
    A = sorted([int(x) for x in f.readlines()])
    # s, n = 100, 7
    # A = sorted([10, 44, 66, 90, 65, 47, 34])

    k = 0
    sum_m = 0
    l = 0
    while sum_m <= s:
        k += 1
        sum_m += A[l]
        l += 1
    l -= 1
    k -= 1
    if s > sum_m - A[l]:
        sum_m -= A[l] + A[l-1]
    else:
        print(sum_m - A[l], k)
    sum_m -= A[l]
    l -= 1
    r = 0
    while sum_m + A[-r] > s:
        r += 1
    print(sum_m + A[-r-2], len(A)-l)