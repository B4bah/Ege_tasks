with open('26(1)-31-05-2024.txt') as f:
    n, k = map(int, f.readline().split())
    A = [int(x) for x in f.readlines()]
    A = sorted(A)[k:-k]
    print(A[:10])
    print(A[0], int(sum(A)/len(A)))

with open("26(1)-31-05-2024.txt") as F:

    n, k = map(int, F.readline().split())

    a = []

    for i in range(n):

        izm = F.readline()

        a.append(int(izm))

    a.sort()

    a = a[k:-k]

    summa = sum(a)

    sred = int(summa / len(a))

    print(a[0], sred)