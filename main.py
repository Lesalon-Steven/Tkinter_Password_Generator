from tkinter import *


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    site = web_field.get()
    user = mail_field.get()
    passk = pass_field.get()
    user_data = f"{site}, {user}, {passk}"
    f = open("data.txt", "a")
    f.write(f'{user_data}\n')
    f.close()
    web_field.delete(0,"end")
    mail_field.delete(0, "end")
    pass_field.delete(0, "end")


# ---------------------------- UI SETUP ------------------------------- #
screen = Tk()
screen.title("Password Manager")
screen.config(padx=50, pady=50)

canvas = Canvas(height=200, width=200)
picture = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=picture)
canvas.grid(row=0, column=1)

website = Label(text="Website:")
website.grid(row=1, column=0)
web_field = Entry(width=35)
web_field.focus()
web_field.grid(row=1, column=1, columnspan=2)

email = Label(text="Email/Username:")
email.grid(row=2, column=0)
mail_field = Entry(width=35)
mail_field.insert(0, "youremail@whatever.com")
mail_field.grid(row=2, column=1, columnspan=2)

password = Label(text="Password:")
password.grid(row=3, column=0)
pass_field = Entry(width=18)
pass_field.grid(row=3, column=1)

generate = Button(text="Generate Password")
generate.grid(row=3, column=2)

add = Button(text="add", width=33, command=save)
add.grid(row=4, column=1, columnspan=2)

screen.mainloop()
