import turtle as t

t.screensize(3000, 3000)
t.tracer(0)
t.lt(90)
m = 50

for _ in range(7):
    t.fd(10 * m)
    t.rt(120)

t.pu()
for x in range(-30, 30):
    for y in range(-30, 30):
        t.goto(x * m, y * m)
        t.dot(3)
t.mainloop()