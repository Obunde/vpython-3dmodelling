from vpython import *
from time import *
mRadius=0.5
wallThickness=0.1
roomWidth=10
roomHeight=10
roomDepth=10
# Floor
floor = box(pos=vector(0, -roomHeight/2, 0), color=color.white, size=vector(roomWidth, wallThickness, roomDepth))

# Left Wall
leftWall = box(pos=vector(-roomWidth/2, 0, 0), color=color.white, size=vector(wallThickness, roomHeight, roomDepth))

# Right Wall
rightWall = box(pos=vector(roomWidth/2, 0, 0), color=color.white, size=vector(wallThickness, roomHeight, roomDepth))

# Back Wall
backWall = box(pos=vector(0, 0, -roomDepth/2), color=color.white, size=vector(roomWidth, roomHeight, wallThickness))

# Ceiling
ceiling = box(pos=vector(0, roomHeight/2, 0), color=color.white, size=vector(roomWidth, wallThickness, roomDepth))

# Mable
marble = sphere(pos=vector(0, 0, 0), color=color.red, radius=mRadius)
deltaX = 0.1
xPos=0
while True:
    rate(10)  # 10 frames per second
    xPos=xPos + deltaX
    if (xPos > (roomWidth/2)-mRadius or xPos < (-roomWidth/2)+mRadius):
        # Reverse direction if marble hits a wall
        deltaX =deltaX*(-1) # reverse direction
    marble.pos= vector(xPos, 0, 0)
