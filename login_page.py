import customtkinter as ctk
from tkinter import messagebox
from PIL import Image
import json


class LoginManager:
    def __init__(self):
        self.loginState = False

    def loginPage(self, window):
        self.main_container = ctk.CTkFrame(master=window)
        self.main_container.pack(fill="both", expand=True)
        backround = ctk.CTkImage(Image.open("python.jpg"), size=(900, 600))
        wlab = ctk.CTkLabel(self.main_container, image=backround)
        wlab.grid(row=0, column=0)

        login_box = ctk.CTkFrame(master=self.main_container)
        login_box.grid(row=0, column=0, sticky="ns")
        log_lab = ctk.CTkLabel(
            login_box,
            text="Wellcome to password manager\nlogin page",
            text_color="#FFAB6D",
            font=("Gabriola", 20, "bold"),
        )
        log_lab.grid(row=0, column=0, padx=30, pady=(150, 30))
        self.user_en = ctk.CTkEntry(
            login_box, placeholder_text="user name", width=200)
        self.user_en.grid(row=1, column=0, padx=10, pady=(50, 10))
        self.pass_en = ctk.CTkEntry(
            login_box, placeholder_text="user password", width=200, show="*")
        self.pass_en.grid(row=2, column=0, padx=10, pady=10)

        log_btn = ctk.CTkButton(login_box, text="login", command=self.login)
        log_btn.grid(row=3, column=0, columnspan=2, padx=10, pady=(50, 10))

        if_not = ctk.CTkLabel(
            login_box,
            text="Have not any so enter new user name\n and password.",
            font=("Gabriola", 15, "normal"),
        )
        if_not.grid(row=4, column=0, columnspan=2, padx=10, pady=(50, 10))
        return self.main_container

    def check_pass(self, us: str, ps: str):
        try:
            with open("data.json", "r") as f:
                data = json.load(f)
                user = data["login_for_app"]["user_name"]
                passwd = data["login_for_app"]["password"]
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

    def login(self):
        user_name = self.user_en.get()
        user_pass = self.pass_en.get()
        if self.check_pass(user_name, user_pass):
            self.loginState = True

        else:
            messagebox.showerror("error", "user name or password is wrong!")


def loginPage4(window):
    # 1. Create the main background container frame
    # Ensure it fills the window

    # Background image setup
    backround = ctk.CTkImage(Image.open("python.jpg"), size=(900, 600))
    # text="" prevents default text overlay
    wlab = ctk.CTkLabel(main_container, image=backround, text="")
    wlab.grid(row=0, column=0)

    # 2. Create the actual login box frame ON TOP of the background container
    # Fixed: Passed master=main_container explicitly so CustomTkinter won't crash

    # --- Content inside the login_box ---
    log_lab = ctk.CTkLabel(
        login_box,  # Fixed: Pointing to login_box
        text="Welcome to password manager\nlogin page",  # Fixed typo "Wellcome"
        text_color="#FFAB6D",
        font=("Gabriola", 20, "bold"),
    )
    log_lab.grid(row=0, column=0, padx=30, pady=(150, 30))

    self.user_en = ctk.CTkEntry(
        login_box, placeholder_text="user name", width=200)
    self.user_en.grid(row=1, column=0, padx=10, pady=(50, 10))

    pass_en = ctk.CTkEntry(
        # Added show="*" to hide password characters
        login_box, placeholder_text="user password", show="*", width=200)
    pass_en.grid(row=2, column=0, padx=10, pady=10)

    log_btn = ctk.CTkButton(login_box, text="login", command=login)
    # Removed columnspan=2 since you only have 1 column
    log_btn.grid(row=3, column=0, padx=10, pady=(50, 10))

    if_not = ctk.CTkLabel(
        login_box,
        text="Don't have an account? Enter a new username\n and password below.",
        font=("Gabriola", 15, "normal"),
    )
    if_not.grid(row=4, column=0, padx=10, pady=(50, 10))

    return main_container  # Return the base frame to main.py
