from stegano import lsb
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
from stegano import lsb

secret_message = "You Have Been Hacked !"
lsb.hide("image.jpg", secret_message).save("image2.png")

def reveal_message():
    secret = lsb.reveal("image2.png")
    messagebox.showinfo("Hidden Message", secret)

# Create GUI
root = tk.Tk()
root.title("Steganography Demo")

# Load image
img = Image.open("image2.png")
img = img.resize((1217, 540))  # Resize if needed
photo = ImageTk.PhotoImage(img)

# Display image
label = tk.Label(root, image=photo)
label.pack()
label.bind("<Button-1>", lambda e: reveal_message())  # Click to reveal message

root.mainloop()


