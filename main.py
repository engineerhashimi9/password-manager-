from tkinter import * # type: ignore
import customtkinter as ctk
from customtkinter import * # type: ignore
from  login_page import LoginManager
from password_generator import generate
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# Password Generator Project

loginManager=LoginManager()

# ------------------------- GUI ------------------------------------------#
def main_page():
    root = ctk.CTk()
    login_frame=loginManager.loginPage(root)
    if loginManager.loginState :
        print("login passed")
        del login_frame
    

    return root


if __name__ == "__main__":
    main_page().mainloop()
