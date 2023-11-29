import tkinter as tk
from tkinter import ttk
import Views
from datetime import datetime, timedelta
import calendar

months = ["Ocak", "Şubat", "Mart", "Nisan", "Mayıs", "Haziran",
          "Temmuz", "Ağustos", "Eylül", "Ekim", "Kasım", "Aralık"]


class MonthlyReportView(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.mode = None
        self.title = tk.StringVar(value="Aylık Rapor")
        self.preload_func = None
        self.cont = controller

        title_frame = tk.Frame(self)
        back_button = tk.Button(title_frame, text="←", command=lambda: controller.show_frame(Views.MainScreenView))
        title_label = tk.Label(title_frame, textvariable=self.title)
        back_button.pack(side="left")
        title_label.pack(side="left", fill="x")
        title_frame.pack(side="top", fill="x", pady=5, padx=5)

        content_frame = tk.Frame(self)
        content_frame.pack(side="top", expand=True, fill="both")
        content_frame.columnconfigure(0, weight=1)

        button_frame = tk.Frame(content_frame)
        button_frame.pack(side="top", fill='x')

        tk.Label(button_frame, text="Rapor Haftası: ").pack(side="left")
        self.report_month_dropdown = ttk.Combobox(button_frame, values=months, state="readonly")
        self.report_month_dropdown.set("Ocak")
        self.report_month_dropdown.pack(side="left")
        self.report_year_dropdown = ttk.Combobox(button_frame, values=[str(i) for i in range(2000, 2024)],
                                                 state="readonly")
        self.report_year_dropdown.set("2023")
        self.report_year_dropdown.pack(side="left")
        show_button = tk.Button(button_frame, text="Göster", command=self.show_weekly_report)
        show_button.pack(side="left")
        report_frame = tk.Frame(self)
        report_frame.pack(side="top", expand=True, fill="x")
        self.report_label = tk.Label(report_frame, text="")
        self.report_label.pack(side="top", expand=True, fill="x")

        monthly_report = tk.Button()

    def date_string(self, year, month):
        year = str(year)
        month = str(month).zfill(2)
        return "{}-{}-01".format(year, month)

    def show_weekly_report(self):
        self.report_label.config(text="")
        target_year = int(self.report_year_dropdown.get())
        target_month = int(months.index(self.report_month_dropdown.get()) + 1)
        date_str = self.date_string(target_year, target_month)
        next_str = self.date_string(target_year, target_month + 1 if target_month != 'Aralık' else 1)

        query = (
            "SELECT "
            "e.EXPENSE_NAME ,e.AMOUNT, e.EXPENSE_DATE "
            "FROM expense e "
            "WHERE e.EXPENSE_DATE >= '{}' AND e.EXPENSE_DATE < '{}' "
            "UNION  "
            "SELECT 'Toplam MAAŞ' , SUM(ee.SALARY) , NULL "
            "FROM employee ee "
            "UNION "
            "SELECT 'TOPLAM HARCAMA', SUM(e.AMOUNT), NULL  "
            "FROM expense e  "
            "WHERE e.EXPENSE_DATE >= '{}' AND e.EXPENSE_DATE < '{}';").format(date_str, next_str, date_str,
                                                                             next_str, )

        results = self.cont.sql_query(query)
        report_text = "KALEM \t\t\t\t HARCAMA \t\t\t\t TARİH \t\t\t\t\n"
        for result in results:
            report_text += "{} \t\t\t\t {} \t\t\t\t {} \t\t\t\t\n".format(result[0], result[1], result[2])
        self.report_label.config(text=report_text)
