import tkinter as tk
from tkinter import messagebox

def check_login():
    username = username_entry.get()
    password = password_entry.get()
    if username == "admin" and password == "password":
        messagebox.showinfo("Login Successful", "Welcome!")
    else:
        messagebox.showerror("Login Failed", "Invalid username or password")

# Create the main window
root = tk.Tk()
root.title("Login Form")

# Create username and password labels and entry fields
tk.Label(root, text="Username:").grid(row=0, column=0, padx=10, pady=10)
username_entry = tk.Entry(root)
username_entry.grid(row=0, column=1, padx=10, pady=10)

tk.Label(root, text="Password:").grid(row=1, column=0, padx=10, pady=10)
password_entry = tk.Entry(root, show="*")
password_entry.grid(row=1, column=1, padx=10, pady=10)

# Login button
login_button = tk.Button(root, text="Login", command=check_login)
login_button.grid(row=2, column=0, columnspan=2, pady=10)

# Start the GUI loop
root.mainloop()
