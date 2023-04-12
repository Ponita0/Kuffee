import turtle

print("initiated")

def gen(wid, hei, name, t):
    t.clear()
    wid = wid + 1
    # requiredHeight = 7
    hei = hei + 1
    angle = 360 / wid
    x = 0
    currentR = 50
    a = 50
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
   
    # turtle.Screen().exitonclick()
