def f(s, m):
    if 36 <= s <= 60: return m % 2 == 0
    if m == 0: return 0
    if s > 60: return (m-1) % 2 == 0
    h = [f(s+1, m-1), f(s*2, m-1), f(s*3, m-1)]
    return any(h) if (m-1) % 2 == 0 else all(h)


print(19, *[s for s in range(1, 35) if f(s, 2)])
print(20, len([s for s in range(1, 35) if not f(s, 1) and f(s, 3)]))
print(21, *[s for s in range(1, 35) if not f(s, 2) and f(s, 4)])