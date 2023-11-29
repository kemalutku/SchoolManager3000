import tkinter as tk
from tkinter import ttk
import Views
from tkcalendar import Calendar
from datetime import datetime

WEEK_MAPPING = {
    0: "MONDAY",
    1: "TUESDAY",
    2: "WEDNESDAY",
    3: "THURSDAY",
    4: "FRIDAY",
    5: "SATURDAY",
    6: "SUNDAY"
}


class AddEntityView(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.mode = None
        self.title = tk.StringVar(value="")
        self.cont = controller
        self.preload_func = None
        self.entry_data = None
        self.guardian_variable = tk.BooleanVar(value=True)
        self.labels = []
        self.clicked_labels = []

        title_frame = tk.Frame(self)
        back_button = tk.Button(title_frame, text="←", command=lambda: self.open_management_view())
        title_label = tk.Label(title_frame, textvariable=self.title)
        back_button.pack(side="left")
        title_label.pack(side="left", fill="x")
        title_frame.pack(side="top", fill="x", pady=5, padx=5)

        self.entity_details_frame = tk.Frame(self)
        self.entity_details_frame.pack(side="top", fill="both", expand=True, padx=20, pady=30)
        self.course_frame = tk.Frame(self)
        self.syllabus_frame = tk.Frame(self.entity_details_frame)

        self.entries = []

    def set_mode(self, mode):
        self.mode = mode
        if mode == Views.STUDENT:
            def toggle_guardian():
                box_state = "normal"
                if not self.guardian_variable.get():
                    box_state = "disabled"
                e_mail_entry['state'] = box_state
                guardian_name_entry['state'] = box_state
                guardian_name_entry['state'] = box_state
                guardian_surname_entry['state'] = box_state
                guardian_contact_entry['state'] = box_state

            self.guardian_variable = tk.BooleanVar(value=True)

            max_student_number_query = "SELECT MAX(ID) FROM student"
            result = self.cont.sql_query(max_student_number_query)

            self.title.set("Öğrenci Ekle")
            okul_no_label = tk.Label(self.entity_details_frame, text="Okul Numarası")
            name_label = tk.Label(self.entity_details_frame, text="Ad")
            surname_label = tk.Label(self.entity_details_frame, text="Soyad")
            birth_date_label = tk.Label(self.entity_details_frame, text="Doğum Tarihi")
            e_mail_label = tk.Label(self.entity_details_frame, text="E-Mail")
            guardian_label = tk.Label(self.entity_details_frame, text="Veli")
            guardian_name = tk.Label(self.entity_details_frame, text="Veli Ad")
            guardian_surname = tk.Label(self.entity_details_frame, text="Veli Soyadı")
            guardian_contact = tk.Label(self.entity_details_frame, text="Veli İletişim")

            okul_no_entry = tk.Label(self.entity_details_frame, text=str(result[0][0] + 1))
            okul_no_entry['state'] = 'disabled'
            name_entry = tk.Entry(self.entity_details_frame)
            surname_entry = tk.Entry(self.entity_details_frame)
            birth_date_calendar = Calendar(self.entity_details_frame)
            e_mail_entry = tk.Entry(self.entity_details_frame)
            guardian_cb = tk.Checkbutton(self.entity_details_frame, variable=self.guardian_variable,
                                         command=toggle_guardian)
            guardian_name_entry = tk.Entry(self.entity_details_frame)
            guardian_surname_entry = tk.Entry(self.entity_details_frame)
            guardian_contact_entry = tk.Entry(self.entity_details_frame)  # TODO: Add Mobile phone verification
            add_student_button = tk.Button(self.entity_details_frame, text="Öğrenci Ekle",
                                           command=self.add_entity_action)

            self.entries.append(okul_no_entry)
            self.entries.append(name_entry)
            self.entries.append(surname_entry)
            self.entries.append(birth_date_calendar)
            self.entries.append(e_mail_entry)
            self.entries.append(guardian_cb)
            self.entries.append(guardian_name_entry)
            self.entries.append(guardian_surname_entry)
            self.entries.append(guardian_contact_entry)

            okul_no_label.grid(row=0, column=0, sticky="nsew", pady=3, padx=3)
            name_label.grid(row=1, column=0, sticky="nsew", pady=3, padx=3)
            surname_label.grid(row=2, column=0, sticky="nsew", pady=3, padx=3)
            birth_date_label.grid(row=3, column=0, sticky="nsew", pady=3, padx=3)
            guardian_label.grid(row=4, column=0, sticky="nsew", pady=3, padx=3)
            e_mail_label.grid(row=5, column=0, sticky="nsew", pady=3, padx=3)
            guardian_name.grid(row=6, column=0, sticky="nsew", pady=3, padx=3)
            guardian_surname.grid(row=7, column=0, sticky="nsew", pady=3, padx=3)
            guardian_contact.grid(row=8, column=0, sticky="nsew", pady=3, padx=3)

            okul_no_entry.grid(row=0, column=1, sticky="nsew", pady=3, padx=3)
            name_entry.grid(row=1, column=1, sticky="nsew", pady=3, padx=3)
            surname_entry.grid(row=2, column=1, sticky="nsew", pady=3, padx=3)
            birth_date_calendar.grid(row=3, column=1, sticky="nsew", pady=3, padx=3)
            guardian_cb.grid(row=4, column=1, sticky="w", pady=3, padx=3)
            e_mail_entry.grid(row=5, column=1, sticky="nsew", pady=3, padx=3)
            guardian_name_entry.grid(row=6, column=1, sticky="nsew", pady=3, padx=3)
            guardian_surname_entry.grid(row=7, column=1, sticky="nsew", pady=3, padx=3)
            guardian_contact_entry.grid(row=8, column=1, sticky="nsew", pady=3, padx=3)
            add_student_button.grid(row=9, column=0, columnspan=2, sticky="nsew", pady=3, padx=3)

            for i in range(9):
                self.entity_details_frame.rowconfigure(i, weight=1)

        elif mode == Views.EMPLOYEE:
            self.title.set("Çalışan Ekle")

            max_employee_number_query = "SELECT MAX(ID) FROM employee"
            result = self.cont.sql_query(max_employee_number_query)

            sicil_no_label = tk.Label(self.entity_details_frame, text="Sicil Numarası")
            name_label = tk.Label(self.entity_details_frame, text="Ad")
            surname_label = tk.Label(self.entity_details_frame, text="Soyad")
            birth_date_label = tk.Label(self.entity_details_frame, text="Doğum Tarihi")
            salary_label = tk.Label(self.entity_details_frame, text="Maaş")
            occupation_label = tk.Label(self.entity_details_frame, text="Meslek")
            isfull_label = tk.Label(self.entity_details_frame, text="Çalışma Türü")

            sicil_no_entry = tk.Label(self.entity_details_frame, text=str(result[0][0] + 1))
            sicil_no_entry['state'] = 'disabled'
            name_entry = tk.Entry(self.entity_details_frame)
            surname_entry = tk.Entry(self.entity_details_frame)
            birth_date_calendar = Calendar(self.entity_details_frame)
            salary_entry = tk.Entry(self.entity_details_frame)
            occupation_entry = ttk.Combobox(self.entity_details_frame, values=["Öğretmen", "Diğer"], state="readonly")
            isfull_entry = ttk.Combobox(self.entity_details_frame, values=["Full", "Part"], state="readonly")
            add_employee_button = tk.Button(self.entity_details_frame, text="Çalışan Ekle",
                                            command=self.add_entity_action)

            self.entries.append(sicil_no_entry)
            self.entries.append(name_entry)
            self.entries.append(surname_entry)
            self.entries.append(birth_date_calendar)
            self.entries.append(salary_entry)
            self.entries.append(occupation_entry)
            self.entries.append(isfull_entry)

            sicil_no_label.grid(row=0, column=0, sticky="nsew")
            name_label.grid(row=1, column=0, sticky="nsew")
            surname_label.grid(row=2, column=0, sticky="nsew")
            birth_date_label.grid(row=3, column=0, sticky="nsew")
            salary_label.grid(row=4, column=0, sticky="nsew")
            occupation_label.grid(row=5, column=0, sticky="nsew")
            isfull_label.grid(row=6, column=0, sticky="nsew")

            sicil_no_entry.grid(row=0, column=1, sticky="nsew")
            name_entry.grid(row=1, column=1, sticky="nsew")
            surname_entry.grid(row=2, column=1, sticky="nsew")
            birth_date_calendar.grid(row=3, column=1, sticky="nsew")
            salary_entry.grid(row=4, column=1, sticky="nsew")
            occupation_entry.grid(row=5, column=1, sticky="nsew")
            isfull_entry.grid(row=6, column=1, sticky="nsew")
            add_employee_button.grid(row=7, column=0, columnspan=2, sticky="nsew")

            for i in range(7):
                self.entity_details_frame.rowconfigure(i, weight=1)

        elif mode == Views.ACTIVITY:
            self.title.set("Ders / Aktivite Ekle")

            tk.Label(self.entity_details_frame, text="Tür").grid(row=0, column=0, sticky="w")
            tk.Label(self.entity_details_frame, text="Ad").grid(row=1, column=0, sticky="w")
            tk.Label(self.entity_details_frame, text="Öğretmen").grid(row=2, column=0, sticky="w")
            tk.Label(self.entity_details_frame, text="Ders Kitabı").grid(row=3, column=0, sticky="w")
            tk.Label(self.entity_details_frame, text="Başlangıç Tarihi").grid(row=4, column=0, sticky="w")
            tk.Label(self.entity_details_frame, text="Bitiş Tarihi").grid(row=5, column=0, sticky="w")

            teacher_list = []
            teacher_query = "SELECT CONCAT(e.ID, '-', e.FIRST_NAME ,' ' ,e.LAST_NAME) " \
                            "FROM teacher t LEFT JOIN employee e ON t.EMP_ID =e.ID;"
            teacher_list = self.cont.sql_query(teacher_query)
            entity_type_selector = ttk.Combobox(self.entity_details_frame, values=['Ders', 'Aktivite'],
                                                state='readonly')
            name_entry = tk.Entry(self.entity_details_frame)
            teacher_selector = ttk.Combobox(self.entity_details_frame, values=[teacher[0] for teacher in teacher_list],
                                            state='readonly')
            book_entry = tk.Entry(self.entity_details_frame)
            start_date_calendar = Calendar(self.entity_details_frame)
            end_date_calendar = Calendar(self.entity_details_frame)
            add_activity_button = tk.Button(self.entity_details_frame, text="Ders / Aktivite Ekle")

            self.entries.append(entity_type_selector)
            self.entries.append(name_entry)
            self.entries.append(teacher_selector)
            self.entries.append(book_entry)
            self.entries.append(start_date_calendar)
            self.entries.append(end_date_calendar)

            entity_type_selector.grid(row=0, column=1, sticky="we")
            name_entry.grid(row=1, column=1, sticky="we")
            teacher_selector.grid(row=2, column=1, sticky="we")
            book_entry.grid(row=3, column=1, sticky="we")
            start_date_calendar.grid(row=4, column=1, sticky="w")
            end_date_calendar.grid(row=5, column=1, sticky="w")
            add_activity_button.grid(row=6, column=0, columnspan=2, sticky="sew")

            self.syllabus_frame.grid(row=0, column=2, sticky="nsew", rowspan=7, pady=10, padx=10)
            self.entity_details_frame.columnconfigure(2, weight=1)
            self.labels = []
            self.clicked_labels = []

            def on_label_click(event):
                clicked_label = event.widget
                grid_info = clicked_label.grid_info()
                hour = grid_info["row"] + 7
                day = WEEK_MAPPING[grid_info["column"] - 1]
                marking_color = 'green'
                color = clicked_label.cget("bg")
                if color != marking_color:
                    clicked_label.config(bg=marking_color)
                    self.clicked_labels.append([hour, day])
                else:
                    try:
                        clicked_label.config(bg='systemWindowBackgroundColor')
                    except tk.TclError:
                        clicked_label.config(bg='SystemButtonFace')
                    self.clicked_labels.remove([hour, day])
                # Print or use the row and column information

            self.syllabus_frame.columnconfigure(0, weight=1)
            for i, d in enumerate(["Pazartesi", "Salı", "Çarşamba", "Perşembe", "Cuma", "Cumartesi", "Pazar"]):
                self.syllabus_frame.columnconfigure(i + 1, weight=1)
                label = tk.Label(self.syllabus_frame, text=d, relief="groove", borderwidth=1, bg="lightgray")
                label.grid(row=0, column=i + 1, sticky="nsew")

            self.syllabus_frame.rowconfigure(0, weight=1)
            for i in range(12):
                self.syllabus_frame.rowconfigure(i + 1, weight=1)
                label = tk.Label(self.syllabus_frame, text="{}:30 -\n{}:20".format(i + 8, i + 9),
                                 relief="groove", borderwidth=1, bg="lightgray")
                label.grid(row=i + 1, column=0, sticky="nsew")

            for i in range(7):
                for j in range(12):
                    label = tk.Label(self.syllabus_frame, text="", relief="groove", borderwidth=1)
                    label.grid(row=j + 1, column=i + 1, sticky="nsew")
                    label.bind("<Button-1>", on_label_click)
                    self.labels.append(label)

    def add_entity_action(self):
        if self.mode == Views.STUDENT:
            student_id = self.entries[0].cget('text')
            student_name = self.entries[1].get()
            student_surname = self.entries[2].get()
            guardian_email = self.entries[4].get()
            guardian_name = self.entries[6].get()
            guardian_surname = self.entries[7].get()
            guardian_contact = self.entries[8].get()
            student_birth_date = self.entries[3].get_date()
            date_str = student_birth_date
            date_obj = datetime.strptime(date_str, "%d.%m.%Y")
            student_formatted_date = date_obj.strftime("%Y-%m-%d")

            insert_student_query = "INSERT INTO student (IS_ACTIVE, ID, FIRST_NAME, LAST_NAME, DATE_OF_BIRTH) " \
                                   "VALUES (1, '{}', '{}', '{}', '{}'" \
                                   ");".format(student_id, student_name, student_surname, student_formatted_date)
            # if student_id or student_name or student_surname or student_formatted_date is None:

            self.cont.sql_query(insert_student_query)
            if self.guardian_variable.get():
                insert_guardian_query = "INSERT INTO guardian (STUDENT_ID, FIRST_NAME, LAST_NAME, MAIL, CONTACT) " \
                                        "VALUES ('{}', '{}', '{}', '{}'," \
                                        " '{}');".format(student_id, guardian_name, guardian_surname, guardian_email,
                                                         guardian_contact)
                self.cont.sql_query(insert_guardian_query)
            commit_result = self.cont.commit()
            if commit_result:
                self.open_management_view()
            else:
                self.commit_fail_popup()
        elif self.mode == Views.EMPLOYEE:
            employee_id = self.entries[0].cget('text')
            employee_name = self.entries[1].get()
            employee_surname = self.entries[2].get()
            employee_birth_date = self.entries[3].get_date()
            date_str = employee_birth_date
            date_obj = datetime.strptime(date_str, "%d.%m.%Y")
            employee_formatted_date = date_obj.strftime("%Y-%m-%d")
            salary = self.entries[4].get()
            occupation = self.entries[5].get()
            isfull = self.entries[6].get()
            if isfull == 'Full':
                isfull = 1
            else:
                isfull = 0

            insert_employee_query = "INSERT INTO employee (ID, IS_FULLTIME, FIRST_NAME, " \
                                    "LAST_NAME, DATE_OF_BIRTH, SALARY)" \
                                    " VALUES('{}', '{}', '{}', '{}', '{}', " \
                                    "'{}')".format(employee_id, isfull, employee_name, employee_surname,
                                                   employee_formatted_date, salary)

            self.cont.sql_query(insert_employee_query)

            if occupation == 'Öğretmen':
                max_teacher_number_query = "SELECT MAX(ID) FROM teacher"
                tresult = self.cont.sql_query(max_teacher_number_query)
                teacher_id = tresult[0][0] + 1
                insert_teacher_query = "INSERT INTO teacher (ID, EMP_ID)" \
                                       " VALUES('{}', '{}')".format(teacher_id, employee_id)
                self.cont.sql_query(insert_teacher_query)
        elif self.mode == Views.ACTIVITY:
            pass

    def open_management_view(self):
        management_view = self.cont.get_frame(Views.SummaryView)
        management_view.set_mode(self.mode)
        self.cont.show_frame(Views.SummaryView)

    def commit_fail_popup(self):
        popup = tk.Toplevel(self)
        popup.title("Kayıt Başarısız!")
        popup_width = 300
        popup_height = 100
        popup.geometry(f"{popup_width}x{popup_height}")

        # Calculate position x and y coordinates
        x_left = self.winfo_x()
        y_top = self.winfo_y()
        root_width = self.winfo_width()
        root_height = self.winfo_height()
        x_center = x_left + (root_width - popup_width) // 2
        y_center = y_top + (root_height - popup_height) // 2

        popup.geometry(f"+{x_center}+{y_center}")

        tk.Label(popup, text="Kayıt Başarısız. Lütfen girdiğiniz alanları ve internet bağlantısınızı kontrol edin!",
                 wraplength=200).pack(pady=20, side="top")
