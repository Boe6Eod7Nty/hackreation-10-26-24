import csv
import os

refreshRate = 60 # refreshrate of physics simulation
timeToSimulate = 3 # time to run the engine, in seconds
totalFrames = int(timeToSimulate * refreshRate)
timePerFrame = 1 / refreshRate
gravity = -9.80665
dataFile = 'outDataDev.csv'

class PhysicsObject:
    def __init__(self, x, y, speedX, speedY, accelX, accelY, radius, color):
        self.x = x
        self.y = y
        self.speedX = speedX
        self.speedY = speedY
        self.accelX = accelX
        self.accelY = accelY
        self.timeStep = timePerFrame
        self.radius = radius
        self.color = color
    def processObjectFrame(self):
        '''
        Updates physics object based on current state to next frame location
        '''
        # define boundaries
        leftWall = -100
        rightWall = 100
        topWall = 100
        botWall = -100

        # update physics by verlet integration
        newX = self.x + self.speedX * timePerFrame + 0.5 * self.accelX * timePerFrame**2
        newY = self.y + self.speedY * timePerFrame + 0.5 * self.accelY * timePerFrame**2
        speedX = self.speedX + self.accelX * timePerFrame
        speedY = self.speedY + self.accelY * timePerFrame

        # check for wall collision
        if newX < leftWall:
            newX = leftWall
            speedX = -(speedX)
        elif newX > rightWall:
            newX = rightWall
            speedX = -(speedX)
        if newY < botWall:
            newY = botWall
            speedY = -(speedY)
        elif newY > topWall:
            newY = topWall
            speedY = -(speedY)

        # update object
        self.x = newX
        self.y = newY
        self.speedX = speedX
        self.speedY = speedY

startingBall = PhysicsObject(0, 0, 50, -5, 0, gravity, 0.5, 'red')

data = []
try:
    os.remove(dataFile)
except:
    pass

for frame in range(0, totalFrames):

    startingBall.processObjectFrame()
    ballData = {
        'frame': frame,
        'ballX': startingBall.x,
        'ballY': startingBall.y,
        'speedX': startingBall.speedX,
        'speedY': startingBall.speedY,
        'accelX': startingBall.accelX,
        'accelY': startingBall.accelY
    }

    data.append(ballData)

with open(dataFile, 'w', newline='') as csvfile:
    fieldnames = ['frame', 'ballX', 'ballY', 'speedX', 'speedY', 'accelX', 'accelY']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(data)
