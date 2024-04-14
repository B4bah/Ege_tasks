from functools import lru_cache


def mov(n):
    x, y = n
    return (x+1, y), (x+2, y), (x, y+1), (x, y+2)


@lru_cache(None)
def f(n):
    if any(sum(x) == 13 for x in mov(n)): return 1
    if all(f(x) == 1 for x in mov(n)): return -1
    if any(f(x) == -1 for x in mov(n)): return 2
    if all(f(x) > 0 for x in mov(n)): return -2
    else: return 0


for i in range(1, 10):
    if f((3, i)) == 1:
        print(i)
# 8

for i in range(1, 10):
    if f((3, i)) == 2:
        print(i)
# 5 6

for i in range(1, 10):
    if f((3, i)) == -2:
        print(i)
# 4