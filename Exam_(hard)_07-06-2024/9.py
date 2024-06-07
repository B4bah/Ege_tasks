with open('09_8946.csv') as f:
    A = [[int(x) for x in s.split(';')] for s in f.readlines()]

    k = 0
    for line in A:
        line_m = line[0] * line[1] * line[2] * line[3] * line[4] // max(line)
        if max(line)**2 > line_m and sum(line) - sum(sorted(line)[-2:]) * 2 < sum(sorted(line)[-2:]):
            k += 1
    print(k)