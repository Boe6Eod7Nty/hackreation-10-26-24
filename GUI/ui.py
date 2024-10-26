import tkinter as tk
from presenter import Presenter
from topBannerUi import TopBannerUI

try:
    from ctypes import windll
    windll.shcore.SetProcessDpiAwareness(1)
except:
        pass


class UI(tk.Tk):
    '''Main UI of the application and view element of the MVP framework.'''

    def __init__(self) -> None:
        '''Initialize the graphical interface.'''
        
        super().__init__()
        self.title("Midnight Science GUI")

        # get screen width and height
        ws = self.winfo_screenwidth() # width of the screen
        hs = self.winfo_screenheight() # height of the screen
        self.config(bg='black')
        
        w = 0.7*ws
        h = 0.7*hs
        # calculate x and y coordinates for the Tk root window
        x = (ws*0.1)
        y = (hs*0.1)

        # set the dimensions of the screen 
        # and where it is placed
        self.geometry('%dx%d+%d+%d' % (w, h, x, y))


    def initUI(self,presenter:Presenter)->None:
        '''Set up the element in the graphical interface.'''

        self.columnconfigure(0,weight=1)
        self.rowconfigure(1,weight=1)
        # Icon frame
        self.iconFrame = TopBannerUI(self,bg = 'red')
        self.iconFrame.grid(row=0,column=0,sticky='EW')
        
        self.gameCanvas = tk.Canvas(self,bg= 'gray30')
        self.gameCanvas.grid(row=1,column=0,sticky='NEWS')
        
