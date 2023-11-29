import tkinter as tk
from tkinter import ttk
import Views


class SummaryView(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.mode = None
        self.title = tk.StringVar(value="")
        self.preload_func = self.populate_tree_view
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
        self.add_relation_button = tk.Button(button_frame, text="Ders Ekle / Sil", height=5,
                                             command=lambda: self.open_mode_view(Views.AddRemoveRelationView, self.mode,
                                                                                 True))
        show_details_button = tk.Button(button_frame, text="Bilgileri Göster", height=5,
                                        command=lambda: self.open_mode_view(Views.EntityDetailsView, self.mode, True))

        self.add_new_button.pack(side="top", fill="x", pady=20, padx=10)
        syllabus_button.pack(side="top", fill="x", pady=20, padx=10)
        self.add_relation_button.pack(side="top", fill="x", pady=20, padx=10)
        show_details_button.pack(side="top", fill="x", pady=20, padx=10)

        button_frame.grid(row=0, column=1)

        summary_frame.pack(side="top", expand=True, fill="both", padx=10, pady=10)

    def open_mode_view(self, view, mode, requires_entity):
        if requires_entity:
            if self.tree_view.selection():
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
            self.tree_view.heading("ad", text="Ad", command=lambda : self.sort_treeview("ad",False))
            self.tree_view.heading("soyad", text="Soyad", command=lambda : self.sort_treeview("soyad",False))
            self.tree_view.heading("yas", text="Yaş")
            self.tree_view.heading("veli_ad", text="Veli Adı")
            self.tree_view.heading("veli_soyad", text="Veli Soyadı")
            self.tree_view.heading("aktif", text="Aktif Öğrenci")

            self.add_new_button.config(text="Öğrenci Ekle")
            self.add_relation_button.pack(side="top", fill="x", pady=20, padx=10)

        elif mode == Views.EMPLOYEE:
            self.title.set("Çalışanlar")
            self.tree_view['columns'] = ('okul_num', 'ad', 'soyad', 'yas', 'maas', 'meslek')

            self.tree_view.column('#0', width=0, stretch=tk.NO)
            self.tree_view.column("okul_num", width=150)
            self.tree_view.column("ad", width=150)
            self.tree_view.column("soyad", width=150)
            self.tree_view.column("yas", width=150)
            self.tree_view.column("maas", width=150)
            self.tree_view.column("meslek", width=150)

            self.tree_view.heading("okul_num", text="Çalışan Numarası", anchor=tk.W)
            self.tree_view.heading("ad", text="Ad", anchor=tk.W, command=lambda : self.sort_treeview("ad",False))
            self.tree_view.heading("soyad", text="Soyad", anchor=tk.W, command=lambda : self.sort_treeview("soyad",False))
            self.tree_view.heading("yas", text="Yaş", anchor=tk.W)
            self.tree_view.heading("maas", text="Maaş", anchor=tk.W)
            self.tree_view.heading("meslek", text="Meslek", anchor=tk.W)

            self.add_new_button.config(text="Çalışan Ekle")
            self.add_relation_button.pack_forget()

        elif mode == Views.ACTIVITY:
            self.title.set("Dersler")
            self.tree_view['columns'] = ('ders_num', 'ad', 'gun', 'type')

            self.tree_view.column('#0', width=0, stretch=tk.NO)
            self.tree_view.column("ders_num", width=150)
            self.tree_view.column("ad", width=150)
            self.tree_view.column("gun", width=150)
            self.tree_view.column("type", width=150)

            self.tree_view.heading("ders_num", text="Ders Numarası", anchor=tk.W)
            self.tree_view.heading("ad", text="Ad", anchor=tk.W)
            self.tree_view.heading("gun", text="Gün", anchor=tk.W)
            self.tree_view.heading("type", text="Tür", anchor=tk.W)

            self.add_new_button.config(text="Ders Ekle")
            self.add_relation_button.pack_forget()

        self.populate_tree_view()

    def populate_tree_view(self):
        for item in self.tree_view.get_children():
            self.tree_view.delete(item)

        if self.mode == Views.STUDENT:
            students_query = "SELECT s.ID, s.FIRST_NAME, s.LAST_NAME, TIMESTAMPDIFF(YEAR," \
                             " s.DATE_OF_BIRTH, CURDATE())," \
                             " COALESCE(g.FIRST_NAME, ' '), COALESCE(g.LAST_NAME, ' ')," \
                             "CASE WHEN s.IS_ACTIVE = 1 THEN 'EVET' WHEN s.IS_ACTIVE = 0 THEN 'HAYIR'" \
                             " ELSE 'UNKNOWN' END AS IS_ACTIVE_TEXT" \
                             " FROM student s" \
                             " LEFT JOIN guardian g on g.STUDENT_ID = s.ID"
            students_list = self.cont.sql_query(students_query)

            for student in students_list:
                self.tree_view.insert('', 'end', values=student)
        elif self.mode == Views.EMPLOYEE:
            employee_query = "SELECT ID, FIRST_NAME, LAST_NAME, DATE_OF_BIRTH, SALARY FROM employee"
            teacher_query = "SELECT EMP_ID FROM teacher"
            teacher_list = list(self.cont.sql_query(teacher_query))
            teacher_list = [element for tup in teacher_list for element in tup]
            employee_list = list(self.cont.sql_query(employee_query))

            for employee in employee_list:

                employee = list(employee)

                if employee[0] in teacher_list:
                    employee.append('Öğretmen')
                else:
                    employee.append('Diğer')
                self.tree_view.insert('', 'end', values=employee)

        elif self.mode == Views.ACTIVITY:
            course_query = "SELECT c.ID, c.COURSE_NAME, " \
                           "GROUP_CONCAT(DISTINCT sh.DAY_OF_WEEK ORDER BY sh.DAY_OF_WEEK) " \
                           "AS DAYS_OF_WEEK FROM course c JOIN course_section cs ON cs.COURSE_ID = c.ID JOIN " \
                           "section_hours sh ON sh.SEC_ID = cs.ID GROUP BY c.ID, c.COURSE_NAME; "
            course_list = list(self.cont.sql_query(course_query))

            for course in course_list:
                course = list(course)
                course.append('Ders')
                self.tree_view.insert('', 'end', values=course)

    def sort_treeview(self, col, descending):
        data = [(self.tree_view.set(item, col), item) for item in self.tree_view.get_children('')]
        data.sort(reverse=descending)
        for index, (val, item) in enumerate(data):
            self.tree_view.move(item, '', index)
        self.tree_view.heading(col, command=lambda: self.sort_treeview( col, not descending))
