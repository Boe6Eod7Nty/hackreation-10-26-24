import numpy as np


class Model():
    '''Model class containing all the submodel of the software.'''

    def __init__(self)->None:
        '''Initialize the model class.'''
        


        
class GameSettings():
    ''' Game Settings'''
    
    def __init__(self)->None:
        gameFrequency = 60
        noOfBalls = 1
        gravity = 9.81
        ball = BallModel(ballX = 20)
        
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
        
        



        