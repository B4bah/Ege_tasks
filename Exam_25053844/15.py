def f(x):
    return (x % a == 0) or (x % 28 != 0) or (x % 49 != 0)


for a in range(1, 1000):
    flag = 1
    for x in range(1, 10000):
        if f(x) == 0:
            flag = 0
            break
    if flag == 1:
        print(a)