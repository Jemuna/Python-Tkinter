import tkinter as tk
from tkinter import messagebox

def show_message():
    messagebox.showinfo("Greeting", "Hello, welcome to Tkinter!")

root = tk.Tk()
root.title("Message Box Example")
button = tk.Button(root, text="Click Me!", command=show_message)
button.pack(pady=20)
root.mainloop()
