with open('27B.txt') as f:
    k = int(f.readline())
    n = int(f.readline())
    A = sorted([int(x) for x in f.readlines()])[::-1]
    # A = [x for x in A if A[0] + x > k]
    # print(len(A))

    # k = 10
    # n = 5
    # A = sorted([8, 1, 6, 3, 5])[::-1]
    # A = [x for x in A if A[0] + x > k]

    # I = set()
    # m = 0
    # for i in range(len(A)):
    #     if not (i in I):
    #         p = len(A)-i-1
    #         while A[i] + A[p] <= k:
    #             I.add(p)
    #             p -= 1
    #         I.add(p)
    #         m += 2
    #     I.add(i)
    # print(m)

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