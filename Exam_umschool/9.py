with open('9.csv') as f:
    A = [[int(x) for x in s.split(';')] for s in f.readlines()]
    k = 0
    for line in A:
        line_s = sorted(line)
        if line_s[0] * line_s[3] == line_s[1] * line_s[2] and line_s[-1] ** 2 > line_s[1] * line_s[0]:
            print(line_s)
            k += 1
    print(k)