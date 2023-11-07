import tkinter as tk
import Views


class LoginScreenView(tk.Frame):
    frame_name = "LoginScreenView"
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        application_name_label = tk.Label(self, text="Okul Yönetim Sistemi \n 3000")
        application_name_label.pack()

        login_button = tk.Button(self, text="Giriş", command=lambda: controller.show_frame(Views.MainScreenView))
        login_button.pack(padx=10, pady=10)