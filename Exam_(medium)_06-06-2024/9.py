with open('9.6_12795.csv') as f:
    A = [[int(x) for x in s.split(';')] for s in f.readlines()]

    k = 0
    for line in A:
        avg = sum(line) // 7
        if avg in line:
            k += 1
    print(k)