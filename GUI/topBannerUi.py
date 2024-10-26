import tkinter as tk
from tkinter import ttk

class TopBannerUI(tk.Frame):
    def __init__(self, *args, **kwarg):
        '''Inititialize tkinter'''
        super().__init__()
        
        self.columnconfigure(1,weight=1)
        
        self.startButton = ttk.Button(self,text="Start game")
        self.startButton.grid(row=0,column=0,sticky='W')
        
        self.optionsButtion = ttk.Button(self,text="Options")
        self.optionsButtion.grid(row=0,column=1,sticky='W')