import turtle
import math

def draw_sunbeams(t, num_beams):
    """
    This function makes turtle t draw num_beams beams for a sun.
    Given beam length is 20 pixels long (120 - 140 pixels from the origin)
    """
    angle = 360 / num_beams
    beam_length = 20

    for _ in range(num_beams):
        t.forward(120)  # Move to the outer circle
        t.pendown()
        t.forward(beam_length)
        t.penup()
        t.backward(140)  # Move back to the center
        t.right(angle)

window = turtle.Screen()
pen = turtle.Turtle()
pen.speed(1)

radius = 100

# Draw a sun
pen.up()
pen.goto(0, -radius)
pen.down()
pen.circle(radius)
pen.up()
pen.goto(0, 0)

# Draw sun beams
draw_sunbeams(pen, 12)

pen.shape('blank')

window.exitonclick()

