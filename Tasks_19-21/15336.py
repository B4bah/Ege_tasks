def f(a, b, m):
    if a + b >= 123: return m % 2 == 0
    if m == 0: return 0
    h = [f(a+1, b, m-1), f(a*2, b, m-1), f(a, b+1, m-1), f(a, b*2, m-1)]
    return any(h) if (m-1) % 2 == 0 else all(h)


def f_(a, b, m):
    if a + b >= 123: return m % 2 == 0
    if m == 0: return 0
    h = [f(a+1, b, m-1), f(a*2, b, m-1), f(a, b+1, m-1), f(a, b*2, m-1)]
    return any(h) if (m-1) % 2 == 0 else any(h)


print(19, [s for s in range(1, 110) if f_(13, s, 2)][0])
print(20, *[s for s in range(1, 110) if not f(13, s, 1) and f(13, s, 3)][:2])
print(21, [s for s in range(1, 110) if not f(13, s, 2) and f(13, s, 4)][0])