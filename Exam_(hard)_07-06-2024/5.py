def f(n):
    bin_n = f'{n:b}'
    if n % 2 == 0:
        bin_n += f"{(bin_n.count('1')):b}"
    else:
        bin_n = '1' + bin_n + '00'
    return int(bin_n, 2)


max_n = 0
for num in range(1, 1000):
    if f(num) < 1000:
        max_n = max(max_n, num)
print(max_n)