def f(x):
    return ((x & 17 != 0) <= ((x & a != 0) <= (x & 58 != 0))) <= ((x & 8== 0) and (x & a != 0) and (x & 58 == 0))


for a in range(1, 100):
    if all(f(x) == 0 for x in range(1, 10000)):
        print(a)
        break