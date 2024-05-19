import tkinter as tk

class Frame(tk.Frame):
    def __init__(self, root=None):
        super().__init__(root,width=600, height=600)
        self.root = root
        self.pack()
        