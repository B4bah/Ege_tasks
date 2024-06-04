import turtle as t

t.screensize(3000, 3000)
t.tracer(0)
t.lt(90)
m = 30

for _ in range(7):
    t.fd(20 * m)
    t.rt(90)
    t.fd(30 * m)
    t.rt(90)
t.dot(10, 'red')
t.pu()
t.fd(5 * m)
t.rt(90)
t.fd(10 * m)
t.rt(90)
t.pd()
t.dot(10, 'green')
for _ in range(3):
    t.fd(25 * m)
    t.rt(90)
    t.fd(15 * m)
    t.rt(90)

t.pu()
for x in range(-2, 40):
    for y in range(-1, 50):
        t.goto(x * m, y * m)
        t.dot()
t.done()