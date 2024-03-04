from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# Password Generator Project

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    a = [random.choice(letters) for _ in range(nr_letters)]
    b = [random.choice(symbols) for _ in range(nr_symbols)]
    c = [random.choice(numbers) for _ in range(nr_numbers)]

    password_list = a + b + c
    random.shuffle(password_list)

    pass_word = "".join(password_list)
    pyperclip.copy(pass_word)
    pass_field.insert(0, pass_word)




# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    site = web_field.get()
    user = mail_field.get()
    passk = pass_field.get()
    new_data = {site:{
        "email": user,
        "password": passk
    }}
    if len(site) == 0 or len(passk) == 0:
        messagebox.showinfo(title="Error", message="Please don't leave any fields empty")
    else:
        is_ok = messagebox.askokcancel(title=site,
                                       message=f"These are the details entered: \nEmail : {user}\n Password: {passk} \nIs it okay to save?")

        if is_ok:
            try:
                with open("data.json", "r") as data_file:
                    data = json.load(data_file)
            except FileNotFoundError:
                with open("data.json", "w") as data_file:
                    json.dump(new_data, data_file, indent=4)
            else:
                data.update(new_data)
                with open("data.json", "w") as data_file:
                    json.dump(data, data_file, indent=4)
            finally:
                web_field.delete(0, "end")
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

generate = Button(text="Generate Password", command=generate_password)
generate.grid(row=3, column=2)

add = Button(text="add", width=33, command=save)
add.grid(row=4, column=1, columnspan=2)

screen.mainloop()
