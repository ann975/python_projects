from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json

#messagebox is a module not class so not imported with *
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    #list comprehensions
    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    #join method
    password = "".join(password_list)

    password_entry.insert(0, password) #inserts password at 0 index
    pyperclip.copy(password) #saves password in clipboard automatically
# ---------------------------- SAVE PASSWORD ------------------------------- #

#saving text to JSON: JavaScript Object Notation, way to transfer data
#nested list and dictionaries, with key, value pair
#write (json.dump()), read (json.load()), update (json.update())
def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    #new dictionary
    new_data ={
        website: {
            "email": email,
            "password": password,
        }
    }

    #standard dialogue
    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty")
    else:
        # with open("data.json", "w") as data_file:
        #     # json.dump(new_data, data_file, indent=4) #write to json file, uses w mode
        #     data = json.load(data_file) #read old data
        #     #takes json data and converts to Python dictionary, has type dictionary, uses r mode
        #     # print(data)
        #     data.update(new_data) #update with new data
        #     json.dump(data, data_file, indent=4) #write new data
        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)
        else:
            data.update(new_data)  # not appending but updating dictionary with new data

            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)

        finally:
            website_entry.delete(0,END)
            password_entry.delete(0, END)

# ---------------------------- FIND PASSWORD ------------------------------- #
def find_password():
    website = website_entry.get()
    try:
        with open("data.json") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No data file found!")
    else:
        if website in data: #check if key is in dictionary
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email:{email}\nPassword:{password}" )
        else:
            messagebox.showinfo(title="Error", message="Website password not saved")


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50, bg="white", highlightthickness=0)

canvas = Canvas(height=200, width=200, bg="white", highlightthickness=0)
lock_image = PhotoImage(file="logo.png")
canvas.create_image(100,100, image=lock_image)
canvas.grid(row=0, column=1)

#Labels
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)

email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)

password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

#Entries
website_entry = Entry(width=21)
website_entry.grid(row=1, column=1)
website_entry.focus() #starts cursor


email_entry = Entry(width= 38)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "email@gmail.com") #END represents last character in entry, 0 would be first

password_entry = Entry(width=21)
password_entry.grid(row=3, column=1)

#Buttons
generate_password_button = Button(text="Generate Password", command=generate_password)
generate_password_button.grid(row=3, column=2)

add_button = Button(text="Add",width=36, command=save)
add_button.grid(row=4, column=1, columnspan=2)

search_button = Button(text="Search", width = 13, command=find_password)
search_button.grid(row=1, column=2)


window.mainloop()