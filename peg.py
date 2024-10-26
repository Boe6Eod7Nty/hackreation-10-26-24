import tkinter as tk

class Peg:
    # Creates circular peg with radius "size"
    def __init__(self, x, y, size):
        self.x = x
        self.y = y
        self.size = size

    def draw(self, canvas):
        # Draw a circle (peg)
        # The bounding box for the circle is defined by (x - size, y - size) to (x + size, y + size)
        canvas.create_oval(self.x - self.size, self.y - self.size,
                           self.x + self.size, self.y + self.size,
                           fill="black", outline="black")