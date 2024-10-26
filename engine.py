import csv
import os

refreshRate = 60 # refreshrate of physics simulation
timeToSimulate = 3 # time to run the engine, in seconds
totalFrames = int(timeToSimulate * refreshRate)
timePerFrame = 1 / refreshRate
gravity = -9.80665
dataFile = 'outDataDev.csv'
boardPegsList = []

class PegObject:
    def __init__(self, x, y, radius, color, shape):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.shape = shape

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
    def processObjectFrame(self, leftWall, rightWall, topWall, botWall):
        '''
        Updates physics object based on current state to next frame location
        '''

        # update physics by verlet integration
        newX = self.x + self.speedX * timePerFrame + 0.5 * self.accelX * timePerFrame**2
        newY = self.y + self.speedY * timePerFrame + 0.5 * self.accelY * timePerFrame**2
        speedX = self.speedX + self.accelX * timePerFrame
        speedY = self.speedY + self.accelY * timePerFrame

        # check for wall collision
        if newX < leftWall:
            newX = leftWall
            speedX = -(speedX*0.9)
        elif newX > rightWall:
            newX = rightWall
            speedX = -(speedX*0.9)
        if newY < botWall:
            newY = botWall
            speedY = -(speedY*0.9)
        elif newY > topWall:
            newY = topWall
            speedY = -(speedY*0.9)

        # check for peg collision
        for peg in boardPegsList:
            distance = ((newX - peg.x) ** 2 + (newY - peg.y) ** 2) ** 0.5
            jointRadius = peg.radius + self.radius
            if distance < jointRadius:
                pass
        

        # update object
        self.x = newX
        self.y = newY
        self.speedX = speedX
        self.speedY = speedY

startingBall = PhysicsObject(0, 0, 50, -25, 0, gravity, 0.5, 'red')
startingPeg = PegObject(0.1, -20, 25, 'white', 'circle')
boardPegsList.append(startingPeg)

data = []
try:
    os.remove(dataFile)
except:
    pass

for frame in range(0, totalFrames):

    startingBall.processObjectFrame(-100, 100, 100, -100)
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
