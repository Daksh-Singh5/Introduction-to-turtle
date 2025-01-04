import turtle
turtle.Screen().bgcolor("cyan")
turtle.Screen().setup(500,700)

pen = turtle.Turtle()
pen.penup()
pen.goto(0,200)
pen.pendown()
for i in range(360):
    pen.forward(5)
    pen.right(1)
turtle.done()