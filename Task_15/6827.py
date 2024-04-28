from itertools import combinations


def f(x):
    A = st <= x <= end
    B = 23 <= x <= 37
    C = 41 <= x <= 73
    return not (((not B) <= C) <= A)


K = [k*0.25 for k in range(22*4, 74*4)]
M = []

for st, end in combinations(K, 2):
    if all(f(x) == 0 for x in K):
        M += [end-st]
print(round(min(M)))