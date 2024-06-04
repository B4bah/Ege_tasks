def retransform(n, base):
    product = 0
    for i in range(len(n)):
        digit = len(n)-i-1
        product += n[digit]*base**i
    return product


for x in range(17, -1, -1):
    num = retransform([7, 1, x, 2, 6, 4], 18) + retransform([4, x, 5, 1, x, 1], 18) + retransform([2, 1, x, 6, 3, 7], 18)
    if num % 17 == 0:
        print(num // 17)
        break