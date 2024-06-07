from itertools import product, permutations


def f(x, y, w, z):
    return (x or ((not z) or w) or w) == (y and (not x) and w)


for a1, a2, a3, a4 in product([0, 1], repeat=4):
    table = [(1, a1, a2, 0), (1, a3, 0, 0), (0, 1, a4, 1)]
    if len(set(table)) == len(table):
        for p in permutations('xywz'):
            if [f(**dict(zip(p, row))) for row in table] == [1, 1, 1]:
                print(*p)