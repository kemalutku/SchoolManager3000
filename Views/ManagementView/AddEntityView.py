import tkinter as tk
import Views
from tkcalendar import Calendar


class AddEntityView(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.mode = None
        self.title = tk.StringVar(value="")
        self.cont = controller

        title_frame = tk.Frame(self)
        back_button = tk.Button(title_frame, text="←", command=lambda: self.open_management_view())
        title_label = tk.Label(title_frame, textvariable=self.title)
        back_button.pack(side="left")
        title_label.pack(side="left", fill="x")
        title_frame.pack(side="top", fill="x", pady=5, padx=5)

        self.entity_details_frame = tk.Frame(self)
        self.entity_details_frame.pack(side="top", fill="both", expand=True, padx=20, pady=30)

    def set_mode(self, mode):
        self.mode = mode
        if mode == Views.STUDENT:
            def toggle_guardian():
                box_state = "normal"
                if not guardian_variable.get():
                    box_state = "disabled"
                guardian_name_entry['state'] = box_state
                guardian_name_entry['state'] = box_state
                guardian_surname_entry['state'] = box_state
                guardian_contact_entry['state'] = box_state

            guardian_variable = tk.BooleanVar(value=True)

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

            okul_no_entry = tk.Entry(self.entity_details_frame)
            okul_no_entry.insert(0, "0")
            name_entry = tk.Entry(self.entity_details_frame)
            surname_entry = tk.Entry(self.entity_details_frame)
            birth_date_calendar = Calendar(self.entity_details_frame)
            e_mail_entry = tk.Entry(self.entity_details_frame)
            guardian_cb = tk.Checkbutton(self.entity_details_frame, variable=guardian_variable, command=toggle_guardian)
            guardian_name_entry = tk.Entry(self.entity_details_frame)
            guardian_surname_entry = tk.Entry(self.entity_details_frame)
            guardian_contact_entry = tk.Entry(self.entity_details_frame)  # TODO: Add Mobile phone verification
            add_student_button = tk.Button(self.entity_details_frame, text="Öğrenci Ekle",
                                           command=self.add_entity_action)

            okul_no_label.grid(row=0, column=0, sticky="nsew", pady=3, padx=3)
            name_label.grid(row=1, column=0, sticky="nsew", pady=3, padx=3)
            surname_label.grid(row=2, column=0, sticky="nsew", pady=3, padx=3)
            birth_date_label.grid(row=3, column=0, sticky="nsew", pady=3, padx=3)
            e_mail_label.grid(row=4, column=0, sticky="nsew", pady=3, padx=3)
            guardian_label.grid(row=5, column=0, sticky="nsew", pady=3, padx=3)
            guardian_name.grid(row=6, column=0, sticky="nsew", pady=3, padx=3)
            guardian_surname.grid(row=7, column=0, sticky="nsew", pady=3, padx=3)
            guardian_contact.grid(row=8, column=0, sticky="nsew", pady=3, padx=3)

            okul_no_entry.grid(row=0, column=1, sticky="nsew", pady=3, padx=3)
            name_entry.grid(row=1, column=1, sticky="nsew", pady=3, padx=3)
            surname_entry.grid(row=2, column=1, sticky="nsew", pady=3, padx=3)
            birth_date_calendar.grid(row=3, column=1, sticky="nsew", pady=3, padx=3)
            e_mail_entry.grid(row=4, column=1, sticky="nsew", pady=3, padx=3)
            guardian_cb.grid(row=5, column=1, sticky="w", pady=3, padx=3)
            guardian_name_entry.grid(row=6, column=1, sticky="nsew", pady=3, padx=3)
            guardian_surname_entry.grid(row=7, column=1, sticky="nsew", pady=3, padx=3)
            guardian_contact_entry.grid(row=8, column=1, sticky="nsew", pady=3, padx=3)
            add_student_button.grid(row=9, column=0, columnspan=2, sticky="nsew", pady=3, padx=3)

            for i in range(9):
                self.entity_details_frame.rowconfigure(i, weight=1)

        elif mode == Views.EMPLOYEE:
            self.title.set("Çalışan Ekle")
            okul_no_label = tk.Label(self.entity_details_frame, text="Okul Numarası")
            name_label = tk.Label(self.entity_details_frame, text="Ad")
            surname_label = tk.Label(self.entity_details_frame, text="Soyad")
            birth_date_label = tk.Label(self.entity_details_frame, text="Doğum Tarihi")
            salary_label = tk.Label(self.entity_details_frame, text="Maaş")
            occupation_label = tk.Label(self.entity_details_frame, text="Meslek")

            okul_no_entry = tk.Entry(self.entity_details_frame)
            okul_no_entry.insert(0, "0")
            name_entry = tk.Entry(self.entity_details_frame)
            surname_entry = tk.Entry(self.entity_details_frame)
            birth_date_calendar = Calendar(self.entity_details_frame)
            e_mail_entry = tk.Entry(self.entity_details_frame)
            guardian_cb = tk.Checkbutton(self.entity_details_frame)
            guardian_name_entry = tk.Entry(self.entity_details_frame)
            guardian_surname_entry = tk.Entry(self.entity_details_frame)
            guardian_contact_entry = tk.Entry(self.entity_details_frame)  # TODO: Add Mobile phone verification
            add_student_button = tk.Button(self.entity_details_frame, text="Öğrenci Ekle")

            okul_no_label.grid(row=0, column=0, sticky="nsew")
            name_label.grid(row=1, column=0, sticky="nsew")
            surname_label.grid(row=2, column=0, sticky="nsew")
            birth_date_label.grid(row=3, column=0, sticky="nsew")
            e_mail_label.grid(row=4, column=0, sticky="nsew")
            guardian_label.grid(row=5, column=0, sticky="nsew")
            guardian_name.grid(row=6, column=0, sticky="nsew")
            guardian_surname.grid(row=7, column=0, sticky="nsew")
            guardian_contact.grid(row=8, column=0, sticky="nsew")

            okul_no_entry.grid(row=0, column=1, sticky="nsew")
            name_entry.grid(row=1, column=1, sticky="nsew")
            surname_entry.grid(row=2, column=1, sticky="nsew")
            birth_date_calendar.grid(row=3, column=1, sticky="nsew")
            e_mail_entry.grid(row=4, column=1, sticky="nsew")
            guardian_cb.grid(row=5, column=1, sticky="nsew")
            guardian_name_entry.grid(row=6, column=1, sticky="nsew")
            guardian_surname_entry.grid(row=7, column=1, sticky="nsew")
            guardian_contact_entry.grid(row=8, column=1, sticky="nsew")
            add_student_button.grid(row=9, column=0, columnspan=2, sticky="nsew")

            for i in range(9):
                self.entity_details_frame.rowconfigure(i, weight=1)

        elif mode == Views.ACTIVITY:
            pass

    def add_entity_action(self):
        # TODO: Do the sql commands to add the entity here
        # TODO: Add popup warning if checkbox failed
        self.open_management_view()

    def open_management_view(self):
        management_view = self.cont.get_frame(Views.SummaryView)
        management_view.set_mode(self.mode)
        self.cont.show_frame(Views.SummaryView)
