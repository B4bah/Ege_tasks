from itertools import combinations


def f(x):
    A = st <= x <= end
    P = 6 <= x <= 17
    Q = 13 <= x <= 28
    return (A <= P) or Q


K = [k * 0.25 for k in range(5*4, 29*4)]
M = []
for st, end in combinations(K, 2):
    if all(f(x) == 1 for x in K):
        M += [end-st]
print(round(max(M)))