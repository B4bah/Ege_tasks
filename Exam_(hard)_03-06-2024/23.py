def f(curr, end, m):
    if curr == end: return 1
    if curr > end or m > 3: return 0
    return f(curr+2, end, m) + f(curr*3, end, m+1) + f(curr*5, end, m+1)


print(f(2, 200, 0))