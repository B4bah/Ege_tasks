def f15(x, y, a):
    return x < 7 and 2*x >= y and x * y >= a


A = []
for x in range(7):
    for y in range(x+1):
        for a in range(100):
            result = f15(x, y, a)
            if result:
                A.append(a)
print(max(A) + 1)
