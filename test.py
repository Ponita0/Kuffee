import multiprocessing
import time
import turtle

def circWithLines(widd, heii, name):

    def draw_turtle():
        t = turtle.Turtle(visible=False)
        t.speed(0)
        wid = widd + 1
        # requiredHeight = 7
        hei = heii + 1
        angle = 360 / wid
        x = 0
        currentR = 50
        a = 50
        try:
            for x in range(hei):
                t.penup()
                t.goto(0, 0)
                t.right(90)
                t.forward(currentR)
                t.left(90)
                t.pendown()
                t.circle(currentR, steps=2000)
                currentR = currentR + 20

            i = 0
            for i in range(wid + 1):
                t.penup()
                t.goto(0, 0)
                t.pendown()
                t.forward(currentR)
                t.penup()
                t.goto(0, 0)
                t.right(angle)
            ts = turtle.getscreen()

            ts.getcanvas().postscript(file="static/files/[Ibrahim Abdelmonem] %s.eps" % name)
        except turtle.Terminator:
            pass
    
    # Close the turtle window explicitly
        turtle.bye()   

    # Create a separate process for the turtle code
    p = multiprocessing.Process(target=draw_turtle)
    p.start()
    p.join()
   
    return "Generated turtle image"

f=0
def circularGrid(number,ratioA,ratioB,name,n):
    f=n 
    
    def DrawCirccc():
        n=f
        turtle.setup(width=850, height=850)
        t = turtle.Turtle(visible=True)
        try :
            if n%2 == 0 :
                n=n-1
            n=int((n+1)/2)
            print(n)
            t.speed(0) # 1:slowest, 3:slow, 5:normal, 10:fast, 0:fastest

            width = turtle.window_width() -50
            height = turtle.window_height() -50

            print(width , " : " , height)

            ratioTotal = ratioA+ratioB
            totalParts = (ratioA+ratioB)*n
            print("total parts: ",totalParts)
            x =  height/(totalParts)
            print("x: ",x)
            # max height = 3 * X * n 
            # height = 3 * x * n

            t.penup()
            t.goto(width/2 ,height/2)
            t.rt(90)


            #draw the main frame
            for i in range(4):
                t.pendown()
                t.fd(height)   
                t.right(90)    

            t.pendown()
            t.fd(ratioB*x)
            t.right(90)
            t.goto(0+height/2,0+height/2)

            #draw the horizontal lines
            for i in range(n):
                t.forward(width)
                t.left(90)
                t.pendown()
            #  t.penup()
                t.fd(x*ratioB)
                t.left(90)
                t.forward(width)
            # t.penup()
                t.right(90)
                t.forward(x*ratioA)
                t.right(90)
                

            #draw vertical lines
            t.goto(0+height/2,0-height/2)
            t.right(90)
            for i in range(n):    
                t.forward(height)
                t.left(90)
                t.forward(x*ratioA)
                t.left(90)          
                t.forward(width)   
                t.right(90)
                t.forward(ratioB*x)
                t.right(90)




            def drawCirc(r):           
                t.pu()
                t.setheading(0)                         
                t.pendown()
                t.circle(r,steps=2000)        

            t.pu()
            # t.goto(0+height/2,0-height/2)
            # t.setheading(270)
            # t.forward(x*ratioB)
            # t.setheading(0)
            # t.forward(x*ratioA)

            if n %2 !=0:
                n=n+1
            t.goto(0+height/2,0-height/2)
            t.setheading(90)
            t.forward(x*(ratioTotal*n/2))
            t.setheading(180)
            t.forward(x*(ratioTotal*n/2))
            t.setheading(270)
            t.forward(x*ratioB)
            t.setheading(0)
            t.forward(x*0.5*ratioB)

            counter =1
            for i in range(number):
                drawCirc((x*0.5*ratioB)*counter)
                t.setheading(270)
                t.pu()
                t.forward(x*ratioA)
                t.pd()
                drawCirc((x*ratioB*0.5*counter)+x*ratioA)
                t.setheading(270)
                t.pu()
                t.forward(x*ratioB)
                t.pd()

                counter=counter+3
            ts = turtle.getscreen()

            ts.getcanvas().postscript(file="static/files/[Ibrahim Abdelmonem] %s.eps" % name)

        except turtle.Terminator:
                pass
    # Close the turtle window explicitly
        turtle.bye()   

        # Create a separate process for the turtle code
    p = multiprocessing.Process(target=DrawCirccc)
    p.start()
    p.join()
    return "Generated turtle image"
z=0
def circWithRect(nCircles,nRects,rectWidth,rectHeight,name):
    z=nRects
    def mainF():      
        nRects=z
        r = 10
        turtle.setup(width=850, height=850)
        t = turtle.Turtle(visible=True)
        t.speed(5)
        t.penup()
        t.goto(0,0)    
        t.setheading(270)
        t.fd(r)
        t.setheading(0)
        
        def drawCirc(r,fromCenter):              
                if fromCenter == True:
                    t.setheading(270)
                    t.pu()
                    t.fd(r)
                    t.pd()
                    t.setheading(0)

                t.pu()
                t.setheading(0)                         
                t.pendown()
                t.circle(r,steps=100)
                # draw axis

        def drawRect(width,height,fromCenter):
            print(width," : " , height)
            if fromCenter == True:
                t.rt(90)
                t.pu()
                t.fd(height/2)
                t.pd()
                t.lt(90)
            t.forward(width/2)
            t.lt(90)
            t.fd(height)
            t.lt(90)
            t.fd(width)
            t.lt(90)
            t.fd(height)
            t.lt(90)
            t.fd(width/2)    

        t.speed(0)
        t.pu()
        t.goto(0,0)       
        t.speed(10)
        u = 20
        if nRects%2 !=0:
            nRects=nRects+1
        t.pu()

        angle = 360/nRects

        for i in range(int(0.5*(nRects))):
            t.pu()
            t.goto(0,0)
            t.pd()
            drawRect(rectWidth,rectHeight,True)
            t.rt(360/nRects)
        

        # start drawing circles 
        t.speed(0)
        t.pu()
        t.goto(0,0)
        t.setheading(270)    
        t.fd(r+10)    
        t.pd()
        counter =1
        x=r    
        t.pu()
        t.goto(0,0)        
        t.setheading(270)
        t.pu()
        t.fd(rectHeight)
        t.pd()
        for i in range(nCircles):
                    drawCirc(rectHeight*(counter),False)   
                    t.setheading(270)            
                    t.pu()
                    t.fd(rectHeight)
                    t.pd()          
                    drawCirc(rectHeight*(counter)+rectHeight,False)      
                    t.setheading(270)
                    t.pu()
                    t.fd(rectHeight*2)
                    t.pd()   
                    counter=counter+3 

        ts = turtle.getscreen()

        ts.getcanvas().postscript(file="static/files/[Ibrahim Abdelmonem] %s.eps" % name)   

    p = multiprocessing.Process(target=mainF)
    p.start()
    p.join()
    return "Generated turtle image"



#circWithRect(10,8,700,20)
#circularGrid(7,1,2,"s",50)
#circWithLines(44,7,"sff")
    # turtle.exitonclick()

