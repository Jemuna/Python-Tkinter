import tkinter as tk
import time

def countdown():
    try:
        total_seconds = int(entry.get())
        while total_seconds > 0:
            minutes, seconds = divmod(total_seconds, 60)
            time_display.config(text=f"{minutes:02}:{seconds:02}")
            root.update()
            time.sleep(1)
            total_seconds -= 1
        time_display.config(text="Time's up!")
    except ValueError:
        time_display.config(text="Invalid input!")

# Create the main window
root = tk.Tk()
root.title("Countdown Timer")

# Label and Entry for input time
tk.Label(root, text="Enter time in seconds:").pack(pady=5)
entry = tk.Entry(root)
entry.pack(pady=5)

# Button to start the countdown
start_button = tk.Button(root, text="Start Countdown", command=countdown)
start_button.pack(pady=5)

# Label to display time
time_display = tk.Label(root, text="00:00", font=("Arial", 30))
time_display.pack(pady=10)

# Start the GUI loop
root.mainloop()
