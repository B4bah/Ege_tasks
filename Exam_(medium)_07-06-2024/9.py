with open('09_8609.csv') as f:
    A = [[int(x) for x in s.split(';')] for s in f.readlines()]

    k = 0
    for line in A:
        if len(set(line)) == len(line) and (max(line) + min(line) * 2) <= (sum(line) - max(line) - min(line)) * 3:
            k += 1
    print(k)