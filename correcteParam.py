from vpython import *
from time import *
mRadius=2
wallThickness=1
roomWidth=15
roomHeight=8
roomDepth=12
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
deltaz=0.1
deltam=vector(deltaX, deltaY, deltaz)  # Initialize marble velocity vector
# Initialize marble position
xPos=0
yPos=0
zPos=0
mPos=vector(xPos, yPos, zPos)  # Initialize marble position
marble.pos= mPos  # Set marble position
# Initialize marble position

while True:
    rate(10)  # 10 frames per second
    #xPos=xPos + deltaX
    #yPos=yPos + deltaY
    #zPos=zPos + deltaz  
    mPos = mPos + deltam  # Update marble position using velocity vector
    marble.pos= mPos  # Set marble position

    # Check for collision with walls
    # X-axis collision detection
    Xrme= mPos.x + mRadius
    Xlme= mPos.x - mRadius
    Rwe = roomWidth/2 - wallThickness/2
    Lwe= -roomWidth/2 + wallThickness/2

    # y-axis collision detection
    Ytme= mPos.y + mRadius
    Ybme= mPos.y - mRadius
    Ce = roomHeight/2 - wallThickness/2
    Fe= -roomHeight/2 + wallThickness/2

    # z-axis collision detection
    Zfme= mPos.z + mRadius
    Zbme= mPos.z - mRadius
    Fwe = roomDepth/2 - wallThickness/2
    Bwe= -roomDepth/2 + wallThickness/2

    

    if (Xrme >= Rwe or Xlme <= Lwe):
        # Reverse direction if marble hits a wall
        deltam.x =deltam.x*(-1) # reverse direction
    marble.pos= mPos

    if (Ytme >= Ce or Ybme <= Fe):
          # Reverse direction if marble hits a wall
        deltam.y = deltam.y * (-1)  # reverse direction
    marble.pos= mPos

    if (Zfme >= Fwe or Zbme <= Bwe):
        # Reverse direction if marble hits a wall
        deltam.z = deltam.z * (-1)  # reverse direction
    marble.pos= mPos
