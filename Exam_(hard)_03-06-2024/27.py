with open('27A_7880.txt') as f:
    n = int(f.readline())
    k = int(f.readline())
    A = [int(x) for x in f.readlines()]

    c = 0
    for l in range(len(A)):
        for r in range(l+1, min(l+k+1, len(A))):
            if A[l] != A[r]:
                if (A[l] + A[r]) % 17 == 0:
                    c += 1

    print(c)