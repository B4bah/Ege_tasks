def f(s, m):
    if s >= 469: return m % 2 == 0
    if m == 0: return 0
    h = [f(s+5, m-1), f(s*3, m-1)]
    return any(h) if (m-1) % 2 == 0 else all(h)


print(19, [s for s in range(1, 469) if not f(s, 1) and f(s, 2)][0])
print(20, *[s for s in range(1, 469) if not f(s, 1) and f(s, 3)][:2])
print(21, [s for s in range(1, 469) if not f(s, 2) and f(s, 4)][0])