import json
from tkinter import *
from tkinter import messagebox
from random import randint,choice,shuffle
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generatepassword():
    password_entry.delete(0,END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


    password_letter = [choice(letters) for item in range(randint(8, 10))]
    password_symbol = [choice(symbols) for item in range(randint(2, 4))]
    password_number = [choice(numbers) for item in range(randint(2, 4))]

    password_list = password_letter+password_number+password_symbol
    shuffle(password_list)

    password = "".join(password_list)

    # password = ""
    # for char in password_list:
    #   password += char

    password_entry.insert(0,password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    wedsite = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        wedsite:{
            "email": email,
            "password":password
        }
    }

    if len(wedsite)==0 or len(password) == 0:
        messagebox.showinfo(title="Oops",message="Hey , there is no data entered ")
    else:

        iscorrect = messagebox.askokcancel("Verifyd",f"email:{email}\npassword:{password}\nIs entered data is correct ?")
        if iscorrect:
            try:
                with open("data.json",mode="r") as data_file:
                    data = json.load(data_file)
            except:
                with open("data.json",mode="w") as data_file:
                    json.dump(new_data,data_file,indent=4)
            else:
                data.update(new_data)
                with open("data.json",mode="w") as data_file:
                    json.dump(data,data_file,indent=4)
            finally:
                website_entry.delete(0,END)
                password_entry.delete(0,END)

def search_action():
    website = website_entry.get()
    with open("data.json", mode="r") as read_data:
        data = json.load(read_data)

    if website in data:
        email = data[website]["email"]
        password = data[website]["password"]
        messagebox.showinfo(title="Email and Password", message=f"email:{email}\npassward:{password}")
    else:
        messagebox.showinfo(title="error", message="NO data found")



# ---------------------------- UI SETUP ------------------------------- #

windows = Tk()
windows.title("password manager")
windows.config(padx=50,pady=50)


canvas = Canvas(height=200, width=200)
logoimage = PhotoImage(file="logo.png")
canvas.create_image(100,100, image= logoimage)
canvas.grid(row=0,column=1)

website_lable = Label(text = "website :")
email_lable = Label(text = "email/username :")
password_lable = Label(text = "Password :")
website_lable.grid(row=1,column=0)
email_lable.grid(row=2,column=0)
password_lable.grid(row=3,column=0)

website_entry = Entry(width=34)
website_entry.focus()
website_entry.grid(column = 1 , row= 1)
email_entry = Entry(width=53)
email_entry.grid(column = 1 , row= 2, columnspan = 2)
email_entry.insert(0, "gururajhr0305l@gmail.com")
password_entry = Entry(width=34)
password_entry.grid(column = 1 , row= 3)

search = Button(text="Search",command=search_action,bg="blue",width=12)
search.grid(column=2, row=1 )
generate_pass_btn = Button(text="Generate password", command=generatepassword)
generate_pass_btn.grid(column = 2, row= 3)
add_btn = Button(text="Add",width=34, command=save)
add_btn.grid(column = 1, row= 4,columnspan = 2)


windows.mainloop()