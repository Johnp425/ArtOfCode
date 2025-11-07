import turtle
from random import *

bob = turtle.Turtle()

turtle.colormode(225)
def square (size, side, c):
        bob.color( c )
        for times in range(side):
            bob.forward( size )
            bob.left( angle )

def comet(size,angle,amt):
        for times in range(amt):
                bob.width(times)
                bob.forward(size)
                bob.left(angle)

def jump(x,y):

        bob.penup()
        bob.goto(x,y)
        bob.pendown()

def stair(distance, amount, c, w):
        bob.color(c)
        bob.width(w)
        for times in range( amount ):
                bob.forward( distance )
                bob.left( 90 )
                bob.forward( distance )
                bob.right( 90 )

def drawsquare( sizeS, sizeC ):
        for times in range(4):
                bob.forward(sizeS)
                bob.left( 90 )

def flower():
  for times in range(10):
    r = radint(0,255)
    c = (r,0,0)
    
    polygon(3,100,c)
    bob.left(36)
    bob.color("yellow")
    bob.circle(20)
    bob.end_fil()

