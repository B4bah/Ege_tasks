def f(a, b, m):
    if a + b >= 130: return m % 2 == 0
    if m == 0: return 0
    h = [f(a + 2, b, m - 1), f(a * 5, b, m - 1), f(a, b + 2, m - 1), f(a, b * 5, m - 1)]
    return any(h) if (m-1) % 2 == 0 else all(h)


print(19, [s for s in range(1, 124) if f(5, s, 1)][0])
print(20, [s for s in range(1, 124) if not f(5, s, 1) and f(5, s, 3)][-1])
print(21, [s for s in range(1, 124) if not f(5, s, 2) and f(5, s, 4)][0])