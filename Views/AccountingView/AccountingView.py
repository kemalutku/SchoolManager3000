import tkinter as tk
from tkinter import ttk
import Views


class AccountingHomeView(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.mode = None
        self.title = tk.StringVar(value="Muhasebe")
        self.preload_func = None
        self.cont = controller

        title_frame = tk.Frame(self)
        back_button = tk.Button(title_frame, text="←", command=lambda: controller.show_frame(Views.MainScreenView))
        title_label = tk.Label(title_frame, textvariable=self.title)
        back_button.pack(side="left")
        title_label.pack(side="left", fill="x")
        title_frame.pack(side="top", fill="x", pady=5, padx=5)

        buttons_frame = tk.Frame(self)
        buttons_frame.columnconfigure(0,weight=1)

        monthly_report_button = tk.Button(buttons_frame, text="Aylık Rapor", height=5, width=30)
        monthly_report_button.grid(row=0, column=0, pady=[30, 10], padx=20, sticky="w")
        weekly_report_button = tk.Button(buttons_frame, text="Haftalık Rapor", height=5, width=30)
        weekly_report_button.grid(row=1, column=0, pady=10, padx=20, sticky="w")
        inventory_tracker_button = tk.Button(buttons_frame, text="Stok Takibi", height=5, width=30)
        inventory_tracker_button.grid(row=2, column=0, pady=10, padx=20, sticky="w")

        buttons_frame.pack(side="top", expand=True, fill="both")

        monthly_report = tk.Button()