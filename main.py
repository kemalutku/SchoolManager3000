from Views import LoginScreenView, MainScreenView

import mysql.connector
import tkinter as tk
import config


class SchoolManager3000(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)

        self.geometry(config.resolution)
        self.resizable(False, False)

        self.school_db = mysql.connector.connect(
            host=config.database_ip,
            user=config.database_user,
            password=config.database_password
        )

        self.cursor = self.school_db.cursor()

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in [LoginScreenView, MainScreenView]:
            frame = F(container, self)
            self.frames[F] = frame
            # Grid configuration ensures frames are stacked on top of each other
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(LoginScreenView)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()



app = SchoolManager3000()
app.mainloop()




