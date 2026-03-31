from tkinter import *
import customtkinter as ctk
from customtkinter import *
from tkinter import messagebox
import clipboard
from PIL import Image
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# Password Generator Project
import random

ll = True


def generate():
    letters = [
        "a",
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
        "z",
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
        "Z",
    ]
    numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    symbols = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]

    password_list = (
        [random.choice(letters) for i in range(random.randint(8, 10))]
        + [random.choice(symbols) for j in range(random.randint(2, 4))]
        + [random.choice(numbers) for k in range(random.randint(2, 4))]
    )

    random.shuffle(password_list)

    password = "".join(password_list)
    clipboard.copy(password)
    genbtn["text"] = "copied to clipboard"
    genbtn["bg"] = "red"
    pasen.delete(0, "end")
    pasen.insert("end", password)
    # -----------------------------------#


def check_pass(us: str, ps: str):
    try:
        with open("data.json", "r") as f:
            data = json.load(f)
            user = data["login_for_app"]["user_name"]
            passwd = data["login_for_app"]["password"]
            print(user, passwd)
            print(us, ps)
            return us == user and ps == passwd
    except:
        with open("data.json", "w") as f:
            json.dump(
                {
                    "login_for_app": {
                        "user_name": f"{us}",
                        "password": f"{ps}",
                    }
                },
                f,
                indent=4,
            )
            return True


def login():
    user_name = user_en.get()
    user_pass = pass_en.get()
    if check_pass(user_name, user_pass):
        print("login sucess")
        root.withdraw()
        window.deiconify()

        return True
    else:
        messagebox.showerror("error", "user name or password is wrong!")
        return False


def save():
    web = weben.get()
    email = useren.get().strip()
    pas = pasen.get().strip()
    dic = {web: {"email": email, "password": pas}}
    if len(web) and len(email) and len(pas):
        try:
            with open("data.json", "r") as f:
                data = json.load(f)

        except:
            with open("data.json", "w") as f:
                json.dump(dic, f, indent=4)
        else:
            data.update(dic)
            with open("data.json", "w") as f:
                json.dump(data, f, indent=4)
        finally:
            weben.delete(0, "end")
            useren.delete(0, "end")
            pasen.delete(0, "end")
            messagebox.showinfo("sucess", "Your data has been saved!")
    else:
        messagebox.showerror("error", "plz complete the form!")


def seach():
    web = weben.get()
    if len(web):
        try:
            with open("data.json", "r") as f:
                j = json.load(f)
            if web in j:
                messagebox.showinfo(
                    "found!",
                    f"email:{j[web]["email"]} \n\npassword:{j[web]["password"]}",
                )
            else:
                messagebox.showerror(
                    "not found",
                    "Sorry!\n there is not record with this website name",
                )
        except:
            messagebox.showerror("not found", "Sorry! Data not found!")

    else:
        messagebox.showerror("erorr", "Plz enter your website name first!")


# ------------------------- GUI ------------------------------------------#
root = CTk()
root.title("login to password manager")
root.config(width=900, height=600)
backround = CTkImage(Image.open("python.jpg"), size=(900, 600))
wlab = CTkLabel(root, image=backround)
wlab.grid(row=0, column=0)
login_frame = CTkFrame(root)
login_frame.grid(row=0, column=0, sticky="ns")
log_lab = CTkLabel(
    login_frame,
    text="Wellcome to password manager\nlogin page",
    text_color="#FFAB6D",
    font=("Gabriola", 20, "bold"),
)
log_lab.grid(row=0, column=0, padx=30, pady=(150, 30))
user_en = CTkEntry(login_frame, placeholder_text="user name", width=200)
user_en.grid(row=1, column=0, padx=10, pady=(50, 10))
pass_en = CTkEntry(login_frame, placeholder_text="user password", width=200)
pass_en.grid(row=2, column=0, padx=10, pady=10)

log_btn = CTkButton(login_frame, text="login", command=login)
log_btn.grid(row=3, column=0, columnspan=2, padx=10, pady=(50, 10))

if_not = CTkLabel(
    login_frame,
    text="Have not any so enter new user name\n and password.",
    font=("Gabriola", 15, "normal"),
)
if_not.grid(row=4, column=0, columnspan=2, padx=10, pady=(50, 10))


################################
window = ctk.CTkToplevel(root)
window.title("password manager")
window.config(padx=50, pady=50)
window.withdraw()
# canvas
img = Image.open("logo.png")
logo = ctk.CTkImage(dark_image=img, size=(200, 200))

l = ctk.CTkLabel(window, text=" ", image=logo)
l.grid(row=0, column=1, columnspan=2)

weblab = ctk.CTkLabel(window, text="Website:")
weblab.grid(row=1, column=0, padx=5, pady=5)
userlab = ctk.CTkLabel(window, text="Email/Username:")
userlab.grid(row=2, column=0, padx=5, pady=5)
paslab = ctk.CTkLabel(window, text="Password:")
paslab.grid(row=3, column=0, padx=5, pady=5)
# Entries
weben = ctk.CTkEntry(window)
weben.grid(row=1, column=1, sticky="ew", padx=5, pady=5)
weben.focus()
useren = ctk.CTkEntry(window)
useren.grid(row=2, column=1, sticky="ew", columnspan=2, padx=5, pady=5)
useren.insert("end", "sadat@gmail.com")
pasen = ctk.CTkEntry(window)
pasen.grid(row=3, column=1, sticky="ew", padx=5, pady=5)
# Buttons
srbtn = ctk.CTkButton(window, text="Search", command=seach)
srbtn.grid(row=1, column=2, sticky="ew")
genbtn = ctk.CTkButton(window, text="Generate Password", command=generate)
genbtn.grid(row=3, column=2, sticky="ew")
addbtn = ctk.CTkButton(window, text="Add", command=save)
addbtn.grid(row=4, column=1, columnspan=2, sticky="ew", padx=5, pady=5)
root.mainloop()


# window
