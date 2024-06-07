def f(x, y):
    return (2 * x + y != 70) or (x < y) or (a < x)


for a in range(1000, -1, -1):
    if all(f(x, y) == 1 for x in range(200) for y in range(200)):
        print(a)
        break