import sys
if sys.version_info[0] == 2:  # Just checking your Python version to import Tkinter properly.
    from Tkinter import *
else:
    from tkinter import *


class Fullscreen_Window:

    def __init__(self):
        self.tk = Tk()
        self.tk.geometry("1000x1000+600+600")
        self.frame = Frame(self.tk)
        self.canvas = Canvas(self.frame)
        # exemplo de linha

        self.frame.pack(fill=BOTH, expand=1)
        self.canvas.pack(fill=BOTH, expand=1)
        self.state = False
        self.tk.bind("<F11>", self.toggle_fullscreen)
        self.tk.bind("<Escape>", self.end_fullscreen)
        self.canvas.bind("<Button-1>", self.clicked)
        self.tk.attributes('-alpha', 0.5)
        self.toggle_fullscreen()
        self.pos = {}

    def clicked(self, event):
        if not self.pos:
            self.pos['x'] = event.x
            self.pos['y'] = event.y
            self.canvas.delete("all")
        else:
            self.canvas.create_line(self.pos['x'], self.pos['y'], event.x, event.y)
            self.pos = {}


    def toggle_fullscreen(self, event=None):
        self.state = not self.state  # Just toggling the boolean
        self.tk.attributes("-fullscreen", self.state)
        return "break"

    def end_fullscreen(self, event=None):
        self.state = False
        self.tk.attributes("-fullscreen", False)
        sys.exit()
        return "break"

if __name__ == '__main__':
    w = Fullscreen_Window()
    w.tk.mainloop()