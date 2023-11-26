import tkinter as tk
from tkinter import ttk
import Views


class SummaryView(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.mode = None
        self.title = tk.StringVar(value="")
        self.cont = controller

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
        self.tree_view.configure(selectmode="browse")
        self.tree_view.grid(row=0, column=0, sticky="nsew")

        button_frame = tk.Frame(summary_frame)
        self.add_new_button = tk.Button(button_frame, text="Ekle", height=5,
                                        command=lambda: self.open_mode_view(Views.AddEntityView, self.mode, False))
        syllabus_button = tk.Button(button_frame, text="Ders Programını\nGöster", height=5,
                                    command=lambda: self.open_mode_view(Views.SyllabusView, self.mode, True))
        add_relation_button = tk.Button(button_frame, text="Ders Ekle / Sil", height=5,
                                        command=lambda: self.open_mode_view(Views.AddRemoveRelationView, self.mode, True))
        show_details_button = tk.Button(button_frame, text="Bilgileri Göster", height=5,
                                        command=lambda: self.open_mode_view(Views.EntityDetailsView, self.mode, False))

        self.add_new_button.pack(side="top", fill="x", pady=20, padx=10)
        syllabus_button.pack(side="top", fill="x", pady=20, padx=10)
        add_relation_button.pack(side="top", fill="x", pady=20, padx=10)
        show_details_button.pack(side="top", fill="x", pady=20, padx=10)

        button_frame.grid(row=0, column=1)

        summary_frame.pack(side="top", expand=True, fill="both", padx=10, pady=10)

    def open_mode_view(self, view, mode, requires_entity):
        if requires_entity:
            selected_item = self.tree_view.selection()[0]
            item_data = self.tree_view.item(selected_item)
            entity_id = item_data['values'][0]

            management_view = self.cont.get_frame(view)
            management_view.entry_data = entity_id

            management_view.set_mode(mode)
            self.cont.show_frame(view)
        else:
            management_view = self.cont.get_frame(view)
            management_view.set_mode(mode)
            self.cont.show_frame(view)

    def set_mode(self, mode):
        self.mode = mode
        if mode == Views.STUDENT:
            self.title.set("Öğrenciler")
            self.tree_view['columns'] = ('okul_num', 'ad', 'soyad', 'yas', 'veli_ad', 'veli_soyad', 'aktif')

            self.tree_view.column('#0', width=0, stretch=tk.NO)
            self.tree_view.column("okul_num", width=150)
            self.tree_view.column("ad", width=150)
            self.tree_view.column("soyad", width=150)
            self.tree_view.column("yas", width=150)
            self.tree_view.column("veli_ad", width=150)
            self.tree_view.column("veli_soyad", width=150)
            self.tree_view.column("aktif", width=150)

            self.tree_view.heading("okul_num", text="Okul Numarası")
            self.tree_view.heading("ad", text="Ad")
            self.tree_view.heading("soyad", text="Soyad")
            self.tree_view.heading("yas", text="Yaş")
            self.tree_view.heading("veli_ad", text="Veli Adı")
            self.tree_view.heading("veli_soyad", text="Veli Soyadı")
            self.tree_view.heading("aktif", text="Aktif Öğrenci")

            self.add_new_button.config(text="Öğrenci Ekle")

        elif mode == Views.EMPLOYEE:
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

        elif mode == Views.ACTIVITY:
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

        self.populate_tree_view()

    def populate_tree_view(self):
        for item in self.tree_view.get_children():
            self.tree_view.delete(item)

        if self.mode == Views.STUDENT:
            students_query = "SELECT s.ID, s.FIRST_NAME, s.LAST_NAME, TIMESTAMPDIFF(YEAR," \
                             " s.DATE_OF_BIRTH, CURDATE())," \
                             " COALESCE(g.FIRST_NAME, ' '), COALESCE(g.LAST_NAME, ' '), s.IS_ACTIVE" \
                             " FROM student s" \
                             " LEFT JOIN guardian g on g.STUDENT_ID = s.ID"
            students_list = self.cont.sql_query(students_query)
            print(students_list)

            for student in students_list:
                self.tree_view.insert('', 'end', values=student)
        elif self.mode == Views.EMPLOYEE:
            employee_query = "SELECT ID, FIRST_NAME, LAST_NAME, DATE_OF_BIRTH FROM employee"
            employee_list = self.cont.sql_query(employee_query)

            for employee in employee_list:
                self.tree_view.insert('', 'end', values=employee)
        elif self.mode == Views.ACTIVITY:
            activity_query = "SELECT ID, COURSE_NAME FROM course"
            employee_list = self.cont.sql_query(activity_query)

            for employee in employee_list:
                self.tree_view.insert('', 'end', values=employee)
