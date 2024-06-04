import turtle as t

t.screensize(3500, 3500)
t.tracer(0)
t.lt(90)
m = 30

t.dot(10, 'red')
for _ in range(2):
    t.fd(23 * m)
    t.lt(90)
    t.bk(27 * m)
    t.lt(90)
t.pu()
t.bk(5 * m)
t.rt(90)
t.fd(11 * m)
t.lt(90)
t.dot(10, 'green')
t.pd()

for i in range(2):
    t.fd(26 * m)
    t.rt(90)
    t.fd(32 * m)
    t.rt(90)

t.pu()
for x in range(-1, 45):
    for y in range(-6, 25):
        t.goto(x * m, y * m)
        t.dot()

t.done()