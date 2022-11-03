import tkinter as tk
from PIL import Image, ImageTk
from utils.Colors import Colors


class Home:
    def __init__(self, window, bg_color, relief=tk.SUNKEN, side=tk.LEFT):
        self.frame = tk.Frame(master=window, name="home", relief=relief, bg=bg_color)
        self.side = side
        self.bg_color = bg_color

        self.frame_content()
        self.add_frame()

    def add_frame(self):
        self.frame.pack(side=self.side, fill=tk.BOTH, expand=True)

    def frame_content(self):
        text_self = tk.Label(
            self.frame,
            text="Python",
            font=("Helvetica", 18, "bold"),
            fg=Colors.WHITE,
            bg=Colors.BLACK,
        )

        text_self.place(x=820, y=300)

        project = tk.Label(
            self.frame,
            text="Learning Purpose",
            font=("Helvetica", 18, "bold"),
            fg=Colors.WHITE,
            bg=Colors.BLACK,
        )

        project.place(x=770, y=400)
