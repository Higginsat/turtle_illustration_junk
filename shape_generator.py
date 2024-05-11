# 11.23
# Andrew-at
# a shape generator using the the Turtle graphics module 

import turtle

# a turtle sprite named 'bob'
bob = turtle.Turtle()

# sets the color of the pen to green
# color can also be RGB value or name
bob.color("green")

# background to black
turtle.Screen().bgcolor("black")

# generates a square with 'length' sides
def square(t, length):
    for i in range(4):
        bob.fd(length)
        bob.lt(90)
    print(bob)

# generates a triangle
# incomplete at this time, figuring out right angles
'''
def triangle(t, length):
    for i in range(2):
        bob.fd(length)
        bob.lt(90)
'''

def polygon(t, length, n):
""" generates a polygon with n number of sides sides """

    for i in range(n):
        bob.fd(length)
        bob.lt(360 / n)
    print(bob)

def circle(t, r, length):
""" generates a circle with r size radius """

    for i in range(r):
        bob.fd(length)
        bob.lt((360 / r))
    print(bob)

def daisy(t, length):
""" generates a 'daisy' type shape """

    for i in range(9):
        bob.fd(length)
        bob.rt(120)
        bob.color("red")
        for i in range(8):
            bob.fd(length)
            bob.lt(-20)
            bob.color("orange")
    print(bob)
    
def nautilus(t):
""" generates a nautilus """

    size = 1
    while (True):
        for i in range(4):
            bob.fd(size)
            bob.rt(90)
            size = size + 1
        bob.rt(10)

def turbine(t, length):
""" generates a turbine/spiral sort of shape using nested for loops """ 

    for i in range(16):
        bob.fd(length)
        bob.lt(-45)
        for i in range(5):
            bob.fd(length)
            bob.rt(2)
            for i in range(8):
                bob.fd(length)
                bob.rt(-94)
                for i in range(16):
                    bob.fd(length)
                    bob.lt(10)
    print(bob)

# coming back to this one later
'''
def arc(t, r, length, angle):
    bob = t
    for i in range(r):
        bob.fd(length)
        bob.lt((angle))
    print(bob)
'''
#nautilus(bob)
# polygon(bob,50, 5)
# circle(bob, 50, 10)
# arc(bob, 20, 10, 360)
# turbine(bob, 10)
# daisy(bob, 20)
# triangle(bob, 10)

input1 = ''
while input1 != 'q':
    input1 = input("Please c, p, a or s for shapebuilder: ")
    print("c = circle, p = polygon, a = arc, s = square")
    print("Press 'q' to quit.")

    if input1 == 'c':
        circle(bob, 40, 10)

    elif input1 == 'p':
        polygon(bob, 40, 6)

    elif input1 == 's':
        square(bob, 40)

turtle.mainloop()
