def transform(n, base):
    d = []
    while n > 0:
        d.append(n % base)
        n //= base
    return d[::-1]


def retransform(num: list[int], base: int) -> int:
    product = 0
    for i in range(len(num)):
        digit = len(num)-i-1
        product += num[digit]*base**i
    #     print(f'product_{digit} = {num[digit]}*{base}**{i} = {num[digit]*base**i}')
    # print(f'product = {product}\n')
    return product


for x in range(10):
    num = retransform([3, x, 1, 5, x], 15) + retransform([1, 2, 3], 3051 + 100*x) + x**x + retransform([1, x, 3], 103 + 10*x) + retransform([1, x, 2], x+1)
    if num % 13 == 0:
        print(transform(num, 13))