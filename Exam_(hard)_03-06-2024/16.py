from sys import setrecursionlimit

setrecursionlimit(1012)


def h(x):
    if x >= 4040: return x
    return x + 4 + h(x+4)


print(h(3) - h(15))