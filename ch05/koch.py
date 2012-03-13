from TurtleWorld import *

world = TurtleWorld()
bob = Turtle()
bob.delay = 0.001

def koch(t,x):
    if x < 3:
        fd(t,x)
    else:
        koch(t,x/3)
        lt(t,60)
        koch(t,x/3)
        rt(t,120)
        koch(t,x/3)
        lt(t,60)
        koch(t,x/3)

def snowflake(t,x):
    for i in range(3):
        koch(t,x)
        rt(t,120)

def sq_koch(t,x):
    if x < 5:
        fd(t,x)
        return
    m = x/5.0
    sq_koch(t,m)
    lt(t,90)
    sq_koch(t,m)
    rt(t,90)
    sq_koch(t,m)
    rt(t,90)
    sq_koch(t,m)
    lt(t,90)
    sq_koch(t,m)

snowflake(bob,3**5)

wait_for_user()



       
