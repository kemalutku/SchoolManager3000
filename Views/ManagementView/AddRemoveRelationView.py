import tkinter as tk
from tkinter import ttk
import Views


class AddRemoveRelationView(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.mode = None
        self.title = tk.StringVar(value="Ders Ekle/Sil")
        self.preload_func = None
        self.cont = controller

        title_frame = tk.Frame(self)
        back_button = tk.Button(title_frame, text="←", command=lambda: self.open_management_view())
        title_label = tk.Label(title_frame, textvariable=self.title)
        back_button.pack(side="left")
        title_label.pack(side="left", fill="x")
        title_frame.pack(side="top", fill="x", pady=5, padx=5)

        self.add_remove_frame = tk.Frame(self)
        self.add_remove_frame.pack(side="top", fill="both", expand=True)
        self.add_relation_frame = tk.Frame(self.add_remove_frame)
        self.add_relation_frame.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")
        self.remove_relation_frame = tk.Frame(self.add_remove_frame)
        self.remove_relation_frame.grid(row=0, column=1, padx=20, pady=20, sticky="nsew")

        self.add_remove_frame.columnconfigure(0, weight=1)
        self.add_remove_frame.columnconfigure(1, weight=1)
        self.add_relation_frame.columnconfigure(0, weight=1)
        self.add_relation_frame.columnconfigure(1, weight=1)
        self.remove_relation_frame.columnconfigure(0, weight=1)
        self.remove_relation_frame.columnconfigure(1, weight=1)


    def set_mode(self, mode):
        self.mode = mode
        if mode == Views.STUDENT or mode == Views.EMPLOYEE:
            tk.Label(self.add_relation_frame, text="DERS EKLE").grid(row=0, column=0, sticky="we", padx=20, pady=20, columnspan=2)
            tk.Label(self.add_relation_frame, text="Öğrenci Numarası").grid(row=1, column=0, sticky="w")
            tk.Label(self.add_relation_frame, text="Ad").grid(row=2, column=0, sticky="w")
            tk.Label(self.add_relation_frame, text="Soyad").grid(row=3, column=0, sticky="w")
            tk.Label(self.add_relation_frame, text="Ders").grid(row=4, column=0, sticky="w")

            tk.Label(self.add_relation_frame, text="").grid(row=1, column=1, sticky="w")
            tk.Label(self.add_relation_frame, text="").grid(row=2, column=1, sticky="w")
            tk.Label(self.add_relation_frame, text="").grid(row=3, column=1, sticky="w")
            self.student_dropdown = ttk.Combobox(self.add_relation_frame)
            self.student_dropdown.grid(row=4, column=1, sticky="w")

            add_relation_button = tk.Button(self.add_relation_frame, text="Ders Ekle")
            add_relation_button.grid(row=5, column=0, columnspan=2, sticky="we")

            tk.Label(self.remove_relation_frame, text="DERS SİL").grid(row=0, column=0, sticky="we", padx=20, pady=20, columnspan=2)
            tk.Label(self.remove_relation_frame, text="Öğrenci Numarası").grid(row=1, column=0, sticky="w")
            tk.Label(self.remove_relation_frame, text="Ad").grid(row=2, column=0, sticky="w")
            tk.Label(self.remove_relation_frame, text="Soyad").grid(row=3, column=0, sticky="w")
            tk.Label(self.remove_relation_frame, text="Ders").grid(row=4, column=0, sticky="w")

            tk.Label(self.remove_relation_frame, text="").grid(row=1, column=1, sticky="w")
            tk.Label(self.remove_relation_frame, text="").grid(row=2, column=1, sticky="w")
            tk.Label(self.remove_relation_frame, text="").grid(row=3, column=1, sticky="w")
            self.student_dropdown = ttk.Combobox(self.remove_relation_frame)
            self.student_dropdown.grid(row=4, column=1, sticky="w")

            remove_relation_button = tk.Button(self.remove_relation_frame, text="Ders Sil")
            remove_relation_button.grid(row=5, column=0, columnspan=2, sticky="we")

        elif mode == Views.ACTIVITY:
            pass

    def open_management_view(self):
        management_view = self.cont.get_frame(Views.SummaryView)
        management_view.set_mode(self.mode)
        self.cont.show_frame(Views.SummaryView)
