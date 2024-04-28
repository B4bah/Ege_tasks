from itertools import permutations, product


def f(k, l, m, n):
    return (not k <= m) and (k or n) or (l <= n)


for a1, a2, a3, a4, a5, a6, a7 in product([0, 1], repeat=7):
    table = {(1, a1, a2, 0), (a3, a4, a5, 1), (0, 1, a6, a7)}
    for p in permutations('klmn'):
        if [f(**dict(zip(p, row))) for row in table] == [0, 0, 0]:
            print(*p)
