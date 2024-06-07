# A = {2: 1, 9: 5, 16: 20, 25: 2, 32: 22, 40: 6}
# n = len(A)
# k = max(A.keys())
# vol = 3
from typing import Dict, Any

with open('27B_15342.txt') as f:
    def trips(guz_fuel: int, volume: int) -> int:
        return guz_fuel // volume + int(guz_fuel % volume != 0)


    n, k = map(int, f.readline().split())
    A = sorted([[int(y) for y in x.split()] for x in f.readlines()])
    # A = []
    # for s in f.readlines():
    #     dist, fuel = map(int, s.split())
    #     A.append([dist, fuel])
    # B = [item[0] for item in list(filter(m_sort, A))]
    vol = 11

    total = []

    for st in A:
        cost = 0
        for guz in A:
            m_dist = min(abs(st[0] - guz[0]), abs(k - st[0] + guz[0]))
            cost += m_dist * trips(guz[1], vol)
        total.append(cost)
    print(min(total))


    # for km in A.keys():
    #     cost = 0
    #     if km <= 1000:
    #         for guz in A.keys():
    #             cost += min(abs(km - guz), abs(k - km + guz)) * trips(A[guz], vol)
    #         #     print(f'{min(abs(i - a), abs(k - i + a))} * {trips(A[a], vol)} = {cost}')
    #         # print(cost)
    #         total.append(cost)
    #
    # print(total)
