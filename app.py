import tkinter as tk
from tkinter import ttk

from constants import *

import matplotlib.pyplot as plt

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from hermite import DrawPlot


class App(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.width = DEFAULT_WIDTH
        self.height = DEFAULT_HEIGHT
        
        self.initWindow()

        self.fig, self.ax = DrawPlot(points, slopes, precision, True, False, False, centerPoint, intervalLength, True)

    def initWindow(self):
        ws = self.winfo_screenwidth() # width of the screen
        hs = self.winfo_screenheight() # height of the screen

        x = (ws/2) - (DEFAULT_WIDTH/2)
        y = (hs/2) - (DEFAULT_HEIGHT/2)

        self.geometry('%dx%d+%d+%d' % (DEFAULT_WIDTH, DEFAULT_HEIGHT, x, y))

        self.title(DEFAULT_TITLE)
        self.iconbitmap("res/images/gtech.ico")

    def run(self):
        self.draw()
        self.update()
        self.mainloop()

    def update(self):
        self.after(REFRESH_RATE, self.update)

    def tadaa(self):
        print(self.tada.get())

    def draw(self):
        self.config(bg=C_SEPARATION_LINE)

        self.sidebarCanvas = tk.Canvas(self, width=SIDEBAR_WIDTH, bg=C_SECONDARY, bd=0, highlightthickness=0)
        self.sidebarCanvas.pack(side="left", fill="y")
        self.sidebarCanvas.pack_propagate(0)

        self.renderCanvas = tk.Canvas(self, width=DEFAULT_WIDTH - SIDEBAR_WIDTH - SEPARATION_LINE_WIDTH, bg=C_MAIN,
            bd=0, highlightthickness=0)
        self.renderCanvas.pack(side="right", fill="y")
        self.renderCanvas.pack_propagate(0)
        
        self.fig.set_facecolor("none")
        self.ax.set_facecolor("none")
        pltCanvas = FigureCanvasTkAgg(self.fig, master=self.renderCanvas)
        self.pltWidget = pltCanvas.get_tk_widget()

        figW, figH = self.fig.get_size_inches()
        ratio = figW / figH
        self.pltWidget.configure(bg=C_MAIN, width=(1920-SIDEBAR_WIDTH)*0.8, height=(1920-SIDEBAR_WIDTH) * ratio*0.8)
        self.pltWidget.pack()

        self.versionLabel = tk.Label(self.renderCanvas, text='Version {}'.format(CURRENT_VERSION), fg=C_TEXT, bg=C_MAIN,
            font=F_CALIBRI)
        self.versionLabel.place(rely=1.0, relx=1.0, x=0, y=0, anchor="se")
