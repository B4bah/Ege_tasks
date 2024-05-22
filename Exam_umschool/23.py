def f(curr, end):
    if curr == end: return 1
    if curr > end: return 0
    return f(curr + 5, end) + f(curr * 2, end)


print(f(1, 12) * f(12, 24))