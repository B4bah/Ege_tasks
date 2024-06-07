with open('27_B_1277.txt') as f:
    n = int(f.readline())
    A = sorted([sorted([int(x) for x in s.split()]) for s in f.readlines()])
    l = 1
    c = 0
    sum_m = sum(A[i][0] for i in range(n))
    if sum_m % 117 == 11:
        while c < len(A):
            if (sum_m - A[c][0] + A[c][l]) % 117 == 11:
                c += 1
            else:
                print(sum_m - A[c][0] + A[c][l])
                break