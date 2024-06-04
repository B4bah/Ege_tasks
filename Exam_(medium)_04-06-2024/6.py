import turtle as t

t.screensize(10000, 3000)
t.tracer(0)
m = 30

a = 0
b = 0
for _ in range(10):
    t.goto(a + 6 * m, b + 15 * m)
    a += 6 * m; b += 15 * m
    t.goto(a + 4 * m, b - 6 * m)
    a += 4 * m; b += -6 * m
    t.goto(a + 2 * m, b + 2 * m)
    a += 2 * m; b += 2 * m
    t.goto(a + 3 * m, b + 9 * m)
    a += 3 * m; b += 9 * m
    # t.fd(6 * m); t.lt(90); t.fd(15 * m); t.rt(90)
    # t.fd(4 * m); t.lt(90); t.bk(6 * m); t.rt(90)
    # t.fd(2 * m); t.lt(90); t.fd(2 * m); t.rt(90)
    # t.fd(3 * m); t.lt(90); t.bk(9 * m); t.rt(90)
    t.dot(10, 'red')

t.pu()
for x in range(-1, 30):
    for y in range(-10, 30):
        t.goto(x * m, y * m)
        t.dot(4)
t.done()