import tkinter as tk
from tkinter import filedialog
import pandas as pd

root = tk.Tk()

canvas1 = tk.Canvas(root, width=300, height=300,
                    bg='lightsteelblue2', relief='raised')
canvas1.pack()

label1 = tk.Label(root, text='File Conversion Tool', bg='lightsteelblue2')
label1.config(font=('helvetica', 20))
canvas1.create_window(150, 60, window=label1)


def getTxt():
    global read_file

    import_file_path = filedialog.askopenfilename(
        filetypes=(("dat files", "*.dat"),))
    read_file = pd.read_csv(import_file_path)


browseButtonTxt = tk.Button(text="      Import DAT File     ", command=getTxt, bg='green', fg='white',
                            font=('helvetica', 12, 'bold'))
canvas1.create_window(150, 130, window=browseButtonTxt)


def convertToCsv():
    global read_file

    export_file_path = filedialog.asksaveasfilename(defaultextension='.csv')
    read_file.to_csv(export_file_path, index=None)


saveAsButtonCsv = tk.Button(text='Convert DAT to CSV', command=convertToCsv, bg='green', fg='white',
                            font=('helvetica', 12, 'bold'))
canvas1.create_window(150, 180, window=saveAsButtonCsv)

root.mainloop()
