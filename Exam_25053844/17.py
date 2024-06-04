with open('17_16383.txt') as f:
    A = [int(x) for x in f.readlines()]
    max_21 = max(x for x in A if abs(x) % 100 == 21 and 10000 <= abs(x) <= 99999)

    k = 0
    max_p = 0
    for i in range(len(A)-1):
        if ((abs(A[i]) % 100 == 21 and 10000 <= abs(A[i]) <= 99999) ^ (abs(A[i+1]) % 100 == 21 and 10000 <= abs(A[i+1]) <= 99999)) and \
           (A[i]**2 + A[i+1]**2) >= max_21**2:
            k += 1
            max_p = max(max_p, A[i] + A[i+1])
    print(k, max_p)