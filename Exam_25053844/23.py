def f(curr, end, forbid=16):
    if curr == end: return 1
    if curr > end or curr == forbid: return 0
    return f(curr+1, end) + f(curr+2, end) + f(curr*3, end)


print(f(2, 9)*f(9, 18))