import tkinter as tk
from Interface.OptionPane import OptionPane
from Interface.GrammarPane import GrammarPane
from Interface.AutomatonPane import AutomatonPane

class MainWindow:
    HEIGHT = 1325
    WIDTH = 600
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Proyecto1 - LFP")
        self.root.geometry(f'{MainWindow.HEIGHT}x{MainWindow.WIDTH}')
        self.root.state('zoomed')
        self.root.configure(bg='#212325')

        self.root.grid_columnconfigure(1,weight=1)
        self.root.grid_rowconfigure(0,weight=1)

        self.grammarPane = GrammarPane(self.root)
        self.automatonPane = AutomatonPane(self.root)
        self.automatonPane.grid_remove()
        self.menu = OptionPane(self.root,self.grammarPane,self.automatonPane)

        self.root.mainloop()