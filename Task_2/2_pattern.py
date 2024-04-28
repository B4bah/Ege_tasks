'''2 ege task pattern'''


'''
from itertools import permutations


def f(.., .., ..,,):
    return ...
    

table = [(.., .., ..,,), (.., .., ..,,), (.., .., ..,,),,]

for p in permutations('......'):
    if [f(**dict(zip(p, row))) for row in table] == [.., .., ..,,]:
        print(p)
'''

'''
from itertools import permutations, product


def f(.., .., ..,,):
    return ...
    

for a1, a2, a3, a4, a5, a6, a7 in product([0, 1], repeat=7):
    table = [(.., .., ..,,), (.., .., ..,,), (.., .., ..,,),,]
    for p in permutations('......'):
        if [f(**dict(zip(p, row))) for row in table] == [.., .., ..,,]:
            print(*p)

'''