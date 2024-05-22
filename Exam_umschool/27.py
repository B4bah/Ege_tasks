with open('27.1.A.txt') as f:
    # def trips(guz_fuel: int, volume: int) -> int:
    #     return guz_fuel // volume + int(guz_fuel % volume != 0)


    # def m_sort(item: int) -> int:
    #     return item[1] == 93


    # n, k = map(int, f.readline().split())
    # A = []
    # for s in f.readlines():
    #     dist, fuel = map(int, s.split())
    #     A.append([dist, fuel])
    n = 10
    A = [11, 15, 8, 14, 22, 24, 10, 25, 9, 8]
    total = []

    # for km in range(n):
    #     cost = 0
    #     for let in A:
    #         m_dist = min(abs(km - let*A.index(let)), abs(n - km + let*A.index(let)))
    #         cost += m_dist * let*A.index(let)
    #     total.append(cost)
    # print(min(total))

    for i in range(n):
        cost = 0
        for st in A:
            m_dist = min(abs(i - A.index(st)), abs(n - i + A.index(st)))
            cost += m_dist * st
        total.append([cost, i])
    print(total)