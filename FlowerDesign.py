from turtle import*
from colorsys import*
bgcolor("black")
tracer(1000)
def draw():
    h = 0
    up()
    goto(0,0)
    down()
    for i in range(100):
        color(hsv_to_rgb(h, 1, 1))
        h +=0.013
        forward(20)
        circle(i,5,3)
        for j in range(i):
            forward(25)
            right(36)
            backward(9)
            circle(j,5,3)
            right(90.2)
draw()
for i in range(8):
    draw()
done()    
                  