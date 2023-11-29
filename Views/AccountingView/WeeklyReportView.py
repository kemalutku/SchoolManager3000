import tkinter as tk
from tkinter import ttk
import Views
from datetime import datetime, timedelta
import calendar


class WeeklyReportView(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.mode = None
        self.title = tk.StringVar(value="Haftalık Rapor")
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
        self.report_week_dropdown = ttk.Combobox(button_frame, values=[str(i) for i in range(53)], state="readonly")
        self.report_week_dropdown.set("1")
        self.report_week_dropdown.pack(side="left")
        show_button = tk.Button(button_frame, text="Göster", command=self.show_weekly_report)
        show_button.pack(side="left")
        report_frame = tk.Frame(self)
        report_frame.pack(side="top", expand=True, fill="x")
        self.report_label = tk.Label(report_frame, text="")
        self.report_label.pack(side="top", expand=True, fill="x")

        monthly_report = tk.Button()

    def ww2d(self, year, work_week):
        # Create a datetime object for the first day of the year
        first_day_of_year = datetime(year, 1, 1)

        # Find the day of the week for the first day of the year
        day_of_week = first_day_of_year.weekday()

        # Calculate the date of the first Monday of the year
        # If the first day is not a Monday, we find the next Monday
        if day_of_week != calendar.MONDAY:
            first_monday = first_day_of_year + timedelta(days=(calendar.MONDAY - day_of_week))
        else:
            first_monday = first_day_of_year

        # Calculate the date for the Monday of the given work week
        # We subtract 1 from work_week since Python is 0-indexed
        date_of_work_week = first_monday + timedelta(weeks=work_week - 1)

        return date_of_work_week.date()

    def show_weekly_report(self):
        self.report_label.config(text="")
        target_week = int(self.report_week_dropdown.get())
        next_week = (target_week + 1) if target_week != 52 else 1
        query = ("SELECT "
                 "e.EXPENSE_NAME ,"
                 "e.AMOUNT, "
                 "e.EXPENSE_DATE FROM expense e  "
                 "WHERE "
                 "e.EXPENSE_DATE >= '{}' AND e.EXPENSE_DATE <'{}' "
                 "UNION  "
                 "SELECT "
                 "'TOPLAM HARCAMA', NULL, SUM(e.AMOUNT) "
                 "FROM expense e "
                 "WHERE e.EXPENSE_DATE >= '{}' AND e.EXPENSE_DATE <'{}';").format(self.ww2d(2023, target_week),
                                                                                  self.ww2d(2023, next_week),
                                                                                  self.ww2d(2023, target_week),
                                                                                  self.ww2d(2023, next_week))
        results = self.cont.sql_query(query)
        report_text = "TARİH \t\t\t\t KALEM \t\t\t\t HARCAMA \t\t\t\t\n"
        for result in results:
            report_text += "{} \t\t\t\t {} \t\t\t\t {} \t\t\t\t\n".format(result[0],result[1], result[2])
        self.report_label.config(text=report_text)
