from tkinter import *

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
screen = Tk()
screen.title("Password Manager")
screen.config(padx=20, pady=20)
canvas = Canvas(height=200, width=200)
picture = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=picture)
canvas.pack()

screen.mainloop()
