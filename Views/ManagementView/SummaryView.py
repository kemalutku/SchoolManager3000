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
        title_frame.pack(side="top", fill="x", pady=5, padx=5)

        summary_frame = tk.Frame(self)
        summary_frame.columnconfigure(0, weight=1)
        summary_frame.rowconfigure(0, weight=1)
        self.tree_view = ttk.Treeview(summary_frame)
        self.tree_view.grid(row=0, column=0, sticky="nsew")

        button_frame = tk.Frame(summary_frame)
        self.add_new_button = tk.Button(button_frame, text="Ekle", height=5)
        syllabus_button = tk.Button(button_frame, text="Ders Programını\nGöster", height=5)
        add_relation_button = tk.Button(button_frame, text="Ders Ekle / Sil", height=5)
        show_details_button = tk.Button(button_frame, text="Bilgileri Göster", height=5)

        self.add_new_button.pack(side="top", fill="x", pady=20, padx=10)
        syllabus_button.pack(side="top", fill="x", pady=20, padx=10)
        add_relation_button.pack(side="top", fill="x", pady=20, padx=10)
        show_details_button.pack(side="top", fill="x", pady=20, padx=10)

        button_frame.grid(row=0, column=1)

        summary_frame.pack(side="top", expand=True, fill="both", padx=10, pady=10)

    def set_mode(self, mode):
        if mode == STUDENT:
            self.title.set("Öğrenciler")
            self.tree_view['columns'] = ('okul_num', 'ad', 'soyad', 'yas', 'veli_ad', 'veli_soyad')

            self.tree_view.column('#0', width=0, stretch=tk.NO)
            self.tree_view.column("okul_num", width=150)
            self.tree_view.column("ad", width=150)
            self.tree_view.column("soyad", width=150)
            self.tree_view.column("yas", width=150)
            self.tree_view.column("veli_ad", width=150)
            self.tree_view.column("veli_soyad", width=150)

            self.tree_view.heading("okul_num", text="Okul Numarası")
            self.tree_view.heading("ad", text="Ad")
            self.tree_view.heading("soyad", text="Soyad")
            self.tree_view.heading("yas", text="Yaş")
            self.tree_view.heading("veli_ad", text="Veli Adı")
            self.tree_view.heading("veli_soyad", text="Veli Soyadı")

            self.add_new_button.config(text="Öğrenci Ekle")

        elif mode == EMPLOYEE:
            self.title.set("Çalışanlar")
            self.tree_view['columns'] = ('okul_num', 'ad', 'soyad', 'yas', 'e-mail', 'maas')

            self.tree_view.column('#0', width=0, stretch=tk.NO)
            self.tree_view.column("okul_num", width=150)
            self.tree_view.column("ad", width=150)
            self.tree_view.column("soyad", width=150)
            self.tree_view.column("yas", width=150)
            self.tree_view.column("e-mail", width=150)
            self.tree_view.column("maas", width=150)

            self.tree_view.heading("okul_num", text="Çalışan Numarası", anchor=tk.W)
            self.tree_view.heading("ad", text="Ad", anchor=tk.W)
            self.tree_view.heading("soyad", text="Soyad", anchor=tk.W)
            self.tree_view.heading("yas", text="Yaş", anchor=tk.W)
            self.tree_view.heading("e-mail", text="E-Mail", anchor=tk.W)
            self.tree_view.heading("maas", text="Maaş", anchor=tk.W)

            self.add_new_button.config(text="Çalışan Ekle")

        elif mode == ACTIVITY:
            self.title.set("Dersler")
            self.tree_view['columns'] = ('ders_num', 'ad', 'gun', 'b_saati', 'type')

            self.tree_view.column('#0', width=0, stretch=tk.NO)
            self.tree_view.column("ders_num", width=150)
            self.tree_view.column("ad", width=150)
            self.tree_view.column("gun", width=150)
            self.tree_view.column("b_saati", width=150)
            self.tree_view.column("type", width=150)

            self.tree_view.heading("ders_num", text="Ders Numarası", anchor=tk.W)
            self.tree_view.heading("ad", text="Ad", anchor=tk.W)
            self.tree_view.heading("gun", text="Gün", anchor=tk.W)
            self.tree_view.heading("b_saati", text="Başlangıç Saati", anchor=tk.W)
            self.tree_view.heading("type", text="Tür", anchor=tk.W)

            self.add_new_button.config(text="Çalışan Ekle")