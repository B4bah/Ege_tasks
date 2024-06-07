def f(curr, end, forb1=11, forb2=18):
    if curr == end: return 1
    if curr > end or curr == forb1 or curr == forb2: return 0
    return f(curr+1, end) + f(curr+2, end) + f(curr*3, end)


print(f(4, 8) * f(8, 23))