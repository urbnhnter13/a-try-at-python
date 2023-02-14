import turtle

l=turtle.Turtle()
dt=turtle.Turtle()

cv=1500
turtle.setworldcoordinates(-cv,-cv,cv,cv)
l.speed(0)

def drawer():
    
    l.pencolor("black")
    l.begin_fill()
    l.fillcolor("red")
    l.lt(150)
    l.forward(180)
    l.circle(-90,180)
    l.setheading(60)
    l.circle(-90,180)
    l.forward(180)
    l.end_fill()
    
dt.setheading(-120)
dt.penup()
for i in range(10):
    drawer()
    dt.circle(-600,30)
    tpos=dt.pos()
    l.penup()
    l.goto(tpos)
    
    l.pendown()
    l.setheading(0)
    
turtle.mainloop()
