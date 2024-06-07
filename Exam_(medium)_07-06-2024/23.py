def f(curr, end, forb=58):
    if curr == end: return 1
    if curr > end or curr == forb: return 0
    return f(curr + 1, end) + f(curr + 2, end) + f(curr + 3, end) + f(curr * 4, end)


print(f(38, 45) * f(45, 68))