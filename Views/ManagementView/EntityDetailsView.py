import tkinter as tk
import Views


class EntityDetailsView(tk.Frame):
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

        self.entity_frame = tk.Frame(self.entity_details_frame)
        self.courses_frame = tk.Frame(self.entity_details_frame)
        self.entity_frame.grid(row=0, column=0, sticky="nsew")
        self.courses_frame.grid(row=0, column=1, sticky="nsew")

        self.entity_details_frame.columnconfigure(0, weight=1)
        self.entity_details_frame.columnconfigure(1, weight=1)

    def set_mode(self, mode):
        self.mode = mode
        query_entity = self.get_entity_data()
        if mode == Views.STUDENT:
            okul_no_label = tk.Label(self.entity_frame, text="Okul Numarası")
            name_label = tk.Label(self.entity_frame, text="Ad")
            surname_label = tk.Label(self.entity_frame, text="Soyad")
            birth_date_label = tk.Label(self.entity_frame, text="Doğum Tarihi")
            e_mail_label = tk.Label(self.entity_frame, text="E-Mail")
            guardian_label = tk.Label(self.entity_frame, text="Veli")
            guardian_name = tk.Label(self.entity_frame, text="Veli Ad")
            guardian_surname = tk.Label(self.entity_frame, text="Veli Soyadı")
            guardian_contact = tk.Label(self.entity_frame, text="Veli İletişim")

            okul_no_label_value = tk.Label(self.entity_frame, text=query_entity['okul_no'])
            name_label_value = tk.Label(self.entity_frame, text=query_entity['ad'])
            surname_label_value = tk.Label(self.entity_frame, text=query_entity['soyad'])
            birth_date_label_value = tk.Label(self.entity_frame, text=query_entity['dogum_tarihi'])
            e_mail_label_value = tk.Label(self.entity_frame, text=query_entity['e-mail'])
            guardian_label_value = tk.Label(self.entity_frame, text=query_entity['veli'])
            guardian_name_value = tk.Label(self.entity_frame, text=query_entity['veli_ad'])
            guardian_surname_value = tk.Label(self.entity_frame, text=query_entity['veli_soyad'])
            guardian_contact_value = tk.Label(self.entity_frame, text=query_entity['veli_numara'])

            okul_no_label.grid(row=0, column=0, sticky="nsew", pady=3, padx=3)
            name_label.grid(row=1, column=0, sticky="nsew", pady=3, padx=3)
            surname_label.grid(row=2, column=0, sticky="nsew", pady=3, padx=3)
            birth_date_label.grid(row=3, column=0, sticky="nsew", pady=3, padx=3)
            e_mail_label.grid(row=4, column=0, sticky="nsew", pady=3, padx=3)
            guardian_label.grid(row=5, column=0, sticky="nsew", pady=3, padx=3)
            guardian_name.grid(row=6, column=0, sticky="nsew", pady=3, padx=3)
            guardian_surname.grid(row=7, column=0, sticky="nsew", pady=3, padx=3)
            guardian_contact.grid(row=8, column=0, sticky="nsew", pady=3, padx=3)

            okul_no_label_value.grid(row=0, column=1, sticky="nsew", pady=3, padx=3)
            name_label_value.grid(row=1, column=1, sticky="nsew", pady=3, padx=3)
            surname_label_value.grid(row=2, column=1, sticky="nsew", pady=3, padx=3)
            birth_date_label_value.grid(row=3, column=1, sticky="nsew", pady=3, padx=3)
            e_mail_label_value.grid(row=4, column=1, sticky="nsew", pady=3, padx=3)
            guardian_label_value.grid(row=5, column=1, sticky="nsew", pady=3, padx=3)
            guardian_name_value.grid(row=6, column=1, sticky="nsew", pady=3, padx=3)
            guardian_surname_value.grid(row=7, column=1, sticky="nsew", pady=3, padx=3)
            guardian_contact_value.grid(row=8, column=1, sticky="nsew", pady=3, padx=3)

        elif mode == Views.EMPLOYEE:
            pass
        elif mode == Views.ACTIVITY:
            pass

    def get_entity_data(self):
        # TODO: Send and parse the sql commands to get the entity details here
        default_entity = None
        if self.mode == Views.STUDENT:
            default_entity = {
                'okul_no': 0,
                'ad': 'Aylin',
                'soyad': 'Kaya',
                'dogum_tarihi': '01-01-2000',
                'yaş': 23,
                'e-mail': 'aylin.kaya@somewhere.edu.tr',
                'veli': 'Var',
                'veli_ad': 'Emirhan',
                'veli_soyad': 'Kaya',
                'veli_numara': '+905001234567'
            }
        return default_entity

    def open_management_view(self):
        management_view = self.cont.get_frame(Views.SummaryView)
        management_view.set_mode(self.mode)
        self.cont.show_frame(Views.SummaryView)
