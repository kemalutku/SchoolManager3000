import tkinter as tk
import Views


class MainScreenView(tk.Frame):
    def __init__(self, parent, cont):
        tk.Frame.__init__(self, parent)
        self.frame_name = "MainScreenView"
        self.cont = cont

        logout_frame = tk.Frame(self)
        name_label = tk.Label(logout_frame, text="Okul Yönetim Sistemi 3000")
        name_label.pack(side="left")
        logout_button = tk.Button(logout_frame, text="Çıkış Yap",
                                  command=lambda: cont.show_frame(Views.LoginScreenView))
        logout_button.config(bg="red")
        logout_button.pack(side="right")
        logout_frame.pack(side="top", fill="x")

        buttons_frame = tk.Frame(self)
        buttons_frame.grid_rowconfigure(0, weight=1)
        buttons_frame.grid_rowconfigure(1, weight=1)
        buttons_frame.grid_rowconfigure(2, weight=1)

        buttons_frame.grid_columnconfigure(0, weight=1)
        buttons_frame.grid_columnconfigure(1, weight=1)

        student_button = tk.Button(buttons_frame, text="Öğrenci Yönetimi",
                                   command=lambda: self.open_management_view(Views.STUDENT))
        employee_button = tk.Button(buttons_frame, text="Çalışan Yönetimi",
                                    command=lambda: self.open_management_view(Views.EMPLOYEE))
        course_button = tk.Button(buttons_frame, text="Ders Yönetimi",
                                  command=lambda: self.open_management_view(Views.ACTIVITY))
        accounting_button = tk.Button(buttons_frame, text="Muhasebe",
                                      command=lambda: cont.show_frame(None))
        stock_button = tk.Button(buttons_frame, text="Stok Takibi",
                                 command=lambda: cont.show_frame(None))
        contact_button = tk.Button(buttons_frame, text="İletişim",
                                   command=lambda: cont.show_frame(None))

        student_button.grid(row=0, column=0, sticky="nsew", padx=[10, 100], pady=20)
        employee_button.grid(row=1, column=0, sticky="nsew", padx=[10, 100], pady=20)
        course_button.grid(row=2, column=0, sticky="nsew", padx=[10, 100], pady=20)
        accounting_button.grid(row=0, column=1, sticky="nsew", padx=[100, 10], pady=20)
        stock_button.grid(row=1, column=1, sticky="nsew", padx=[100, 10], pady=20)
        contact_button.grid(row=2, column=1, sticky="nsew", padx=[100, 10], pady=20)

        buttons_frame.pack(side="top", expand=True, fill="both")

        logo_frame = tk.Frame(self)
        logo_frame.pack(side="top", expand=True, fill="both")

    def open_management_view(self, mode):
        management_view = self.cont.get_frame(Views.SummaryView)
        management_view.set_mode(mode)
        self.cont.show_frame(Views.SummaryView)
