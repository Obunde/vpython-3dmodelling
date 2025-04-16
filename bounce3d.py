from vpython import *
from time import *
mRadius=0.5
wallThickness=1
roomWidth=12
roomHeight=10
roomDepth=20
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
deltaY=0.1
deltaZ=0.1

xPos=0
yPos=0
zPos=0

while True:
    rate(25)  # 25 frames per second
    xPos=xPos + deltaX
    yPos=yPos + deltaY
    zPos=zPos + deltaZ

    Xmre= xPos + mRadius
    Xlme= xPos - mRadius

    Ytme= yPos + mRadius
    Ybme= yPos - mRadius

    Zfme= zPos + mRadius
    Zbme= zPos - mRadius

    Rwe = roomWidth/2 - wallThickness/2
    Lwe= -roomWidth/2 + wallThickness/2

    Cwe= roomHeight/2 - wallThickness/2
    FLOORwe= -roomHeight/2 + wallThickness/2

    Fwe= roomDepth/2 - wallThickness/2
    Bwe = -roomDepth/2 + wallThickness/2
   
    if (Xmre >= Rwe or Xlme<= Lwe):
        # Reverse direction if marble hits a wall
        deltaX =deltaX*(-1) # reverse direction
    if (Ytme >= Cwe or Ybme<= FLOORwe):
        # Reverse direction if marble hits a wall       
        deltaY =deltaY*(-1) # reverse direction
    if (Zfme >= Fwe or Zbme<= Bwe):
        # Reverse direction if marble hits a wall
        deltaZ =deltaZ*(-1)
    marble.pos= vector(xPos, yPos, zPos)
