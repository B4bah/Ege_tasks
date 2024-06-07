from fnmatch import fnmatch

for x in range(999, 10 ** 9, 999):
    if fnmatch(str(x), '13*57?9'):
        if len(str(x)) == 9:
            print(x, x // 999)