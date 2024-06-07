with open('17_4415.txt') as f:
    A = [int(x) for x in f.readlines()]

    k = 0
    max_r = 0
    for i in range(len(A) - 1):
        if abs(A[i] - A[i+1]) % 60 == 0:
            k += 1
            max_r = max(max_r,abs(A[i] - A[i+1]))
    print(k, max_r)