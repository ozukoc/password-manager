from tkinter import *
from tkinter import messagebox
from random import randint, shuffle, choice
import pyperclip
import json
# ---------------------------- logoWORD GENERATOR ------------------------------- #
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
           'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


def generator():

    gen_letters = [choice(letters) for char in range(randint(8, 10))]
    gen_symbols = [choice(symbols) for char in range(randint(2, 4))]
    gen_numbers = [choice(numbers) for char in range(randint(2, 4))]

    password_list = gen_letters + gen_numbers + gen_symbols
    shuffle(password_list)

    gen_password = "".join(password_list)

    pyperclip.copy(gen_password)

    pass_entry.insert(0, gen_password)


# ---------------------------- SAVE logoWORD ------------------------------- #
def save_data():
    website = website_entry.get()
    email = username_entry.get()
    password = pass_entry.get()
    new_data = {website: {
        "email": email,
        "password": password,
    }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showerror(title="Oops!",
                             message="Your information is missing !")
    else:
        try:
            with open("data.json", "r") as data_file:
                # Reading old data
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            # Updating old data with new data
            data.update(new_data)

            with open("data.json", "w") as data_file:
                # Saving updated data
                json.dump(data, data_file, indent=4)
        finally:
            website_entry.delete(0, END)
            pass_entry.delete(0, END)
            website_entry.focus()
#----------------------------- Search Data ---------------------------- #


def search_data():
    website = website_entry.get()
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showerror(title="Oops", message="Not found")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(
                title=website, message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(
                title="Error", message=f"No details for {website} exists.")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50, bg="#FFFFFF")

canvas = Canvas(width=200, height=200, bg="#FFFFFF", highlightthickness=0)

logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

# ---------------------------- LABELS ------------------------------- #
website_label = Label(text="Website:", bg="white")
website_label.grid(column=0, row=1)

username_label = Label(text="Email/Username:", bg="white")
username_label.grid(column=0, row=2)

pass_label = Label(text="Password:", bg="white")
pass_label.grid(column=0, row=3)

# ---------------------------- ENTRIES ------------------------------- #
website_entry = Entry()
website_entry.grid(column=1, row=1, columnspan=2, sticky=EW)
website_entry.focus()

username_entry = Entry()
username_entry.grid(column=1, row=2, columnspan=2, sticky=EW)
username_entry.insert(0, "example@email.com")

pass_entry = Entry()
pass_entry.grid(column=1, row=3, sticky=EW)

# ---------------------------- BUTTONS ------------------------------- #
generate_btn = Button(text="Generate Password", command=generator)
generate_btn.grid(column=2, row=3, sticky=EW)

add_btn = Button(text="Add", width=35, command=save_data)
add_btn.grid(column=1, row=4, columnspan=2, )

search_btn = Button(text="Search", command=search_data)  # command=search_data
search_btn.grid(column=2, row=1, sticky=EW)


window.mainloop()
