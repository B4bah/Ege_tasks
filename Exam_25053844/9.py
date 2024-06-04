with open('9.csv') as f:
    A = [[int(x) for x in s.split(';')] for s in f.readlines()]

    k = 0
    for line in A:
        p = sum(line) - sum(set(line))
        set_line_p = sorted(set(line) - {p})
        if len(set(line)) == 6 and set_line_p[0] * set_line_p[1] * set_line_p[2] > p**2:
            k += 1
    print(k)