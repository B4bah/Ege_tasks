from random import randint

for _ in range(50):
    n = 50
    A = [randint(-1000, 1000) for _ in range(n)]

    max_a = - 10 ** 20

    for l in range(n):
        for m in range(l+1, n):
            for r in range(m+2, n):
                max_a = max(max_a, sum(A[m+1:r+1]) - sum(A[l:m+1]))

    pref = [0] * n
    for i in range(1, n):
        pref[i] = pref[i-1] + A[i]
    pref = [0] + pref

    max_l = [- 10 ** 20] * (n + 1)
    for i in range(1, n+1):
        max_l[i] = max(max_l[i-1], pref[i])

    max_r = [- 10 ** 20] * (n + 1)
    max_r[-1] = pref[-1]
    for i in range(n-1, -1, -1):
        max_r[i] = max(max_r[i+1], pref[i])

    max_b = - 10 ** 20
    for m in range(2, n-2):
        max_b = max(max_b, (max_r[m+2] - pref[m]) - (pref[m] - max_l[m-2]))
    print(max_a, max_b)