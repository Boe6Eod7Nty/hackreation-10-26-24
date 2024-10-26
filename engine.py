import csv
import os

refreshRate = 60 # refreshrate of physics simulation
timeToSimulate = 2 # time to run the engine, in seconds
totalFrames = int(timeToSimulate * refreshRate)
timePerFrame = 1 / refreshRate
gravity = 9.80665
dataFile = 'processedData.csv'

class PhysicsObject:
    def __init__(self, x, y, speedX, speedY, accelX, accelY):
        self.x = x
        self.y = y
        self.speedX = speedX
        self.speedY = speedY
        self.accelX = accelX
        self.accelY = accelY

def processObjectFrame(physicsObject):
    '''
    Returns physicsObject with updated values
    '''
    newX = physicsObject.x + physicsObject.speedX * timePerFrame + 0.5 * physicsObject.accelX * timePerFrame**2
    newY = physicsObject.y + physicsObject.speedY * timePerFrame + 0.5 * physicsObject.accelY * timePerFrame**2

    speedX = physicsObject.speedX + physicsObject.accelX * timePerFrame
    speedY = physicsObject.speedY + physicsObject.accelY * timePerFrame

    return PhysicsObject(newX, newY, speedX, speedY, physicsObject.accelX, physicsObject.accelY)

startingBall = PhysicsObject(0, 0, 0, 0, 0, gravity)

data = []

os.remove(dataFile)

for frame in range(0, totalFrames):

    startingBall = processObjectFrame(startingBall)
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
