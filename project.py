import turtle
turtle.Screen().bgcolor("cyan")
turtle.Screen().setup(500,700)


Pen = turtle.Turtle()
Pen.speed(0)
for i in range(19):
    for i in range(360):
        Pen.forward(1)
        Pen.right(1)
    Pen.left(20)
turtle.done()