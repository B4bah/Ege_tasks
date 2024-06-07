with open('17_2679.txt') as f:
    A = [int(x) for x in f.readlines()]
    max_m = max(y for y in A if len(str(y)) > 1 and str(y)[-1] == str(y)[-2])

    k = 0
    max_s = 0
    for i in range(len(A) - 1):
        if (abs(A[i]) % 5 == 0 or abs(A[i]) % 7 == 0 or abs(A[i+1]) % 5 == 0 or abs(A[i+1]) % 7 == 0) and A[i] + A[i+1] <= max_m:
            k += 1
            max_s = max(max_s, A[i] + A[i+1])
    print(k, max_s)