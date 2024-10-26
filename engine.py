import csv
import os

refreshRate = 60 # refreshrate of physics simulation
timeToSimulate = 2 # time to run the engine, in seconds
totalFrames = int(timeToSimulate * refreshRate)
timePerFrame = 1 / refreshRate
gravity = 9.80665
dataFile = 'outDataDev.csv'

class PhysicsObject:
    def __init__(self, x, y, speedX, speedY, accelX, accelY):
        self.x = x
        self.y = y
        self.speedX = speedX
        self.speedY = speedY
        self.accelX = accelX
        self.accelY = accelY
        self.timeStep = timePerFrame
    def processObjectFrame(self):
        '''
        Updates physics object based on current state to next frame location
        '''
        newX = self.x + self.speedX * timePerFrame + 0.5 * self.accelX * timePerFrame**2
        newY = self.y + self.speedY * timePerFrame + 0.5 * self.accelY * timePerFrame**2
        speedX = self.speedX + self.accelX * timePerFrame
        speedY = self.speedY + self.accelY * timePerFrame

        self.x = newX
        self.y = newY
        self.speedX = speedX
        self.speedY = speedY

startingBall = PhysicsObject(0, 0, 0.1, 0, 0, gravity)

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
