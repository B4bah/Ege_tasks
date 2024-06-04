with open('27_A_16391.txt') as f:
    n = f.readline()
    A = [int(x) for x in f.readlines()]
    # n = 7
    # A = [100, 300, 400, 9300, 800, 500, 9500]
    # print(len(A), max(A), min(A))

    l = 0
    r = 0
    r_sum = sum(A[l:len(A) - r + 1])
    M = set()
    while len(A) - r > 0:
        # if len(A) - r <= len(A) // 4:
        #     l = 0
        #     r += 1
        #     r_sum = sum(A[l:len(A) - r + 1])
        # print(l, len(A)-r, r_sum)
        if sum(A[l:len(A)-r+1]) >= 263 and r_sum % 263 == 0:
            M.add(len(A) - r - l + 1)
            l = 0
            r += 1
            r_sum = sum(A[l:len(A) - r + 1])
        elif l == len(A) - r:
            l = 0
            r += 1
            r_sum = sum(A[l:len(A)-r+1])
        else:
            r_sum -= A[l]
            l += 1

    print(max(M))