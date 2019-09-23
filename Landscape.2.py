import turtle

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



square(turtle, 75)



turtle.exitonclick()