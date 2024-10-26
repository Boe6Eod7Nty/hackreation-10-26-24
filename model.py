import numpy as np
from engine import PhysicsObject

class Model():
    '''Model class containing all the submodel of the software.'''

    def __init__(self)->None:
        '''Initialize the model class.'''
        self.gameFrequency = 30
        self.timeStep = 1/self.gameFrequency
        self.noOfBalls = 1
        self.gravity = -9.81
        self.canvasHeight = 5 # in meters
        self.iSimulationRunning = False
        radius = 20
        
        color = '#FF0000'
        self.ball = PhysicsObject(0, 0, 0, 0, 0, self.gravity, radius,color)
        self.ball.timePerFrame = self.timeStep
        


        
class GameSettings():
    ''' Game Settings'''
    
    def __init__(self)->None:
        '''fff'''
        
class BallModel():
    '''Game model'''
    
    def __init__(self,
                 ballMass = 1,
                 ballRadius = 5,
                 ballColor = '#FF0000',
                 ballX = 0,
                 ballY = 0)->None:
        
        self.ballMass = ballMass
        self.ballRadius = ballRadius
        self.ballColor = ballColor
        self.ballX = ballX
        self.ballY = ballY
        self.ballXdot = 0
        self.ballYdot = 0
        
        self.ballVert = np.array()
        
        



        