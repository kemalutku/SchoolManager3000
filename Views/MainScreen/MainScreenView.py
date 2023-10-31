import tkinter as tk


class MainScreenView(tk.Frame):
    def __init__(self, parent, cont):
        tk.Frame.__init__(self, parent)
        self.frame_name = "MainScreenView"

        student_button = tk.Button(self, text="Öğrenci Yönetimi", command=lambda: cont.show_frame(self.frame_name))
        employee_button = tk.Button(self, text="Çalışan Yönetimi", command=lambda: cont.show_frame(self.frame_name))
        course_button = tk.Button(self, text="Ders Yönetimi", command=lambda: cont.show_frame(self.frame_name))
        accounting_button = tk.Button(self, text="Muhasebe", command=lambda: cont.show_frame(self.frame_name))
        contact_button = tk.Button(self, text="İletişim", command=lambda: cont.show_frame(self.frame_name))

        student_button.grid(row=0, column=0, sticky="nsew")
        employee_button.grid(row=1, column=0, sticky="nsew")
        course_button.grid(row=2, column=0, sticky="nsew")
        accounting_button.grid(row=0, column=1, sticky="nsew")
        contact_button.grid(row=1, column=1, sticky="nsew")
