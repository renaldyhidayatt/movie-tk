from widgets.window.Window import Window
from widgets.left_frame.LeftFrame import LeftFrame
from widgets.right_frame.RightFrame import RightFrame


if __name__ == "__main__":
    root = Window("Movie Lib")
    left_frame = LeftFrame(root.window, "leftFrame")
    right_frame = RightFrame(root.window, "rightFrame")

    root.start_method()
