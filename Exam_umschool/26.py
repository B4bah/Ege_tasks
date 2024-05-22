with open('26.1.txt') as f:
    n = int(f.readline())
    A = sorted([int(x) for x in f.readlines()])[::-1]
    k = 5
    B = [max(A)]
    l = 0
    i = 1
    while i < n:
        if B[l] - A[i] >= 5:
            B.append(A[i])
            l += 1
            i += 1
        else:
            i += 1
    print(len(B), min(B))