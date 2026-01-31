from turtle import *
from colorsys import *
tracer(50)
bgcolor('white')
h = 0
for i in range (3000):
    h+=0.005
    color(hsv_to_rgb(h%1,1,1))
    if i % 5 == 0:
        right(3)
    forward(180)
    right(360/5)
    hideturtle()
done()