import tkinter as tk

class HermiteParams:
    def __init__(self, master: tk.Canvas=None):
        self.master = master

    def draw(self):
        self.master.grid_rowconfigure