import customtkinter as ctk
from tkinter import messagebox
import clipboard


def password_manager():
    app_content = ctk.CTkframe()
    app_content.title("password manager")
    app_content.config(padx=50, pady=50)
    app_content.withdraw()
    # canvas
    img = Image.open("logo.png")
    logo = ctk.CTkImage(dark_image=img, size=(200, 200))

    l = ctk.CTkLabel(app_content, text=" ", image=logo)
    l.grid(row=0, column=1, columnspan=2)

    weblab = ctk.CTkLabel(app_content, text="Website:")
    weblab.grid(row=1, column=0, padx=5, pady=5)
    userlab = ctk.CTkLabel(app_content, text="Email/Username:")
    userlab.grid(row=2, column=0, padx=5, pady=5)
    paslab = ctk.CTkLabel(app_content, text="Password:")
    paslab.grid(row=3, column=0, padx=5, pady=5)
    # Entries
    weben = ctk.CTkEntry(app_content)
    weben.grid(row=1, column=1, sticky="ew", padx=5, pady=5)
    weben.focus()
    useren = ctk.CTkEntry(app_content)
    useren.grid(row=2, column=1, sticky="ew", columnspan=2, padx=5, pady=5)
    useren.insert("end", "sadat@gmail.com")
    pasen = ctk.CTkEntry(app_content)
    pasen.grid(row=3, column=1, sticky="ew", padx=5, pady=5)
    # Buttons
    srbtn = ctk.CTkButton(app_content, text="Search", command=seach)
    srbtn.grid(row=1, column=2, sticky="ew")
    genbtn = ctk.CTkButton(
        app_content, text="Generate Password", command=generate)
    genbtn.grid(row=3, column=2, sticky="ew")
    addbtn = ctk.CTkButton(app_content, text="Add", command=save)
    addbtn.grid(row=4, column=1, columnspan=2, sticky="ew", padx=5, pady=5)
    return app_content
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

