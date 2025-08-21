from tkinter import *
from tkinter.messagebox import showwarning, showinfo
from random import randint, choice, shuffle
import pyperclip
import json

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
# ---------------------------- SEARCH PASSWORD ------------------------------- #
def search_password():
    if website_name_entry.get():
        name = website_name_entry.get()
        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            showwarning(title="Missing File", message="File not Found")
        else:
            for key, value in data.items():
                if key == name:
                    email = value["email"]
                    password = value["password"]
                    showinfo(name, f"Email: {email}\nPassword: {password}")
                else:
                    showwarning(title="Missing Website", message="Data not Found")
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]
    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)
    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_password():
    if website_name_entry.get() and email_entry.get() and password_entry.get():
        website_name = website_name_entry.get()
        email = email_entry.get()
        password = password_entry.get()
        new_data = {
            website_name: {
                "email": email,
                "password": password,
            }
        }
        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file)
        else:
            data.update(new_data)
            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)
        finally:
            website_name_entry.delete(0, "end")
            password_entry.delete(0, "end")
    else:
        showwarning(title = "Missing Field Values", message = "Please fill in all the fields")
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(row=0, column=1)

website_name_label = Label(text="Website:")
website_name_label.grid(row=1, column=0)
website_name_label.focus()

website_name_entry = Entry(width=26)
website_name_entry.grid(row=1, column=1)

search_button = Button(text="Search Website", width=15, command=search_password)
search_button.grid(row=1, column=2)

email_label = Label(text="E-mail/Username:")
email_label.grid(row=2, column=0)

email_entry = Entry(width=45)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "antoniou.kostas97@gmail.com")

password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

password_entry = Entry(width=26)
password_entry.grid(row=3, column=1)

generate_button = Button(text="Generate password", command=generate_password)
generate_button.grid(row=3, column=2)

add_button = Button(text="Add", width=36, command=add_password)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()