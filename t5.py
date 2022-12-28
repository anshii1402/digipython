from turtle import*
import random
speed('fast')
s= Screen()
s.setup(500,500)
colors=['pink','orange']
for i in range(50):
    x = random.randint(-200,200)
    y = random.randint(-200,200)
penup()
goto(x,y)
pendown()
# write(f'{x},{y}')
# pensize(random.randint(1,2))
pencolor(colors[random.randint(0,1)])
radius= random.randint(5,30)
fillcolor('red')
begin_fill()
for i in range(6):
    circle (radius)
    left(60)
    end_fill()
mainloop()
