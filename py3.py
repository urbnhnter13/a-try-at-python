from turtle import*

def drawer_2():
    pencolor("black")
    begin_fill()
    fillcolor("red")
    lt(150)
    forward(180)
    circle(-90,180)
    setheading(60)
    circle(-90,180)
    forward(180)
    end_fill()
    setheading(0)
   

def genrtr(p,q):
    
    penup()
    goto(p,q)
    pendown()
    drawer_2()


def spawner(ix,iy):
    n=ix
    m=iy
    while(m<800):
        n=ix
        while(n<800):
            genrtr(n,m)
            n=n+250
        m=m+300


def asker():
    choice=input(str("Shall we start?(y/n)  "))
    if(choice=="y"):
        tchce=int(input("Enter times"))
        creator(tchce)
    else:
        print("WHY......  :( \n Whatever")
        exit()

def creator(times):
    
    ok=-800
    title("Art")
    x=1000
    y=1000
    setworldcoordinates(-x,-y,x,y)

    speed(100000000000000000)
    pensize(1.5)
    while(ok!=-(800-(30*times))):
        spawner(ok,ok)
        ok=ok+30

    choice2=(input(str("Do you want to start again?(y/n)  ")))
    if(choice2=="y"):
        clear()
        asker()
    else:
        print("BYE "*4)
        exit()

    
asker()

mainloop()
