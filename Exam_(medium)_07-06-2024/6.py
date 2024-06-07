import turtle as t

t.screensize(3000, 3000)
t.tracer(0)
t.lt(90)
m = 30

for _ in range(2):
    t.fd(10 * m)
    t.rt(90)
    t.fd(18 * m)
    t.rt(90)
t.pu()
t.bk(6 * m)
t.rt(90)
t.fd(9 * m)
t.lt(90)
t.pd()
for _ in range(2):
    t.fd(17 * m)
    t.rt(90)
    t.fd(5 * m)
    t.rt(90)

t.pu()
for x in range(-30, 30):
    for y in range(-30, 30):
        t.setpos(x * m, y * m)
        t.dot()
t.mainloop()