import tkinter as tk
from tkinter import messagebox
import math

def press(num):
    entry.insert(tk.END, str(num))

def equalpress():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except:
        messagebox.showerror("Error", "Invalid input")
        entry.delete(0, tk.END)

def sine():
    try:
        angle = float(entry.get())
        result = math.sin(math.radians(angle))
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except:
        messagebox.showerror("Error", "Invalid input")
        entry.delete(0, tk.END)

def cosine():
    try:
        angle = float(entry.get())
        result = math.cos(math.radians(angle))
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except:
        messagebox.showerror("Error", "Invalid input")
        entry.delete(0, tk.END)

def tangent():
    try:
        angle = float(entry.get())
        result = math.tan(math.radians(angle))
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except:
        messagebox.showerror("Error", "Invalid input")
        entry.delete(0, tk.END)

def arc_tangent():
    try:
        angle = float(entry.get())
        result = 1/math.tan(math.radians(angle))
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except:
        messagebox.showerror("Error", "Invalid input")
        entry.delete(0, tk.END)

def arc_sine():
    try:
        angle = float(entry.get())
        result = 1 / math.sin(math.radians(angle))
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except:
        messagebox.showerror("Error", "Invalid input")
        entry.delete(0, tk.END)

def arc_cosine():
    try:
        angle = float(entry.get())
        result = 1 / math.cos(math.radians(angle))
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except:
        messagebox.showerror("Error", "Invalid input")
        entry.delete(0, tk.END)

def clear():
    entry.delete(0, tk.END)

if __name__ == "__main__":
    gui = tk.Tk()
    gui.title("Calculator")
    gui.configure(background="Black")

    gui.geometry("400x350")

    entry = tk.Entry(gui)
    entry.grid(row=0, column=0, columnspan=10, ipadx=38, ipady=30)

    button_data = [
        ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
        ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
        ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
        ("0", 4, 0), (".", 4, 1), ("+", 4, 2), 
    ]

    for (text, row, col) in button_data:
        button = tk.Button(gui, text=text, fg='black', bg='white', command=lambda t=text: press(t), height=2, width=13)
        button.grid(row=row + 1, column=col, pady=4)

    equal_button = tk.Button(gui, text='=', fg='black', bg='white', command=equalpress, height=2, width=13)
    equal_button.grid(row=5, column=3, pady=4)

    clear_button = tk.Button(gui, text='Clear', fg='black', bg='white', command=clear, height=2, width=13)
    clear_button.grid(row=6, column=3, pady=2)

    sin_button = tk.Button(gui, text='sin', fg='black', bg='white', command=sine, height=2, width=13)
    sin_button.grid(row=5, column=0, pady=2)

    cos_button = tk.Button(gui, text='cos', fg='black', bg='white', command=cosine, height=2, width=13)
    cos_button.grid(row=5, column=1, pady=2)

    tan_button = tk.Button(gui, text='tan', fg='black', bg='white', command=tangent, height=2, width=13)
    tan_button.grid(row=5, column=2, pady=2)

    cot_button = tk.Button(gui, text='cot', fg='black', bg='white', command=arc_tangent, height=2, width=13)
    cot_button.grid(row=6, column=0, pady=2)

    sec_button = tk.Button(gui, text='sec', fg='black', bg='white', command=arc_cosine, height=2, width=13)
    sec_button.grid(row=6, column=1, pady=2)

    cosec_button = tk.Button(gui, text='cosec', fg='black', bg='white', command=arc_sine, height=2, width=13)
    cosec_button.grid(row=6, column=2, pady=2)

    gui.mainloop()

