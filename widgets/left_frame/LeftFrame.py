import tkinter as tk

from utils.Colors import Colors
from utils.Menu import MENU

from widgets.button.Button import Button
from widgets.right_frame.RightFrame import RightFrame


class LeftFrame:
    """
    Class Left menu items
    """

    def __init__(self, window, name):
        self.frame = tk.Frame(master=window, name=name, bg=Colors.BLACK)
        self.master = window
        self.add_frame()
        self.add_menus()

    def add_frame(self):
        self.frame.pack(side=tk.LEFT, fill=tk.Y, pady=(62, 0))

    def handle_click(self, event):
        self.manage_button_colors(event)
        page_name = str(event.widget).split(".")[2]

        rightFrame = self.master.children["rightFrame"]

        RightFrame.destroy_children(rightFrame)

        RightFrame.frame_content(rightFrame, page_name)

    def add_menus(self):

        for menu_key, menu_text in MENU.items():
            if menu_key == "about":
                button = Button(
                    self.frame,
                    menu_key,
                    menu_text,
                    Colors.ORANGE,
                    Colors.BLACK,
                    18,
                    2,
                    handle_click=self.handle_click,
                    side=tk.BOTTOM,
                )
            else:
                button = Button(
                    self.frame,
                    menu_key,
                    menu_text,
                    Colors.ORANGE,
                    Colors.BLACK,
                    18,
                    2,
                    handle_click=self.handle_click,
                    side=tk.TOP,
                )

                if menu_key == "home":
                    self.selected_button_color(button.button)

    def manage_button_colors(self, event):
        for child in event.widget.master.winfo_children():
            if child == event.widget:
                child.configure(bg=Colors.ORANGE, fg=Colors.WHITE)
            else:
                child.configure(bg=Colors.BLACK, fg=Colors.ORANGE)

    def selected_button_color(self, button):

        button.configure(bg=Colors.ORANGE, fg=Colors.WHITE)
