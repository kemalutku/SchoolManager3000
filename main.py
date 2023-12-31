from Views import *

from Utils.fake_db import FakeDB
import mysql.connector
import tkinter as tk
import config


class SchoolManager3000(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title("Okul Yönetim Sistemi")

        self.geometry(config.resolution)
        self.resizable(False, False)

        try:
            if not config.use_mockup_database:
                self.school_db = mysql.connector.connect(
                    host=config.database_ip,
                    user=config.database_user,
                    password=config.database_password
                )
            else:
                self.school_db = FakeDB()
        except mysql.connector.errors.DatabaseError:
            print("Connecting to online host failed. Switching to local host")
            self.school_db = FakeDB()

        self.cursor = self.school_db.cursor()
        self.cursor.execute("use Bil071")
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in [LoginScreenView, MainScreenView,
                  SummaryView, AddEntityView, SyllabusView, AddRemoveRelationView, EntityDetailsView,
                  InventoryView, ModifyInventoryView, AddInventoryView,
                  AccountingHomeView, ReportView, MonthlyReportView, WeeklyReportView,
                  CommunicationView
                  ]:
            frame = F(container, self)
            self.frames[F] = frame
            # Grid configuration ensures frames are stacked on top of each other
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(LoginScreenView)

    def show_frame(self, cont):
        if cont is not None:
            frame = self.frames[cont]
            if frame.preload_func:
                frame.preload_func()
            frame.tkraise()

    def get_frame(self, f):
        return self.frames.get(f)

    def sql_query(self, q):
        self.cursor.execute(q)
        result = self.cursor.fetchall()
        return result

    def commit(self):
        try:
            self.school_db.commit()
            return True
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            self.school_db.rollback()
            return False
        finally:
            # Make sure to fetch any remaining results
            while self.school_db.next_result():
                pass


if __name__ == "__main__":
    app = SchoolManager3000()
    app.mainloop()
