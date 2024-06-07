from itertools import product, permutations


def f(x, y, w, z):
    return (x or (not y)) and (not (x == z)) and w


for a1, a2, a3, a4 in product([0, 1], repeat=4):
    table = {(a1, 0, 0, 1), (0, 0, 1, 1), (0, a2, a3, a4)}
    for p in permutations('xywz'):
        if [f(**dict(zip(p, row))) for row in table] == [1, 1, 1]:
            print(*p)