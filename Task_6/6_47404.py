import turtle as t

t.screensize(12000, 12000)
t.tracer(0)
t.lt(90)
m = 40

for _ in range(4):
     t.fd(10*m)
     t.rt(90)
t.right(30)
for _ in range(5):
    t.fd(6*m)
    t.rt(60)
    t.fd(6*m)
    t.rt(120)
t.dot('red')
t.pu()
for x in range(-m, m):
    for y in range(-m, m):
        t.goto(x*m, y*m)
        t.dot()
t.done()