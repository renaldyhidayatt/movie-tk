import tkinter as tk

from utils.Colors import Colors
from pages.Home import Home
from pages.MovieDetail import MovieDetail
from pages.MovieList import MovieList


class RightFrame:
    """
    Widget Right Frame
    """

    bg_color = Colors.ORANGE

    def __init__(self, window, name, relief=tk.SUNKEN, side=tk.LEFT):
        self.frame = tk.Frame(
            master=window, name=name, relief=relief, bg=RightFrame.bg_color
        )
        self.side = side
        self.add_frame()

    def add_frame(self):
        # frame content
        self.frame_content()
        self.frame.pack(side=self.side, fill=tk.BOTH, expand=True)

    def frame_content(self, page_name="home"):
        try:
            incoming_frame = self.frame
        except:
            incoming_frame = self
        finally:
            if page_name == "home":

                Home(incoming_frame, RightFrame.bg_color)
            elif page_name == "movieList":

                MovieList(incoming_frame, RightFrame.bg_color)
            elif page_name == "movieDetail":
                MovieDetail(incoming_frame, RightFrame.bg_color)

    def destroy_children(frame):

        for child in frame.winfo_children():
            child.destroy()
