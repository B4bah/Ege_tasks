import turtle as t

t.screensize(5000, 5000)
t.tracer(0)
t.lt(90)
m = 50

for _ in range(2):
    t.fd(13 * m)
    t.rt(90)
    t.fd(5 * m)
    t.rt(90)

t.pu()
for x in range(-30, 30):
    for y in range(-30, 30):
        t.goto(x * m, y * m)
        t.dot()
t.done()