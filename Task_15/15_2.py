def f15(x, y, a):
    return y + 3 * x == 60 and 2 * x <= a and y <= a


A = []
for x in range(100):
    for y in range(x+1):
        for a in range(100):
            result = f15(x, y, a)
            if result:
                A.append(a)
print(max(A))