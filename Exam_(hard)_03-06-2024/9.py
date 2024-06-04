with open('9.csv') as f:
    A = [[int(x) for x in s.split(';')] for s in f.readlines()]

    k = 0
    for line in A:
        line_r = {x for x in line if line.count(x) == 3}
        if len(line_r) == 1 and len(set(line)) == 4:
            line_unr = set(line) - line_r
            print(line, line_r, line_unr)
            if (sum(line_unr) / 3) <= 3 * sum(line_r):
                k += 1
    print(k)