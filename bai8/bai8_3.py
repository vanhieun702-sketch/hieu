import turtle

colors = ["red", "blue", "green"]
painter = turtle.Turtle()
painter.pensize(2)
for i in range(12):
    painter.pencolor(colors[i % len(colors)]) 
    painter.circle(100)
    painter.right(30)
    painter.left(60)
    painter.setposition(0, 0)

turtle.done()