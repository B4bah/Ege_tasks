def retrans(n, base):
    p = 0
    for i in range(len(n)):
        d = len(n) - i - 1
        p += n[d] * base ** i
    return p


for x in [0, 1, 2, 3, 4, 5, 6, 7]:
    num = retrans([2, 5, 6, 7, x, 3], 8) + retrans([1, x, 2, 4], 8)
    if num % 7 == 0:
        print(num // 7)