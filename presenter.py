import tkinter as tk
from tkinter import filedialog, ttk
import os
import threading
import subprocess
import numpy as np



try:
    from ctypes import windll
    windll.shcore.SetProcessDpiAwareness(1)
except:
        pass



class Presenter():
    '''Class of the presenter.'''
    
    def __init__(self, model, view) -> None:
        '''Initialize the presenter object.'''
        # Save model and view into the presenter
        self.model = model
        self.view = view
    
    def RunUI(self):
        '''Run the UI.'''
        # Initialize UI and start the loop 
        self.view.initUI(self)
        
        
        self.view.after(16)  # 16 milliseconds (roughly 60 FPS)
        if self.model.iSimulationRunning:
            self.model.ball.processObjectFrame()
            print(self.model.y)
            
            
        self.view.mainloop()
        
        self.view.protocol("WM_DELETE_WINDOW", self._on_closing)  # Force closing when 

    def _on_closing(self):
        self.view.quit()  # stops mainloop
        self.view.destroy()  # this is necessary on Windows to prevent Fatal Python Error: PyEval_RestoreThread: NULL tstate
        
    def DropTheBall(self):
        '''Drop the ball'''
        print("Dropping the ball.")
        self.model.isSimulationRunning = True
        
        # Get canvas border 
        canvHeight= self.view.gameCanvas.winfo_height()
        canvWidth= self.view.gameCanvas.winfo_width()
        canvasCenter = canvWidth*0.5
        print(canvWidth)
        print(canvHeight)
        
        ballX0 = (self.model.ball.x - self.model.ball.radius)+canvasCenter
        ballX1 = (self.model.ball.x + self.model.ball.radius)+canvasCenter
        ballY0 = self.model.ball.y - self.model.ball.radius
        ballY1 = self.model.ball.y + self.model.ball.radius
        self.view.gameCanvas.create_oval(ballX0,ballY0,ballX1,ballY1)
        # self.view.gameCanvas
        while self.model.isSimulationRunning == True:
            
            self.view.gameCanvas.delete("all")
            self.model.ball.processObjectFrame()        
            ballX0 = (self.model.ball.x - self.model.ball.radius)+canvasCenter
            ballX1 = (self.model.ball.x + self.model.ball.radius)+canvasCenter
            ballY0 = self.model.ball.y - self.model.ball.radius
            ballY1 = self.model.ball.y + self.model.ball.radius
            
            self.view.gameCanvas.create_oval(ballX0,-ballY0,ballX1,-ballY1, fill = 'white')
            self.view.gameCanvas.update_idletasks()
            
            print("Ball y: " + str(self.model.ball.y))
            print("-canvHeight: " + str(-canvHeight))
            
            if self.model.ball.y < -canvHeight:
                self.model.isSimulationRunning = False
                break
        
        
        self.model.ball.x = 0
        self.model.ball.y = 0
        self.model.ball.speedX = 0
        self.model.ball.speedY = 0
        self.model.isSimulationRunning = False
        
        
    def OpenOptions(self,subplotOptsBtn)->None:
        '''Open subplot options.'''   
        # Create new window
        optsWindowX = subplotOptsBtn.winfo_rootx()
        optsWindowY = subplotOptsBtn.winfo_rooty()
        optsWindow = tk.Toplevel(self.view)
        optsWindow.geometry(f"+{optsWindowX}+{optsWindowY}")
        optsWindow.columnconfigure(0,weight=1)
        optsWindow.rowconfigure(0,weight=1)
        optsWindow.resizable(False, False)
        optsWindow.grab_set()        
        

        

                    
        