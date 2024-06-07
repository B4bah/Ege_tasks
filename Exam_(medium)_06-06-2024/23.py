def f(curr, end):
    if curr == end: return 1
    if curr < end: return 0
    return f(curr - 3, end) + f(curr // 2, end)


print(f(108, 42) * f(42, 12))