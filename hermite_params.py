import tkinter as tk
from tkinter import ttk

from constants import *

class HermiteParams:
    def __init__(self):
        self.points = []

        self.binButtonImg = tk.PhotoImage(file="res/images/bin_button.png")

    def draw(self, master: tk.Frame=None):
        self.pointsFrame = tk.Frame(master, bg="red", height=50)
        self.pointsFrame.pack(fill="x", padx=30, pady=10)
        self.pointsFrame.pack_propagate(0)

        # self.addPointButton = tk.Button(self.pointsFrame, image=tk.PhotoImage(file=r"C:/Users/avollet/Documents/Hermite_Mathematiques/res/images/add_button.png"))
        # self.addPointButton.pack(side="right")

        self.deleteButton = tk.Button(self.pointsFrame, width=1, height=1, bg=C_SECONDARY, image=self.binButtonImg)
        self.deleteButton.pack(side="right")

        self.pointsCombobox = ttk.Combobox(self.pointsFrame, height=40, background=C_MAIN, foreground=C_TEXT, values=["a", "b", "c"], font=F_CALIBRI)
        self.pointsCombobox.current(0)
        self.pointsCombobox.pack(fill='x')