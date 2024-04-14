from functools import lru_cache

@lru_cache(None)
def mov(t: tuple[int, int]) -> tuple[tuple[int, int], tuple[int, int], tuple[int, int], tuple[int, int]]:
    x, y = t
    return (x+10, y), (x, y+10), (x*2, y), (x, y*2)


def f(n):
    if any(107 <= sum(x) <= 170 for x in mov(n)): return 1
    elif all(f(x) == 1 for x in mov(n)): return -1
    elif any(f(x) == -1 for x in mov(n)): return 2
    elif all(f(x) >= 0 for x in mov(n)): return -2
    else: return 0


def f_(n):
    if any(107 <= sum(x) <= 170 for x in mov(n)): return 1
    elif any(f(x) == 1 for x in mov(n)): return -1
    elif all(f_(x) == -1 for x in mov(n)): return 2
    elif any(f_(x) >= 0 for x in mov(n)): return -2
    else: return 0


k = 0
for i in range(1, 100+1):
    if f((5, i)) == -1:
        if k < 2:
            k += 1
            print(i)
        else:
            break


# for i in range(1, 100+1):
#     if f_(5, i) == 2:
#         print(i)
#         break
#
# for i in range(1, 100+1):
#     if f((5, i)) == 2:
#         print(i)
#         break
#
# for i in range(1, 100+1):
#     if f_((5, i)) == -2:
#         print(i)
#         break