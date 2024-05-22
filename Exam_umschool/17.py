with open('17.3.txt') as f:
    A = [int(x) for x in f.readlines()]
    B = []
    min_A = min(A)
    for i in range(len(A)-1):
        if A[i] % 123 == min_A or A[i+1] % 123 == min_A:
            B.append(A[i]+ A[i+1])
    print(len(B), max(B))