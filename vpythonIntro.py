from vpython import *
from time import *

# Floor
floor = box(pos=vector(0, -5, 0), color=color.white, length=10, height=0.1, width=10)

# Left Wall
leftWall = box(pos=vector(-5, 0, 0), color=color.white, length=0.1, height=10, width=10)

# Right Wall
rightWall = box(pos=vector(5, 0, 0), color=color.white, length=0.1, height=10, width=10)

# Back Wall
backWall = box(pos=vector(0, 0, -5), color=color.white, length=10, height=10, width=0.1)

# Ceiling
ceiling = box(pos=vector(0, 5, 0), color=color.white, length=10, height=0.1, width=10)

# Mable
marble = sphere(pos=vector(0, 0, 0), color=color.red, radius=0.5)
while True:
    pass