import turtle
import turtle
import colorsys
n = 70
h = 0
turtle.bgcolor("black")
turtle.color("white")
turtle.speed(100)
turtle.hideturtle()
x = 0
while 1 == 1:
    c = colorsys.hsv_to_rgb(h, 1, 0.8)
    h += 0.1/n
    turtle.color(c)
    turtle.forward(1)
    turtle.left(51)
    x += 1
    turtle.forward(x)
