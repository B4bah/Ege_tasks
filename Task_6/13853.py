import turtle as t

t.tracer(0)
t.screensize(2000, 2000)
m = 50
t.pu()
for i in range(10):
    t.fd(5*m)
    t.dot(10, 'blue')
    t.rt(90)
    t.fd(3*m)
    t.dot(10, 'blue')
    t.rt(90)
    t.fd(2*m)
    t.dot(10, 'blue')
    t.rt(90)

t.pu()
for x in range(-m, m):
    for y in range(-m, m):
        t.goto(x*m, y*m)
        t.dot(5)
t.done()