from fnmatch import fnmatch

for x in range(98, 10**8+1, 98):
    if fnmatch(str(x), '12*678?'):
        print(x, x // 98)