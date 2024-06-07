from fnmatch import fnmatch

for x in range(2291, 10**10, 2291):
    if fnmatch(str(x), '*222132?'):
        print(x, x // 2291)