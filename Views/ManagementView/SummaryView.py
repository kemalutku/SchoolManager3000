import tkinter as tk
from tkinter import ttk
import Views

STUDENT = "student_view"
EMPLOYEE = "employee_view"
ACTIVITY = "activity"


class SummaryView(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.mode = None
        self.title = tk.StringVar(value="")

        title_frame = tk.Frame(self)
        back_button = tk.Button(title_frame, text="←", command=lambda: controller.show_frame(Views.MainScreenView))
        title_label = tk.Label(title_frame, textvariable=self.title)
        back_button.pack(side="left")
        title_label.pack(side="left", fill="x")
        title_frame.pack(side="top", fill="x")

        summary_frame = tk.Frame(self)
        self.tree_view = ttk.Treeview(summary_frame)
        self.tree_view.pack(side="left", expand=True, fill="both")

        button_frame = tk.Frame(summary_frame)
        add_new_button = tk.Button(button_frame, text="Ekle")
        syllabus_button = tk.Button(button_frame, text="Ders Programını\nGöster")
        add_relation_button = tk.Button(button_frame, text="Ders Ekle/Sil")
        show_details_button = tk.Button(button_frame, text="Bilgileri Göster")

        add_new_button.pack(side="top", fill="x")
        syllabus_button.pack(side="top", fill="x")
        add_relation_button.pack(side="top", fill="x")
        show_details_button.pack(side="top", fill="x")
        button_frame.pack(side="left", fill="both")

        summary_frame.pack(side="top", expand=True, fill="both")

    def set_mode(self, mode):
        if mode == STUDENT:
            self.title.set("Öğrenciler")
        elif mode == EMPLOYEE:
            self.title.set("Çalışanlar")
        elif mode == ACTIVITY:
            self.title.set("Dersler")
