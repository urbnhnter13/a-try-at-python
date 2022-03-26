from turtle import*



def artdrwr():
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
   


def pntselct(p1,p2,l1,l2,xsps,ysps):
    xstpt=p1
    ystpt=p2
    xlim=l1            #lim should be greater than start point
    ylim=l2
    xspce=xsps
    yspce=ysps
    i=xstpt
    
    

    while(i<xlim):
        j=ystpt-300
        while(j<ylim):
            penup()
        
            goto(i,j)
            pendown()
            artdrwr()
            j=j+(250+yspce)
        i=i+(250+xspce)

#pntselct(0,0,1800,1800,100,100)
def pointsel(k,l,m,n):
    i=k
    
    while i<m :
        if(i%2==0):
            j=l
            n=n
        else:
            j=-100
            n=1000
        while j<n:
            penup()
            q=i*2.5
            r=j*3
            goto(q,r)
            pendown()
            artdrwr()
            j=j+100
        i=i+100
        



def caller():
    pointsel(-1000,0,1000,1000)
    pointsel(-1000,-1000,1000,0)

condi=input(str("Do you want to start?(y/n)"))



if(condi=="y"):
    cov=2000
    setworldcoordinates(-cov,-cov,cov,cov)
    speed(100000000000)
    caller()
else:
    print("why tho, see my program output, please \n whatever :( \n")
    exit()
    
    
    
mainloop()
