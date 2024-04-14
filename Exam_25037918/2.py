def f(w, x, y, z):
    return (not(y and (x == (not z))) or w) and (not z or y)


A = []
for w in range(2):
    for x in range(2):
        for y in range(2):
            for z in range(2):
                if not f(w, x, y, z):
                    A.append([w, x, y, z])
print('w x y z')
B = [sum(A[i]) for i in range(len(A))]
