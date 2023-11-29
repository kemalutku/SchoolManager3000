import tkinter as tk
import Views


class EntityDetailsView(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.mode = None
        self.title = tk.StringVar(value="")
        self.cont = controller
        self.preload_func = None
        self.entry_data = None

        title_frame = tk.Frame(self)
        back_button = tk.Button(title_frame, text="←", command=lambda: self.open_management_view())
        title_label = tk.Label(title_frame, textvariable=self.title)
        back_button.pack(side="left")
        title_label.pack(side="left", fill="x")
        title_frame.pack(side="top", fill="x", pady=5, padx=5)

        self.entity_details_frame = tk.Frame(self)
        self.entity_details_frame.pack(side="top", fill="both", expand=True, padx=20, pady=30)

        self.entity_frame = tk.Frame(self.entity_details_frame)
        self.courses_frame = tk.Frame(self.entity_details_frame)
        self.entity_frame.grid(row=0, column=0, sticky="nsew")
        self.courses_frame.grid(row=0, column=1, sticky="nsew")

        self.entity_details_frame.columnconfigure(0, weight=1)
        self.entity_details_frame.columnconfigure(1, weight=1)

        self.courses_frame.columnconfigure(0, weight=1)
        self.courses_frame.columnconfigure(1, weight=1)
        self.course_labels = []

    def set_mode(self, mode):
        self.mode = mode
        query_entity = self.get_entity_data()
        if mode == Views.STUDENT:
            okul_no_label = tk.Label(self.entity_frame, text="Okul Numarası")
            name_label = tk.Label(self.entity_frame, text="Ad")
            surname_label = tk.Label(self.entity_frame, text="Soyad")
            birth_date_label = tk.Label(self.entity_frame, text="Doğum Tarihi")
            guardian_label = tk.Label(self.entity_frame, text="Veli")
            guardian_name = tk.Label(self.entity_frame, text="Veli Ad")
            guardian_surname = tk.Label(self.entity_frame, text="Veli Soyadı")
            e_mail_label = tk.Label(self.entity_frame, text=" Veli E-Mail")
            guardian_contact = tk.Label(self.entity_frame, text="Veli İletişim")

            okul_no_label_value = tk.Label(self.entity_frame, text=query_entity['okul_no'])
            name_label_value = tk.Label(self.entity_frame, text=query_entity['ad'])
            surname_label_value = tk.Label(self.entity_frame, text=query_entity['soyad'])
            birth_date_label_value = tk.Label(self.entity_frame, text=query_entity['dogum_tarihi'])
            guardian_label_value = tk.Label(self.entity_frame, text=query_entity['veli'])
            guardian_name_value = tk.Label(self.entity_frame, text=query_entity['veli_ad'])
            guardian_surname_value = tk.Label(self.entity_frame, text=query_entity['veli_soyad'])
            e_mail_label_value = tk.Label(self.entity_frame, text=query_entity['e-mail'])
            guardian_contact_value = tk.Label(self.entity_frame, text=query_entity['veli_numara'])

            okul_no_label.grid(row=0, column=0, sticky="nsew", pady=3, padx=3)
            name_label.grid(row=1, column=0, sticky="nsew", pady=3, padx=3)
            surname_label.grid(row=2, column=0, sticky="nsew", pady=3, padx=3)
            birth_date_label.grid(row=3, column=0, sticky="nsew", pady=3, padx=3)
            guardian_label.grid(row=4, column=0, sticky="nsew", pady=3, padx=3)
            guardian_name.grid(row=5, column=0, sticky="nsew", pady=3, padx=3)
            guardian_surname.grid(row=6, column=0, sticky="nsew", pady=3, padx=3)
            e_mail_label.grid(row=7, column=0, sticky="nsew", pady=3, padx=3)
            guardian_contact.grid(row=8, column=0, sticky="nsew", pady=3, padx=3)

            okul_no_label_value.grid(row=0, column=1, sticky="nsew", pady=3, padx=3)
            name_label_value.grid(row=1, column=1, sticky="nsew", pady=3, padx=3)
            surname_label_value.grid(row=2, column=1, sticky="nsew", pady=3, padx=3)
            birth_date_label_value.grid(row=3, column=1, sticky="nsew", pady=3, padx=3)
            guardian_label_value.grid(row=4, column=1, sticky="nsew", pady=3, padx=3)
            guardian_name_value.grid(row=5, column=1, sticky="nsew", pady=3, padx=3)
            guardian_surname_value.grid(row=6, column=1, sticky="nsew", pady=3, padx=3)
            e_mail_label_value.grid(row=7, column=1, sticky="nsew", pady=3, padx=3)
            guardian_contact_value.grid(row=8, column=1, sticky="nsew", pady=3, padx=3)
            tk.Label(self.courses_frame, text="Alınan Dersler").grid(row=1, column=0, padx=10, pady=10)
            i = 2
            self.clear_tables()
            for lecture in query_entity['dersler']:
                lbl = tk.Label(self.courses_frame, text=lecture)
                lbl.grid(row=i, column=0, padx=10, pady=10)
                self.course_labels.append(lbl)
                i += 1

        elif mode == Views.EMPLOYEE:
            id_label = tk.Label(self.entity_frame, text="Çalışan Numarası")
            name_label = tk.Label(self.entity_frame, text="Ad")
            surname_label = tk.Label(self.entity_frame, text="Soyad")
            birth_date_label = tk.Label(self.entity_frame, text="Doğum Tarihi")

            id_label_value = tk.Label(self.entity_frame, text=query_entity['id'])
            name_label_value = tk.Label(self.entity_frame, text=query_entity['ad'])
            surname_label_value = tk.Label(self.entity_frame, text=query_entity['soyad'])
            birth_date_label_value = tk.Label(self.entity_frame, text=query_entity['dogum_tarihi'])

            id_label.grid(row=0, column=0, sticky="nsew", pady=3, padx=3)
            name_label.grid(row=1, column=0, sticky="nsew", pady=3, padx=3)
            surname_label.grid(row=2, column=0, sticky="nsew", pady=3, padx=3)
            birth_date_label.grid(row=3, column=0, sticky="nsew", pady=3, padx=3)

            id_label_value.grid(row=0, column=1, sticky="nsew", pady=3, padx=3)
            name_label_value.grid(row=1, column=1, sticky="nsew", pady=3, padx=3)
            surname_label_value.grid(row=2, column=1, sticky="nsew", pady=3, padx=3)
            birth_date_label_value.grid(row=3, column=1, sticky="nsew", pady=3, padx=3)

        elif mode == Views.ACTIVITY:
            id_label = tk.Label(self.entity_frame, text="Ders Numarası")
            name_label = tk.Label(self.entity_frame, text="Ders Adı")
            surname_label = tk.Label(self.entity_frame, text="Ders Kitabı")
            # birth_date_label = tk.Label(self.entity_frame, text="Ders Günü")

            id_label_value = tk.Label(self.entity_frame, text=query_entity['id'])
            name_label_value = tk.Label(self.entity_frame, text=query_entity['ad'])
            surname_label_value = tk.Label(self.entity_frame, text=query_entity['kitap'])
            # birth_date_label_value = tk.Label(self.entity_frame, text=query_entity['gun'])

            id_label.grid(row=0, column=0, sticky="nsew", pady=3, padx=3)
            name_label.grid(row=1, column=0, sticky="nsew", pady=3, padx=3)
            surname_label.grid(row=2, column=0, sticky="nsew", pady=3, padx=3)
            # birth_date_label.grid(row=3, column=0, sticky="nsew", pady=3, padx=3)

            id_label_value.grid(row=0, column=1, sticky="nsew", pady=3, padx=3)
            name_label_value.grid(row=1, column=1, sticky="nsew", pady=3, padx=3)
            surname_label_value.grid(row=2, column=1, sticky="nsew", pady=3, padx=3)
            # birth_date_label_value.grid(row=3, column=1, sticky="nsew", pady=3, padx=3)

    def get_entity_data(self):
        if self.mode == Views.STUDENT:
            query = ("SELECT "
                     "s.ID , s.FIRST_NAME , s.LAST_NAME , s.DATE_OF_BIRTH , "
                     "g.FIRST_NAME , g.LAST_NAME , g.MAIL , g.CONTACT "
                     "FROM student s LEFT JOIN guardian g ON s.ID = g.STUDENT_ID "
                     "WHERE s. ID = {};") \
                .format(self.entry_data)
            ders_query = ("SELECT c.COURSE_NAME FROM student s "
                          "LEFT OUTER JOIN  student_section ss ON s.ID = ss.STUDENT_ID "
                          "LEFT OUTER JOIN course_section cs ON cs.ID = ss.SECTION_ID "
                          "LEFT OUTER JOIN course c ON c.ID = cs.COURSE_ID WHERE s.ID = {}") \
                .format(self.entry_data)
            ders_result = self.cont.sql_query(ders_query)

            result = self.cont.sql_query(query)[0]
            entitiy = {
                'okul_no': result[0],
                'ad': result[1],
                'soyad': result[2],
                'dogum_tarihi': result[3],
                'e-mail': result[6],
                'veli': "",
                'veli_ad': result[4],
                'veli_soyad': result[5],
                'veli_numara': result[7],
                'dersler': ders_result,
            }
            return entitiy
        elif self.mode == Views.EMPLOYEE:
            query = "SELECT e.ID, e.FIRST_NAME, e.LAST_NAME, e.DATE_OF_BIRTH FROM employee e WHERE e.ID ={} " \
                .format(self.entry_data)
            result = self.cont.sql_query(query)[0]
            entitiy = {
                'id': result[0],
                'ad': result[1],
                'soyad': result[2],
                'dogum_tarihi': result[3],
            }
            return entitiy
        elif self.mode == Views.ACTIVITY:
            query = "SELECT c.ID, c.COURSE_NAME, c.TEXT_BOOK FROM course c WHERE c.ID ={} " \
                .format(self.entry_data)
            result = self.cont.sql_query(query)[0]
            entitiy = {
                'id': result[0],
                'ad': result[1],
                'kitap': result[2],
            }
            return entitiy

    def open_management_view(self):
        management_view = self.cont.get_frame(Views.SummaryView)
        management_view.set_mode(self.mode)
        self.cont.show_frame(Views.SummaryView)

    def clear_tables(self):
        for label in self.course_labels:
            label.config(text="")
