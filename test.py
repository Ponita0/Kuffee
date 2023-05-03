import multiprocessing
import os
import time
import turtle

def circWithLines(widd, heii, name,fileType = 'eps'):

    def draw_turtle():
        t = turtle.Turtle(visible=False)
        t.pensize(0.1)
        t.color("gray")
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
            ts = t.getscreen()

            ts.getcanvas().postscript(file="static/files/[Kuffee]%s.eps")
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
def circularGrid(number,ratioA,ratioB,name,n,fileType = 'eps'):
    f=n 
    number=number+1
    def DrawCirccc():
        n=f
        turtle.setup(width=890, height=890)
        t = turtle.Turtle(visible=True)
        t.pensize(0.1)
        t.color("gray")

        try :
            if n%2 == 0 :
                n=n-1
            n=int((n+1)/2)
            t.speed(0) # 1:slowest, 3:slow, 5:normal, 10:fast, 0:fastest

            width = turtle.window_width() -50
            height = turtle.window_height() -50

            ratioTotal = ratioA+ratioB
            totalParts = (ratioA+ratioB)*n
            x =  height/(totalParts) 
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
        except turtle.Terminator:
                pass
    # Close the turtle window explicitly
        #turtle.bye()   
        ts = t.getscreen()
        canvas = ts.getcanvas()
        canvas.postscript(file="static/files/[Kuffee]%s.eps" % name)

        # Create a separate process for the turtle code
    p = multiprocessing.Process(target=DrawCirccc)
    p.start()
    p.join()
    return "Generated turtle image"
z=0
def circWithRect(nCircles,nRects,rectWidth,name,fileType = 'eps'):
    z=nRects
    def mainF():      
        nRects=z
        r = 300
        turtle.setup(width=890, height=890)
        t = turtle.Turtle(visible=False)
        t.pensize(0.1)
        t.color("gray")

        t.speed(0)
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
                t.circle(r,steps=1000)
                # draw axis              


        def drawRect(width,height,fromCenter):
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

        

        # start drawing circles 
        maxR =rectWidth/2
        t.speed(0)
        t.pu()
        t.goto(0,0)
        t.setheading(270)    
        # t.fd(maxR+10)    
        t.pd()
        counter =1
        x=r    
        t.pu()
        t.goto(0,0)        
        t.setheading(270)
        t.pu()
        t.goto(0,0)
        t.setheading(270)
        t.fd(maxR)
        t.pd()
        # for i in range(nCircles):
        #             drawCirc(rectHeight*(counter),False)   
        #             t.setheading(270)            
        #             t.pu()
        #             t.fd(rectHeight)
        #             t.pd()          
        #             drawCirc(rectHeight*(counter)+rectHeight,False)      
        #             t.setheading(270)
        #             t.pu()
        #             t.fd(rectHeight*2)
        #             t.pd()   
        #             counter=counter+3 
        t.pu()
        t.goto(0,0)        
        drawCirc(50,True)
        t.pu()
        t.goto(0,0)
        t.setheading(270)
        t.fd(maxR)
        t.pd()

        currentR = maxR
        x = (maxR-50)/nCircles
        x = ((maxR-50))/ (3*nCircles)

        # 3x * n = (maxR-50)/nCircles

        for i in range(nCircles):
            drawCirc(currentR*(counter),False)
            currentR=currentR-x
            t.pu()
            t.setheading(90)            
            t.fd(x)
            t.setheading(0)
            drawCirc(currentR*(counter),False)
            t.pu()
            t.setheading(90)
            t.fd(x*2)
            t.pu()
            currentR=currentR-x*2


        t.pu()
        t.goto(0,0)       
        u = 20
        if nRects%2 !=0:
            nRects=nRects+1
        t.pu()

        angle = 360/nRects

        for i in range(int(0.5*(nRects))):
            t.pu()
            t.goto(0,0)
            t.pd()
            drawRect(rectWidth,x,True)
            t.rt(360/nRects)
        # Set pen position to the edge of the drawing area      

        # Hide the turtle from view

        ts = t.getscreen()
        canvas = ts.getcanvas()
        canvas.postscript(file="static/files/[Kuffee]%s.eps" % name)
                

        

    p = multiprocessing.Process(target=mainF)
    p.start()
    p.join()
    
    return "Generated turtle image"

def regularGrid(ratioA,ratioB,Nwidth,Nheight,name,fileType = 'eps'):
    if Nheight>Nwidth:
        temp = Nheight
        Nheight= Nwidth
        Nwidth=temp
    def DrawCirccc():
        turtle.setup(width=890, height=890)
        t = turtle.Turtle(visible=True)
        t.pensize(0.1)
        t.color("gray")
        try :            
            t.speed(0) # 1:slowest, 3:slow, 5:normal, 10:fast, 0:fastest
            width = turtle.window_width() -50
            height = turtle.window_height() -50
            ratioTotal = ratioA+ratioB # 2
            totalParts = (ratioTotal)*Nwidth
            x =  width*2/(totalParts) 
            t.pu()
            t.goto(width/2,height/2)
            t.setheading(180)
            t.pd()
            t.fd(Nwidth*x)
            t.left(90)
            t.fd(Nheight*x)
            t.lt(90)
            t.fd(Nwidth*x)
            t.lt(90)
            t.fd(Nheight*x)
            t.setheading(180)

            for i in range(int(Nwidth/2)):
                t.fd(x)                
                t.lt(90)
                t.fd(x*Nheight)
                t.rt(90)
                t.fd(x)
                t.rt(90)
                t.fd(x*Nheight)
                t.lt(90)

            t.pu()
            t.goto(width/2,height/2)
            t.setheading(270)
            t.pd()

            for i in range(int( Nheight/2)):
                t.fd(x)
                t.rt(90)
                t.fd(x*Nwidth)
                t.lt(90)
                t.fd(x)
                t.left(90)
                t.fd(x*Nwidth)
                t.rt(90)                   
        except turtle.Terminator:
                pass
    # Close the turtle window explicitly
        #turtle.bye()   
        ts = t.getscreen()
        canvas = ts.getcanvas()
        canvas.postscript(file="static/files/[Kuffee]%s.eps" % name)

        # Create a separate process for the turtle code
    p = multiprocessing.Process(target=DrawCirccc)
    p.start()
    p.join()
    return "Generated turtle image"

def irregularGrid(ratioA,ratioB,name,n,fileType = 'eps'):
    f=n 
    def DrawCirccc():
        n=f
        turtle.setup(width=890, height=890)
        t = turtle.Turtle(visible=False)
        t.pensize(0.1)
        t.color("gray")

        try :
            if n%2 == 0 :
                n=n-1
            n=int((n+1)/2)
            t.speed(0) # 1:slowest, 3:slow, 5:normal, 10:fast, 0:fastest

            width = turtle.window_width() -50
            height = turtle.window_height() -50

            ratioTotal = ratioA+ratioB
            totalParts = (ratioA+ratioB)*n
            x =  height/(totalParts) 
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
            t.pu()       

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
            
        except turtle.Terminator:
                pass
    # Close the turtle window explicitly
        #turtle.bye()   
        ts = t.getscreen()
        canvas = ts.getcanvas()
        canvas.postscript(file="static/files/[Kuffee]%s.eps" % name)

        # Create a separate process for the turtle code
    p = multiprocessing.Process(target=DrawCirccc)
    p.start()
    p.join()
    return "Generated turtle image"


def EpsToPdf(name):
    os.system(f'epstopdf static/files/{name} static/files/{name.replace(".eps",".pdf")}')

