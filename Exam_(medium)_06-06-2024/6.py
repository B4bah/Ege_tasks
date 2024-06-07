import turtle as t

t.screensize(3000, 3000)
t.tracer(0)
# t.lt(90)
m = 50

a = 0
b = 0
for _ in range(1):
    t.goto(a + 5 * m, b + 4 * m)
    a += 5 * m; b += 4 * m
    t.goto(a + 4 * m, b - 4 * m)
    a += 4 * m; b += -4 * m
    t.goto(a - 7 * m, b - 2 * m)
    a += -7 * m; b += -2 * m
    t.goto(a - 2 * m, b + 2 * m)
    a += -2 * m; b += 2 * m


t.pu()
for x in range(-30, 30):
    for y in range(-30, 30):
        t.goto(x * m, y * m)
        t.dot()
t.mainloop()