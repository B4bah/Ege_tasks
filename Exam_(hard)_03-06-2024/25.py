def divs(num):
    d = set()
    for i in range(1, int(num**0.5)+1):
        if num % i == 0:
            d.add(num // i)
            d.add(i)
    return sorted(d)


m = 0
for k in range(1, 100000):
    if len([x for x in divs(750000 + k) if x % 2 == 0]) % 2 == 1:
        m += 1
        if m <= 5:
            print(k, len([x for x in divs(750000 + k) if x % 2 == 0]))
        else:
            break