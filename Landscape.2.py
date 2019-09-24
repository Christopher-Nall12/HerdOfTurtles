import turtle

turtle.speed(2000)

bob = turtle.Turtle()
billy = turtle.Turtle()

bob.fillcolor("green")

bob.begin_fill()
bob.forward(900)
bob.backward(1800)
bob.right(90)
bob.forward(800)
bob.left(90)
bob.forward(1800)
bob.left(90)
bob.forward(800)
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
bob.forward(245)
bob.right(90)
bob.pendown()
bob.forward(50)
bob.left(90)
bob.forward(25)
bob.left(90)
bob.forward(50)
bob.penup()


billy.goto(0, 0)
billy.penup()
billy.fillcolor("saddle brown")
billy.begin_fill()
billy.right(120)
billy.right(90)
billy.pendown()
billy.forward(300)
billy.right(90)
billy.forward(50)
billy.right(90)
billy.forward(300)
billy.right(90)
billy.forward(50)
billy.end_fill()
billy.penup()
billy.goto(25, 275)
billy.fillcolor("lime green")
billy.begin_fill()
billy.right(180)
billy.circle(250)
billy.end_fill()





turtle.exitonclick()