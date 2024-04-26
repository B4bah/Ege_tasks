''' 15'th ege task'''

'''
segments:

from itertools import combinations


def f(x):
    A = st <= x <= end
    P = st_P <= x <= end_P
    Q = st_Q <= x <= end_Q
    return ...


K = [k * 0.25 for k in range(..*4, (max(P, Q)+4)*4+1)]
M = []
for st, end in combinations(K, 2):
    if all(f(x) == .. for x in K):
        M += [end-st]
print(round(min/max(M))

'''

'''
sets:

A = set()
P = {.., ..,,}
Q = {.., ..,,}


def f(x):
    a = x in A
    p = x in P
    q = x in Q
    return ...


k = 0
for x in range(.., 10000):
    if f(x) == ..:
        k += 1
print(k)
'''

'''
divisions:

def f(x):
    return ...


for a in range(.., 100):
    for x in range(.., 10000):
        if f == ..:
            break
    print(a)
    break
'''

'''
conjunctions:

def f(x):
    return ...


for a in range(., 100):
    if all(f(x) == .. for x in range(.., 10000):
        print(a)
    else:
        break
'''