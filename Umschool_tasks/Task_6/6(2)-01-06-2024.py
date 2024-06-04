import turtle as t

t.screensize(5000, 5000)
t.tracer(0)
t.lt(90)
m = 70

for _ in range(3):
    t.fd(10 * m)
    t.rt(240)

t.pu()
for x in range(-30, 30):
    for y in range(-30, 30):
        t.goto(x * m, y * m)
        t.dot(3)
t.done()