from functools import lru_cache

@lru_cache(None)
def f(n):
    if n < 2:
        return 7
    if n > 1:
        return 7 * f(n-2)

M = [f(x) for x in range(1, 13000)]
print(f(12950) / (7 ** 6473))