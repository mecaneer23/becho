#!/usr/bin/env python3

from tkinter import ttk, Tk, StringVar
import sys

if len(sys.argv) > 1:
    total = int(sys.argv[1])
else:
    print("Make sure to include a starting number")
    exit()

root = Tk()
root.title(f"Count Down From {total}")

partial = 0

def count_down():
    global partial
    partial += 1
    iterator.set(total - partial)
    if partial > total:
        root.destroy()

iterator = StringVar(value=str(total))
ttk.Style().configure("TButton", font=("Helvetica", 100))
ttk.Button(root, textvariable=iterator, command=count_down, width=len(str(total))).pack()

root.mainloop()