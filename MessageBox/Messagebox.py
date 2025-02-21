import tkinter as tk
from tkinter import messagebox

def show_message():
    messagebox.showinfo("Greeting", "Hello, welcome to Tkinter!")

# Create the main window
root = tk.Tk()
root.title("Message Box Example")

# Create a button to show the message
button = tk.Button(root, text="Click Me!", command=show_message)
button.pack(pady=20)

# Start the GUI loop
root.mainloop()
