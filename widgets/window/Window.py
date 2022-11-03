import tkinter as tk

from utils.Colors import Colors
from utils.Geometri import GEOMETRI


class Window:
    """
    Create Main Window
    """

    def __init__(self, title):
        self.window = tk.Tk()
        self.window.title(title)
        self.window.configure(bg=Colors.BLACK)
        self.set_size()

    def start_method(self):
        self.window.mainloop()

    def set_size(self):
        w, h = GEOMETRI.MAIN_WINDOW_WIDTH, GEOMETRI.MAIN_WINDOW_HEIGHT
        self.window.geometry("%dx%d" % (w, h))
