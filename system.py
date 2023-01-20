from tkinter import *
from PIL import Image, ImageTk
import requests
import io
import customtkinter

root = customtkinter.CTk()
#size of window
root.geometry("1350x750")
#title
root.title("Book Recommendation System")
#disable resize option
root.resizable(width=False, height=False)
root.config(bg="#263140")

#creating canvas
canvas = Canvas(root, width=1800, height=750, bd=0, border=0)
canvas.pack()

# Read the image file
image = Image.open("./books.jpg")
# Resize the image
image = image.resize((1800,750))
# Convert the image to a PhotoImage object
image = ImageTk.PhotoImage(image)

# Add the image to the canvas as a background
canvas.create_image(0, 0, image=image, anchor="nw")

root.mainloop()
