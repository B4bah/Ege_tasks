# from itertools import permutations, product
#
#
# def f(x, y, w, z):
#     return (x and (not y)) or (y == z) or w
#
#
# for a1, a2, a3, a4, a5 in product([0, 1], repeat=5):
#     table = [(a1, 0, a2, 0), (a3, 0, a4, 0), (0, 0, a5, 0)]
#     for p in permutations('xywz'):
#         if [f(**dict(zip(p, row))) for row in table] == [0, 0, 0]:
#             print(*p)

def f(x, y, w, z):
    return (x and (not y)) or (y == z) or w


print('x w z y')
for x in range(2):
    for y in range(2):
        for w in range(2):
            for z in range(2):
                if not f(x, y, w, z):
                    print(x, w, z, y)