import tkinter.messagebox
import pyperclip
from time import sleep
from random import *
from tkinter import*
import json  # inbuilt module
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
chars=["!", "#", "%", "&", "(", ")", "*", "+"]
nums=["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
low_letters=[    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z"]
capitalize_letter=[
    "A",
    "B",
    "C",
    "D",
    "E",
    "F",
    "G",
    "H",
    "I",
    "J",
    "K",
    "L",
    "M",
    "N",
    "O",
    "P",
    "Q",
    "R",
    "S",
    "T",
    "U",
    "V",
    "W",
    "X",
    "Y",
    "Z"]



def generate_button_clicked():
    password_entry.delete(0,END)
    char_num = randint(4, 4)
    num_num = randint(2, 4)
    c_letter_num = randint(2, 4)
    rand_chars = sample(chars, char_num)
    rand_nums = sample(nums, num_num)
    rand_letters_c = sample(capitalize_letter, c_letter_num)
    rand_letters_l = sample(low_letters, 16 - char_num - num_num - c_letter_num)
    password = rand_chars + rand_nums + rand_letters_c + rand_letters_l
    password_shuffled = sample(password, 16)
    password_string = "".join(password_shuffled)

    password_entry.insert(0,password_string)
    pyperclip.copy(password_string)


#*********ALTERNATIVE**********
    # password_letters = [choice(letters) for _ in range(randint(8, 10))]
    # password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    # password_numbers = [choice(numbers) for _ in range(randint(2, 4))]
    #
    # password_list = password_letters + password_symbols + password_numbers
    # shuffle(password_list)
    #
    # password = "".join(password_list)
    # password_entry.insert(0, password)

# ---------------------------- Search --------------------------------- #
def search_button_clicked():
    web_entry=website_entry.get().lower()
    if web_entry=="":
        tkinter.messagebox.showerror("Error","Please enter a website!")
    else:
        try:
            with open("data.json","r") as data_file:
                data=json.load(data_file)

        except FileNotFoundError:
            tkinter.messagebox.showwarning("Warning","No data file found. Please add data first!")
        else:
            keys = [key for key, value in data.items()]

            if web_entry in keys:
                e_mail=data[web_entry]["mail"]
                password=data[web_entry]["password"]
                tkinter.messagebox.showinfo("Information",f"{web_entry.upper()}\nMail/Username:  {e_mail}\nPassword:  {password}")
            else:
                tkinter.messagebox.showwarning("Warning",f"'{web_entry.capitalize()}' not found!")



# ---------------------------- SAVE PASSWORD ------------------------------- #
#file process
def add_button_clicked():
    web_entry=website_entry.get().lower()
    mail_entry=email_entry.get().lower()
    pass_entry=password_entry.get().lower()
    new_data={
        web_entry:{
            "mail":mail_entry,
            "password":pass_entry
        }
    }
    if web_entry=="" or mail_entry=="" or pass_entry=="":
        tkinter.messagebox.showwarning("Error","Please fill the all blanks!")
    else:
        question=tkinter.messagebox.askyesno("Question","Are you sure?",default="yes")
        if question==YES:
            try:
                #reading old data
                with open("data.json", "r") as data_file:
                    data=json.load(data_file)
            except FileNotFoundError:
                with open("data.json", "w") as data_file:
                    json.dump(new_data, data_file, indent=4)
            else:
                # updating old data with new data
                data.update(new_data)
                # writing updated data to data file
                with open("data.json", "w") as data_file:
                    json.dump(data, data_file, indent=4)
            finally:
                sleep(0.5)
                tkinter.messagebox.showinfo("Information","Your password has been saved successfully.")
                password_entry.delete(0,END)
                website_entry.delete(0,END)


# ---------------------------- UI SETUP ------------------------------- #


window=Tk()
window.title("Password Manager🔑")
window.config(padx=20,pady=20)
window.iconbitmap(default='favicon.ico')
canvas=Canvas(height=200,width=200)
image=PhotoImage(file="logo.png")
canvas.create_image(100,100,image=image)
canvas.grid(column=1,row=0)


website_label=Label(text="Website:",pady=10)
website_label.grid(column=0,row=1)
email_label=Label(text="Email/Username:",pady=10)
email_label.grid(column=0,row=2)
password_label=Label(text="Password:",pady=10)
password_label.grid(column=0,row=3)

placeholder="example@gmail.com"
website_entry=Entry(width=32)
website_entry.grid(column=1,row=1)
website_entry.focus()
email_entry=Entry(width=50)
email_entry.grid(column=1,row=2,columnspan=2)
email_entry.insert(0,placeholder)
password_entry=Entry(width=32)
password_entry.grid(column=1,row=3)

generate_button=Button(text="Generate Password",width=14,command=generate_button_clicked,bg="#FACBEA")
generate_button.grid(column=2,row=3)
add_button=Button(text="Add",width=30,command=add_button_clicked,bg="#CDFAD5")
add_button.grid(column=1,row=4,columnspan=2)
search_button=Button(text="Search",width=15,bg="#D2E0FB",command=search_button_clicked)
search_button.grid(column=2,row=1)




window.mainloop()
