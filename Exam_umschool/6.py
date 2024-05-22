'''
Повтори 4 [Вперёд 10 Направо 270]
Поднять хвост
Вперёд 3 Направо 270 Вперёд 5 Направо 90
Опустить хвост
Повтори 2 [Вперёд 10 Направо 270 Вперёд 12 Направо 270]
'''

import turtle as t

t.screensize(12000, 12000)
t.tracer(0)
t.lt(90)
m = 40

for _ in range(4):
    t.fd(10*m)
    t.rt(270)
t.pu()
t.fd(3*m)
t.rt(270)
t.fd(5*m)
t.rt(90)
t.pd()
for _ in range(2):
    t.fd(10*m)
    t.rt(270)
    t.fd(12*m)
    t.rt(270)
t.pu()
for x in range(-m, m):
    for y in range(-m, m):
        t.goto(x*m, y*m)
        t.dot()
t.done()