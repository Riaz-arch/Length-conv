import tkinter as tk
from tkinter import messagebox

def convert_to_centimeters():
    try:
        # Get the input from the user
        inches = float(entry_inches.get())
        # Convert inches to centimeters
        centimeters = inches * 2.54
        # Show the result in a message box
        messagebox.showinfo("Conversion Result", f"{inches} inches is equal to {inches*2.54} centimeters.")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter a valid number.")