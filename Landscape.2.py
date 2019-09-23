import turtle

turtle.speed(2000)

bob = turtle.Turtle()
billy = turtle.Turtle()

bob.fillcolor("green")

bob.begin_fill()
bob.forward(600)
bob.backward(1200)
bob.right(90)
bob.forward(400)
bob.left(90)
bob.forward(1200)
bob.left(90)
bob.forward(400)
bob.end_fill()
bob.penup()
bob.goto(0, 0)

billy.penup()
billy.backward(200)
billy.pendown()
billy.right(180)

def square(turtle, side):
    for i in range(4):
        billy.forward(100)
        billy.right(90)

billy.fillcolor("firebrick")
billy.begin_fill()
square(turtle, 75)
billy.end_fill()

billy.fillcolor("dark slate grey")
billy.penup()
billy.right(90)
billy.forward(100)
billy.right(90)
billy.pendown()
billy.begin_fill()
billy.forward(25)
billy.backward(145)
billy.left(60)
billy.forward(145)
billy.right(120)
billy.forward(145)
billy.end_fill()
billy.penup()


bob.penup()
bob.left(90)
bob.forward(250)


turtle.exitonclick()