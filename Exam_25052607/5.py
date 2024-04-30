def f(n):
    n_b = f'{n:b}'
    if n_b.count('1') % 2 == 0:
        n_b = '10' + n_b[:-2] + '00'
    else:
        n_b = '11' + n_b[:-2] + '11'
    return int(n_b, 2)


M = set()
for n in range(100, 201):
    if f(n) % 3 == 0:
        M.add(f(n))
print(sum(M))