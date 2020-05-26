from os.path import basename
import tkinter as tk
import numpy as np
from tkinter.filedialog import asksaveasfilename, askopenfilename

root = tk.Tk()

def upload():
    # Open the file choosen by the user
    filename = askopenfilename(filetypes=(("csv files", "*.csv"),))
    data = np.genfromtxt(filename, delimiter=",", names=True, dtype=None)


def download():
    pass

btn1 = tk.Button(root, text="Upload .dat file", command=upload)
btn2 = tk.Button(root, text="Download .csv file", command=download)

btn1.pack()
btn2.pack()

root.mainloop()