import tkinter as tk
from tkinter import ttk
from presenter import Presenter

try:
    from ctypes import windll
    windll.shcore.SetProcessDpiAwareness(1)
except:
    pass


class View(tk.Tk):
    '''Main UI of the application and view element of the MVP framework.'''

    def __init__(self) -> None:
        '''Initialize the graphical interface.'''
        
        super().__init__()
        self.title("Midnight Science GUI")

        # get screen width and height
        ws = self.winfo_screenwidth()  # width of the screen
        hs = self.winfo_screenheight()  # height of the screen
        self.config(bg='black')
        
        w = 0.7 * ws
        h = 0.7 * hs
        # calculate x and y coordinates for the Tk root window
        x = (ws * 0.1)
        y = (hs * 0.1)

        # set the dimensions of the screen 
        # and where it is placed
        self.geometry('%dx%d+%d+%d' % (w, h, x, y))

    def initUI(self, presenter: Presenter) -> None:
        '''Set up the element in the graphical interface.'''

        self.presenter = presenter
        self.columnconfigure(0,weight=1)
        self.rowconfigure(1,weight=1)
        # Icon frame
        self.iconFrame = TopBanner(self,presenter,bg = 'red')
        self.iconFrame.grid(row=0,column=0,sticky='EW')
        
        # Game canvas
        self.gameCanvas = tk.Canvas(self, bg='gray30')
        self.gameCanvas.grid(row=1, column=0, sticky='NEWS')

        # Call draw_square after the UI is initialized
        self.after(100, self.draw_square)

        # Bind to the configure event to redraw the square when resizing
        self.bind("<Configure>", lambda event: self.draw_square())

    def draw_square(self):
        '''Draw square on the game canvas'''
        # Get current width and height of the canvas
        canvas_width = self.gameCanvas.winfo_width()
        canvas_height = self.gameCanvas.winfo_height()

        square_size = 500  # Adjust size as needed
        x1 = (canvas_width - square_size) / 2  # Center horizontally
        y1 = (canvas_height - square_size) / 2  # Center vertically
        x2 = x1 + square_size
        y2 = y1 + square_size

        # Clear the canvas before drawing
        self.gameCanvas.delete("all")  # Clear any existing shapes
        self.gameCanvas.create_rectangle(x1, y1, x2, y2, fill='white', outline='black', width=4)


class TopBanner(tk.Frame):
    def __init__(self, parent, presenter, *args, **kwarg):
        '''Inititialize tkinter'''
        super().__init__(*args, **kwarg)
        
        self.presenter = presenter
        self.columnconfigure(1,weight=1)
        
        self.startButton = ttk.Button(self,text="Start game",command = self.presenter.DropTheBall)
        self.startButton.grid(row=0,column=0,sticky='W')
        
        self.optionsButton = ttk.Button(self, text="Options")
        self.optionsButton.grid(row=0, column=1, sticky='W')

