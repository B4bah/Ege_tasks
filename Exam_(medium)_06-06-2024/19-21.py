def f(a, b, m):
    if a + b >= 231: return m % 2 == 0
    if m == 0: return 0
    h = [f(a+2, b, m-1), f(a*2, b, m-1), f(a, b+2, m-1), f(a, b*2, m-1)]
    return any(h) if (m-1) % 2 == 0 else all(h)


def f_(a, b, m):
    if a + b >= 231: return m % 2 == 0
    if m == 0: return 0
    h = [f(a+2, b, m-1), f(a*2, b, m-1), f(a, b+2, m-1), f(a, b*2, m-1)]
    return any(h) if (m-1) % 2 == 0 else any(h)


print(19, [b for b in range(1, 214) if f_(17, b, 2)][-1])
print(20, [b for b in range(1, 214) if not f(17, b, 1) and f(17, b, 3)][0], [b for b in range(1, 214) if not f(17, b, 1) and f(17, b, 3)][-1])
print(21, [b for b in range(1, 214) if not f(17, b, 2) and f(17, b, 4)][0])