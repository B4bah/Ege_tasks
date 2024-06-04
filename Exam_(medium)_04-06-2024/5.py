def f(n):
    bin_n = f'{n:b}'
    if bin_n.count('1') % 2 == 0:
        bin_n = '11' + bin_n[2:] + '0'
    else:
        bin_n = '10' + bin_n[2:] + '1'
    return int(bin_n, 2)


max_r = 0
for num in range(1, 50):
    max_r = max(max_r, f(num))
print(max_r)