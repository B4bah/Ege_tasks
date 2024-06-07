def transform(n, base):
    d= []
    while n > 0:
        d.append(n % base)
        n //= base
    return d[::-1]


num = 9 ** 11 * 3 ** 20 - 3 ** 9 - 27
print(transform(num, 3).count(2))