with open('9_2050.csv') as f:
    A = [sorted([int(x) for x in s.split(';')]) for s in f.readlines()]

    k = 0
    for line in A:
        if len(set(line)) == 3:
            if line[2] / line[1] == line[1] / line[0]:
                k += 1
    print(k)