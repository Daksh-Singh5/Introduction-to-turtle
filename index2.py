import turtle
turtle.Screen().bgcolor("cyan")
turtle.Screen().setup(500,700)
inf = turtle.Turtle()
wid = 0
while True:
    for i in range(4):
        inf.forward(wid+1)
        inf.right(90)
        wid-=5
    wid+=1






turtle.done()