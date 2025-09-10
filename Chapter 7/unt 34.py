import turtle

colors = ["red", "yellow", "blue", "green", "orange", "red"]

aiden = turtle.Turtle()
turtle.bgcolor("black")

for n in range(36):
    for i in range(6):
        aiden.color(colors[i])
        aiden.forward(100)
        aiden.left(60)
        aiden.right(10)

aiden.penup()
aiden.color("white")

for i in range(36):
    aiden.forward(220)
    aiden.pendown()
    aiden.circle(5)
    aiden.penup()
    aiden.backward(220)
    aiden.right(10)

aiden.hideturtle()


    
