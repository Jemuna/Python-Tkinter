import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

def open_image():
    file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.bmp;*.gif")])
    if file_path:
        img = Image.open(file_path)
        img = img.resize((400, 400))
        img_tk = ImageTk.PhotoImage(img)
        label.config(image=img_tk)
        label.image = img_tk  # Keep a reference to avoid garbage collection

# Create the main window
root = tk.Tk()
root.title("Image Viewer")

# Button to open an image
open_button = tk.Button(root, text="Open Image", command=open_image)
open_button.pack(pady=10)

# Label to display the image
label = tk.Label(root)
label.pack(pady=10)

# Start the GUI loop
root.mainloop()
