def f(num: int, k: int, m: int) -> None:
    if k < m:
        f(num+1, k+1, m)
        A.append(num)
        f(num*4, k+1, m)
        A.append(num)


A = []
f(7, 0, 6)
print(len(set(A)))


def f(num: int, k: int, m: int) -> None:
    if k == m:
        A.append(num)
    else:
        f(num-5, k+1, m)
        f(-num*2, k+1, m)


A = []
f(216, 0, 7)
print(len([x for x in A if x > 0]))


def f(num: int, k: int, m: int) -> None:
    if k == m:
        A.append(num)
    else:
        f(num+1, k+1, m)
        f(num+2, k+1, m)
        f(num*2, k+1, m)


A = []
f(3, 0, 5)
print(len([x for x in A if x % 2 == 0]))