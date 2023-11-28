import tkinter as tk
import Views
from tkinter import PhotoImage


class LoginScreenView(tk.Frame):
    frame_name = "LoginScreenView"

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.preload_func = None
        # image = PhotoImage(file=r"Views/LoginScreen/TOBB_Logo.png")

        application_name_label = tk.Label(self, text="Okul Yönetim Sistemi \n 3000")
        application_name_label.pack()

        # app_image = tk.Label(self, image=image)
        # app_image.pack()

        login_button = tk.Button(self, text="Giriş", command=lambda: controller.show_frame(Views.MainScreenView))
        login_button.pack(padx=10, pady=10)
