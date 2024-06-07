import turtle as t

t.screensize(10000, 10000)
t.tracer(0)
m = 40

a = 0
b = 0
t.dot(10, 'red')

for _ in range(20):
    t.goto(a + 10 * m, b + 20 * m)
    a += 10 * m; b += 20 * m
    t.goto(a + 5 * m, b - 15 * m)
    a += 5 * m; b += -15 * m
    t.goto(a - 12 * m, b - 9 * m)
    a += -12 * m; b += -9 * m
t.dot(10, 'green')

t.pu()
for x in range(-30, 100):
    for y in range(-80, 10):
        t.setpos(x * m, y * m)
        t.dot(4)
t.mainloop()
print(((a/m)**2 + (b/m)**2)**0.5)