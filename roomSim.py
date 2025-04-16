from vpython import *
from time import *

# Floor
floor = box(pos=vector(0, -5, 0), color=color.white, size=vector(10, 0.1, 10))

# Left Wall
leftWall = box(pos=vector(-5, 0, 0), color=color.white, size=vector(0.1, 10, 10))

# Right Wall
rightWall = box(pos=vector(5, 0, 0), color=color.white, size=vector(0.1, 10, 10))

# Back Wall
backWall = box(pos=vector(0, 0, -5), color=color.white, size=vector(10, 10, 0.1))

# Ceiling
ceiling = box(pos=vector(0, 5, 0), color=color.white, size=vector(10, 0.1, 10))

# Mable
marble = sphere(pos=vector(0, 0, 0), color=color.red, radius=0.5)
deltaX = 0.1
xPos=0
while True:
    rate(10)  # 10 frames per second
    xPos=xPos + deltaX
    if (xPos > 5 or xPos < -5):
        deltaX =deltaX*(-1) # reverse direction
    marble.pos= vector(xPos, 0, 0)
