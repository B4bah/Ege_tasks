with open('9.csv') as f:
    A = [[int(x) for x in s.split(';')] for s in f.readlines()]

    k = 0
    for line in A:
        if (len(set(line)) == len(line)) ^ (2*(max(line) + min(line)) <= 3*(sum(line)-max(line)-min(line))):
            k += 1
    print(k)