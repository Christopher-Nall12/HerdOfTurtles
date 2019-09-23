import turtle

turtle.speed

bob = turtle.Turtle()
bill = turtle.Turtle()
carl = turtle.Turtle()
dave = turtle.Turtle()
bill.shape("turtle")
bob.shape("turtle")

bob.pensize(4)
bob.penup()
bob.right(90)
bob.forward(100)
bob.right(270)
bob.pendown()

bob.fillcolor("yellow")

bob.begin_fill()
bob.circle(200)
bob.end_fill()

bill.fillcolor("white")

bill.penup()
bill.goto(50, 150)
bill.forward(20)
bill.right(90)
bill.pendown()
bill.begin_fill()
bill.circle(55)
bill.end_fill()

bill.penup()
bill.goto(-150, 150)
bill.pendown()
bill.begin_fill()
bill.circle(55)
bill.end_fill()

carl.penup()
carl.backward(10)
carl.pensize(2)
carl.pendown()
carl.forward(40)

dave.penup()
dave.fillcolor("black")
dave.goto(-150, 150)
dave.forward(30)
dave.right(90)
dave.forward(10)
dave.pendown()
dave.begin_fill()
dave.circle(20)
dave.end_fill()
dave.penup()
dave.goto(50, 150)
dave.right(90)
dave.backward(55)
dave.left(90)
dave.forward(10)
dave.pendown()
dave.begin_fill()
dave.circle(20)
dave.end_fill()

def triangle(carl, size):
    for i in range(3):
        carl.forward(20)
        carl.left(135)
        carl.forward(28)

carl.fillcolor("blue")


carl.penup()
carl.goto(-100, 50)
carl.color("blue")
carl.pendown()
carl.right(20)

carl.begin_fill()
triangle(carl, 20)
carl.end_fill()

bill.penup()
bob.penup()
carl.penup()
dave.penup()
bill.forward(300)
dave.forward(300)
carl.forward(400)
bob.forward(300)

dave.goto(-150, 150)
dave.backward(50)
dave.left(115)
dave.pensize(2)
dave.pendown()
dave.forward(100)
dave.penup()
dave.right(20)
dave.forward(120)
dave.pendown()
dave.right(30)
dave.forward(100)




turtle.exitonclick()