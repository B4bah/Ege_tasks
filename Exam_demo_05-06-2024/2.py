from itertools import product, permutations


def f(x, y, w, z):
    return (x and (not y)) or (y == z) or (not w)


for a1, a2, a3, a4 in product([0, 1], repeat=4):
    table = {(a1, a2, 0, 0), (1, 0, a3, 0), (1, 0, 1, a4)}
    for p in permutations('xywz'):
        if [f(**dict(zip(p, row))) for row in table] == [0, 0, 0]:
            print(*p)