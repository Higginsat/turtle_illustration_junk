import turtle

bob = turtle.Turtle()
bob.color("red")
turtle.Screen().bgcolor("black")

def square(t, length):
    bob = t
    for i in range(4):
        bob.fd(length)
        bob.lt(90)
    print(bob)

def polygon(t, length, n):
    bob = t
    for i in range(n):
        bob.fd(length)
        bob.lt(360/n)
    print(bob)

def circle(t, r, length):
    bob = t
    for i in range(r):
        bob.fd(length)
        bob.lt((360/r))
    print(bob)

# 3 nested for loops, lol
def daisy(t, length):
    bob = t
    for i in range(9):
        bob.fd(length)
        bob.rt(120)
        bob.color("red")
        for i in range(8):
            bob.fd(length)
            bob.lt(-20)
            bob.color("orange")

    print(bob)


def turbine(t, length):
    bob = t
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
def nautilus(t, ):
        bob = t
        size=1
        while (True):
            for _ in range(4):
                bob.forward(size)
            bob.right(90)
            size = size + 1
            bob.right(10)

#polygon(bob,50, 5)
#circle(bob, 50, 10)
#arc(bob, 20, 10, 360)
#turbine(bob, 10)
#daisy(bob, 20)
turtle.mainloop()

'''
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
    
    elif input1 == 'a':
        arc(bob, 50, 10, 90)

turtle.mainloop()
'''
