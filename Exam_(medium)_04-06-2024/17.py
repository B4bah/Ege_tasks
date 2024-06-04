with open('17_7682.txt') as f:
    A = [int(x) for x in f.readlines()]
    max_570 = max(y for y in A if abs(y) % 570 == 0)

    k = 0
    m = 0
    for i in range(len(A)-3):
        if sum(A[i:i+4]) / 4 > abs(max_570):
            k += 1

    for j in range(len(A)-2):
        if sum(1 for x in A[j:j+3] if x > 0) >= 2 and abs(sum(A[j:j+3])) % 34 == 0:
            m += 1
    print(k, m)