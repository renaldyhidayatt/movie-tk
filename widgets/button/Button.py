import tkinter as tk

from utils.Colors import Colors


class Button:
    """
    Create Button Tkinter
    """

    def __init__(
        self,
        master,
        name,
        text,
        fg,
        bg,
        width,
        height,
        handle_click,
        padx=0,
        pady=0,
        side=tk.TOP,
    ) -> None:
        self.button = tk.Button(
            master=master,
            name=name,
            text=text,
            fg=fg,
            bg=bg,
            width=width,
            height=height,
            activebackground=Colors.ORANGE,
        )

        self.padx = padx
        self.pady = pady
        self.side = side
        self.add_button()
        self.bind_event(handle_click)

    def add_button(self):
        self.button.configure(font=("Arial", 12))
        self.button.pack(padx=self.padx, pady=self.pady, side=self.side)

    def bind_event(self, handle_click):
        self.button.bind("<Button-1>", handle_click)
