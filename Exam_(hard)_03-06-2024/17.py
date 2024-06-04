with open('17_4414.txt') as f:
    A = [int(x) for x in f.readlines()]

    k = 0
    max_r = 0
    for i in range(len(A)):
        for j in range(i+1, len(A)):
            if A[i] != A[j]:
                if abs(A[i] - A[j]) % 36 == 0 and (A[i] % 13 == 0 or A[j] % 13 == 0):
                    k += 1
                    max_r = max(max_r, abs(A[i] - A[j]))
    print(k, max_r)