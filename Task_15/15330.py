from itertools import combinations


def f(x):
    A = st <= x <= end
    P = 35 <= x <= 55
    Q = 45 <= x <= 65
    return (P <= A) and ((not A) <= (not Q))


K = [k * 0.25 for k in range(1, 120*4)]
M = []
for st, end in combinations(K, 2):
    if all(f(x) == 1 for x in K):
        M += [end-st]
print(round(min(M)))
