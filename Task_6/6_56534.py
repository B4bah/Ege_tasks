import turtle as t

t.tracer(0)
t.lt(90)
m = 50

t.dot(10, 'red')
for _ in range(3):
    t.fd(7 * m)
    t.rt(90)
t.fd(8 * m)
for _ in range(3):
    t.lt(90)
    t.fd(5 * m)

t.pu()
for x in range(-m, m):
    for y in range(-m, m):
        t.goto(x * m, y * m)
        t.dot(5)
t.done()