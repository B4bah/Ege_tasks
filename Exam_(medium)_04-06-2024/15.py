def f(x, y):
    return (x >= 27) or (2 * x < 3 * y) or ((x + 2) * (y - 3) < a)


for a in range(300, 500):
    if all(f(x, y) == 1 for x in range(1000) for y in range(1000)):
        print(a)
        break