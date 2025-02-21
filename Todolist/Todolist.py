import tkinter as tk

def add_task():
    task = entry.get()
    if task != "":
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)

def delete_task():
    try:
        task_index = listbox.curselection()
        listbox.delete(task_index)
    except IndexError:
        pass

# Create the main window
root = tk.Tk()
root.title("To-Do List")

# Label and Entry for input task
tk.Label(root, text="Enter a task:").pack(pady=5)
entry = tk.Entry(root, width=30)
entry.pack(pady=5)

# Button to add task
add_button = tk.Button(root, text="Add Task", command=add_task)
add_button.pack(pady=5)

# Listbox to display tasks
listbox = tk.Listbox(root, width=50, height=10)
listbox.pack(pady=5)

# Button to delete selected task
delete_button = tk.Button(root, text="Delete Task", command=delete_task)
delete_button.pack(pady=5)

# Start the GUI loop
root.mainloop()
