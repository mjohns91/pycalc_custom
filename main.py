"""Main entry point for the calculator."""

import tkinter as tk
from ui import CalculatorApp

if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()
