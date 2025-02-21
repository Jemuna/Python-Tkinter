import tkinter as tk
from tkinter.colorchooser import askcolor

def choose_color():
    color = askcolor()[1]
    if color:
        root.config(bg=color)

# Create the main window
root = tk.Tk()
root.title("Color Picker")
root.geometry("800x800")

# Button to open the color chooser
color_button = tk.Button(root, text="Choose Color", command=choose_color)
color_button.pack(pady=20)

# Start the GUI loop
root.mainloop()
