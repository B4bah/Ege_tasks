def f(curr, end, m):
    if curr == end: return 1
    if curr > end or m > 2: return 0
    return f(curr-2, end, m+1) + f(curr*2, end, m) + f(curr*3, end, m)


print(f(6, 48, 0))