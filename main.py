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
            if config.database_use_online:
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

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in [LoginScreenView, MainScreenView, SummaryView, AddEntityView, SyllabusView]:
            frame = F(container, self)
            self.frames[F] = frame
            # Grid configuration ensures frames are stacked on top of each other
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(LoginScreenView)

    def show_frame(self, cont):
        if cont is not None:
            frame = self.frames[cont]
            frame.tkraise()

    def get_frame(self, f):
        return self.frames.get(f)


if __name__ == "__main__":
    app = SchoolManager3000()
    app.mainloop()
