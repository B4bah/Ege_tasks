from itertools import product, permutations


def f(x, y, w, z):
    return (z == w) and (x <= y) or (not w)


for a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, a11 in product([0, 1], repeat=11):
    table = {(a1, a2, 0, 0), (a3, 0, 0, 0), (a4, 0, 0, a5), (a6, a7, a8, 0), (a9, a10, 0, a11)}
    for p in permutations('xywz'):
        if [f(**dict(zip(p, row))) for row in table] == [0, 0, 0, 0, 0]:
            print(*p)