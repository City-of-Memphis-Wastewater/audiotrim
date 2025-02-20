# audiotrim/gui.py

import tkinter as tk
from tkinter import filedialog
import audiotrim.config_utils as config_utils

def create_gui(defaults, script):
    def browse_file():
        filename = filedialog.askopenfilename()
        if filename:
            input_file_entry.delete(0, tk.END)
            input_file_entry.insert(0, filename)
    
    root = tk.Tk()
    root.geometry("+75+75")
    root.title("Audio Trim GUI")
    #root.iconbitmap("psg.ico")
    tk.Label(root, text="Input File").grid(row=0, column=0)
    input_file_entry = tk.Entry(root, width=80)
    input_file_entry.grid(row=0, column=1)
    input_file_entry.insert(0, defaults['input_file'])
    tk.Button(root, text="Browse", command=browse_file).grid(row=0, column=2)

    tk.Label(root, text="Output File").grid(row=1, column=0)
    output_file_entry = tk.Entry(root, width=80)
    output_file_entry.grid(row=1, column=1)
    output_file_entry.insert(0, defaults['output_file'])

    tk.Label(root, text="Start Time (s)").grid(row=2, column=0)
    start_time_entry = tk.Entry(root)
    start_time_entry.grid(row=2, column=1)
    start_time_entry.insert(0, defaults['start_time'])

    tk.Label(root, text="End Time (s)").grid(row=3, column=0)
    end_time_entry = tk.Entry(root)
    end_time_entry.grid(row=3, column=1)
    end_time_entry.insert(0, defaults['end_time'])

    def on_trim():
        path_in = input_file_entry.get()
        path_out = output_file_entry.get()
        time_start = float(start_time_entry.get())
        time_end = float(end_time_entry.get())
        script(path_in, path_out, time_start, time_end)

    tk.Button(root, text="Trim Audio", command=on_trim).grid(row=4, columnspan=3)
    root.mainloop()
