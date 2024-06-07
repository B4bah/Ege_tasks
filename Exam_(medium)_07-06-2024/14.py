def retrans(n, base):
    p = 0
    for i in range(len(n)):
        digit = len(n) - i - 1
        p += n[i] * base ** digit
    return p


for x in range(16):
    num = retrans([1, 1, x, 7, 3], 16) + retrans([9, 4, 6, 6, 2, x, 5, 3, x], 16) + retrans([6, x, 4, 1], 16) + \
        retrans([3, 1, x, 7, 7], 16) + retrans([9, x, 8, 2, x, x, 1, 8, 1], 16)
    if num % 15 == 0:
        print(num // 15)
        break