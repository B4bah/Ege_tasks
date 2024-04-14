# A = {2: 1, 9: 15, 16: 20, 25: 2, 32: 22, 40: 6}
# n = len(A)
# k = max(A.keys())
# vol = 3

with open('27A_15342.txt') as f:
    def trips(distance: int, volume: int) -> int:
        return distance // volume + int(distance % volume != 0)


    n, k = map(int, f.readline().split())
    A = dict()
    for s in f.readlines():
        dist, fuel = map(int, s.split())
        A[dist] = fuel
    vol = 11
    total = []
    for i in range(k):
        cost = 0
        if i == 32:
            for a in A.keys():
                cost += min(abs(i - a), abs(k - i + a)) * trips(A[a], vol)
            #     print(f'{min(abs(i - a), abs(k - i + a))} * {trips(A[a], vol)} = {cost}')
            # print(cost)
            total.append(cost)
    print(min(total))