import tkinter as tk
from tkinter import ttk
import Views


class CommunicationView(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.mode = None
        self.title = tk.StringVar(value="İletişim")
        self.cont = controller

        title_frame = tk.Frame(self)
        back_button = tk.Button(title_frame, text="←", command=lambda: controller.show_frame(Views.MainScreenView))
        title_label = tk.Label(title_frame, textvariable=self.title)
        back_button.pack(side="left")
        title_label.pack(side="left", fill="x")
        title_frame.pack(side="top", fill="x", pady=5, padx=5)

        contacts_frame = tk.Frame(self)
        contacts_frame.columnconfigure(1, weight=1)
        contacts_frame.rowconfigure(0, weight=1)

        filter_frame = tk.Frame(contacts_frame)
        age_label = tk.Label(filter_frame, text="Yaş")
        age_label.grid(row=0, column=0, padx=2)
        self.age_entry_l = tk.Entry(filter_frame, width=5)
        self.age_entry_l.grid(row=0, column=1, padx=2)
        sep_label = tk.Label(filter_frame, text="-")
        sep_label.grid(row=0, column=2, padx=2)
        self.age_entry_u = tk.Entry(filter_frame, width=5)
        self.age_entry_u.grid(row=0, column=3, padx=2)

        ders_label = tk.Label(filter_frame, text="Alınan Ders")
        ders_label.grid(row=1, column=0, pady=10, columnspan=4)
        self.ders_dropdown = ttk.Combobox(filter_frame)
        self.ders_dropdown.grid(row=2, column=0, columnspan=4)

        filter_button = tk.Button(filter_frame, text="Filtrele", command=self.filter_command)
        filter_button.grid(row=5, column=0, columnspan=4, sticky="s")
        filter_frame.rowconfigure(5, weight=1)
        filter_frame.grid(row=0, column=0, padx=5, sticky="nsew", pady= [20,0])

        self.tree_view = ttk.Treeview(contacts_frame)
        self.configure_tree_view()
        self.tree_view.grid(row=0, column=1, sticky="nsew")

        action_frame = tk.Frame(contacts_frame)
        send_sms_button = tk.Button(action_frame, text="SMS Gönder", width=15, height=5,
                                    command=self.send_sms_command)
        send_sms_button.grid(row=0, column=0, padx=10, pady=10)
        send_email_button = tk.Button(action_frame, text="E-Posta Gönder", width=15, height=5,
                                      command=self.send_email_command)
        send_email_button.grid(row=1, column=0, padx=10, pady=10)
        action_frame.grid(row=0, column=2, sticky="nsew")

        contacts_frame.pack(side="top", expand=True, fill="both", padx=10, pady=10)

    def send_sms_command(self):
        popup = tk.Toplevel(self)
        popup.title("SMS Gönder")

        # Set the size of the popup window
        popup_width = 300
        popup_height = 200
        popup.geometry(f"{popup_width}x{popup_height}")
        popup.resizable(False, False)

        # Calculate position x and y coordinates
        x_left = self.winfo_x()
        y_top = self.winfo_y()
        root_width = self.winfo_width()
        root_height = self.winfo_height()
        x_center = x_left + (root_width - popup_width) // 2
        y_center = y_top + (root_height - popup_height) // 2

        popup.geometry(f"+{x_center}+{y_center}")

        tk.Label(popup, text="SMS İçeriği:").pack(pady=20,side="top")
        tk.Entry(popup).pack(fill="both", side="top", padx=10,expand=True)
        tk.Label(popup, text="Yukarıdaki SMS'i göndermek için GÖNDER'e tıklayın.").pack(pady=20)
        button_frame = tk.Frame(popup)
        button_frame.pack(pady=20, side="top")
        send_button = tk.Button(button_frame, text="Gönder", command=popup.destroy)
        send_button.pack(side="left", padx=10)
        cancel_button = tk.Button(button_frame, text="İptal", command=popup.destroy)
        cancel_button.pack(side="left", padx=10)

    def send_email_command(self):
        popup = tk.Toplevel(self)
        popup.title("E-Posta Gönder")

        # Set the size of the popup window
        popup_width = 300
        popup_height = 200
        popup.geometry(f"{popup_width}x{popup_height}")

        # Calculate position x and y coordinates
        x_left = self.winfo_x()
        y_top = self.winfo_y()
        root_width = self.winfo_width()
        root_height = self.winfo_height()
        x_center = x_left + (root_width - popup_width) // 2
        y_center = y_top + (root_height - popup_height) // 2

        popup.geometry(f"+{x_center}+{y_center}")

        tk.Label(popup, text="E-Posta İçeriği:").pack(pady=20, side="top")
        tk.Entry(popup).pack(fill="both", side="top", padx=5)
        tk.Label(popup, text="Yukarıdaki E-Posta'yı göndermek için GÖNDER'e tıklayın.").pack(pady=20)
        button_frame = tk.Frame(popup)
        button_frame.pack(pady=20, side="top")
        send_button = tk.Button(button_frame, text="Gönder", command=popup.destroy)
        send_button.pack(side="left", padx=10)
        cancel_button = tk.Button(button_frame, text="İptal", command=popup.destroy)
        cancel_button.pack(side="left", padx=10)

    def filter_command(self):
        pass

    def configure_tree_view(self):
        self.title.set("Öğrenciler")
        self.tree_view['columns'] = ('secim', 'okul_num', 'ad', 'soyad', 'yas', 'telefon', 'e-posta')

        self.tree_view.column('#0', width=0, stretch=tk.NO)
        self.tree_view.column("secim", width=25)
        self.tree_view.column("okul_num", width=150)
        self.tree_view.column("ad", width=150)
        self.tree_view.column("soyad", width=150)
        self.tree_view.column("yas", width=150)
        self.tree_view.column("telefon", width=150)
        self.tree_view.column("e-posta", width=150)

        self.tree_view.heading("secim", text=" ")
        self.tree_view.heading("okul_num", text="Okul Numarası")
        self.tree_view.heading("ad", text="Ad")
        self.tree_view.heading("soyad", text="Soyad")
        self.tree_view.heading("yas", text="Yaş")
        self.tree_view.heading("telefon", text="Telefon")
        self.tree_view.heading("e-posta", text="E-Posta")