import turtle

l=turtle.Turtle()

cv=1500
turtle.setworldcoordinates(-cv,-cv,cv,cv)


def drawer():
    
    l.pencolor("black")
    l.pendown()
    l.pensize(2)
    l.begin_fill()
    
    
    l.fillcolor("red")
    l.lt(150)
    
    l.forward(180)
    l.circle(-90,180)
    l.setheading(60)
    l.circle(-90,180)
    l.forward(180)
    l.end_fill()
    l.pensize(2)
    l.setheading(0)
    

def spawner():
    x=75
    l.penup()
    l.goto(2.5*x,7.5*x)
    l.pendown()
    drawer()
    
    l.penup()
    l.goto(0*x,10*x)
    drawer()
    l.penup()
    l.goto(-2.5*x,7.5*x)
    drawer()
    l.penup()
    l.goto(-5*x,5*x)
    drawer()
    l.penup()
    l.goto(-2.5*x,2.5*x)
    drawer()
    l.penup()
    l.goto(0*x,0*x)
    drawer()
    l.penup()
    l.goto(2.5*x,-2.5*x)
    drawer()
    l.penup()
    l.goto(5*x,-5*x)
    drawer()
    l.penup()
    l.goto(2.5*x,-7.5*x)
    drawer()
    l.penup()
    l.goto(0*x,-10*x)
    drawer()
    l.penup()
    l.goto(-2.5*x,-7.5*x)
    drawer()

spawner()

