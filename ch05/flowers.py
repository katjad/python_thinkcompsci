"""

Code from Chapter 4 
Think Python: An Introduction to Software Design
Allen B. Downey

"""

from TurtleWorld import *
import math

def square(t, length):
    """Use the Turtle (t) to draw a square with sides of
    the given length.  Returns the Turtle to the starting
    position and location.
    """
    for i in range(4):
        fd(t, length)
        lt(t)

def polyline(t, n, length, angle):
    """Draw n line segments with the given length and
    angle (in degrees) between them.
    """
    for i in range(n):
        fd(t, length)
        lt(t, angle)

def polygon(t, n, length):
    angle = 360.0/n
    polyline(t, n, length, angle)

def arc(t, r, angle):
    arc_length = 2 * math.pi * r * abs(angle) / 360
    n = int(arc_length / 4) + 1
    step_length = arc_length / n
    step_angle = float(angle) / n

    # making a slight left turn before the polyline reduces
    # the error caused by the linear approximation of the arc
    lt(t, step_angle/2)
    polyline(t, n, step_length, step_angle)
    rt(t, step_angle/2)

def circle(t, r):
    arc(t, r, 360)




world = TurtleWorld()
bob = Turtle()
bob.delay = 0.01


# n is number of leaves
#r = 1/6 flowerradius * n
#angle = 360/n

def leaf(t,r,angle):
    arc(t,r,angle)
    lt(t,180-angle)
    arc(t,r,angle)

def flower(t,radius,n):
    r = radius/6 * n
    angle = 360/n
    for i in range(n):
        leaf(t,r,angle)
        lt(t,angle+(180-angle))


set_pen_color(bob,'green')
flower(bob,100,3)
lt(bob,60)
set_pen_color(bob,'pink')
flower(bob,100,3)
lt(bob,30)
set_pen_color(bob,'orange')
flower(bob,50,6)

wait_for_user()
