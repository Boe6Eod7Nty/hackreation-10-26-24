import csv
import os

refreshRate = 60 # refreshrate of physics simulation
timeToSimulate = 2 # time to run the engine, in seconds
totalFrames = int(timeToSimulate * refreshRate)
timePerFrame = 1 / refreshRate
gravity = 9.80665
dataFile = 'processedData.csv'

data = []
ballStartingData = {'frame': 0, 'ballX': 0, 'ballY': 0, 'speedX': 0.0, 'speedY': 0.0, 'accelX': 0, 'accelY': gravity}

os.remove(dataFile)
data.append(ballStartingData)

for frame in range(1, totalFrames):

    previousFrame = data[frame - 1]

    oldX = previousFrame['ballX']
    oldY = previousFrame['ballY']
    oldSpeedX = previousFrame['speedX']
    oldSpeedY = previousFrame['speedY']

    newX = oldX + oldSpeedX * timePerFrame + 0.5 * previousFrame['accelX'] * timePerFrame**2
    newY = oldY + oldSpeedY * timePerFrame + 0.5 * previousFrame['accelY'] * timePerFrame**2

    speedX = oldSpeedX + previousFrame['accelX'] * timePerFrame
    speedY = oldSpeedY + previousFrame['accelY'] * timePerFrame
    

    ballData = {}
    ballData['frame'] = previousFrame['frame'] + 1
    ballData['ballX'] = newX
    ballData['ballY'] = newY
    ballData['speedX'] = speedX
    ballData['speedY'] = speedY
    ballData['accelX'] = previousFrame['accelX']
    ballData['accelY'] = previousFrame['accelY']

    data.append(ballData)

with open(dataFile, 'w', newline='') as csvfile:
    fieldnames = ['frame', 'ballX', 'ballY', 'speedX', 'speedY', 'accelX', 'accelY']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(data)
