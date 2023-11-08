import tkinter as tk
import Views


class SyllabusView(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.mode = None
        self.title = tk.StringVar(value="")
        self.cont = controller
        self.labels = []

        title_frame = tk.Frame(self)
        back_button = tk.Button(title_frame, text="←", command=lambda: self.open_management_view())
        title_label = tk.Label(title_frame, textvariable=self.title)
        back_button.pack(side="left")
        title_label.pack(side="left", fill="x")
        title_frame.pack(side="top", fill="x", pady=5, padx=5)

        self.syllabus_frame = tk.Frame(self)
        self.create_syllabus_template()
        self.syllabus_frame.pack(side="top", fill="both", expand=True, padx=10, pady=10)

    def create_syllabus_template(self):
        self.syllabus_frame.columnconfigure(0, weight=1)
        for i, d in enumerate(["Pazartesi", "Salı", "Çarşamba", "Perşembe", "Cuma", "Cumartesi", "Pazar"]):
            self.syllabus_frame.columnconfigure(i + 1, weight=1)
            label = tk.Label(self.syllabus_frame, text=d, relief="groove", borderwidth=1, bg="lightgray")
            label.grid(row=0, column=i + 1, sticky="nsew")

        self.syllabus_frame.rowconfigure(0, weight=1)
        for i in range(12):
            self.syllabus_frame.rowconfigure(i + 1, weight=1)
            label = tk.Label(self.syllabus_frame, text="{}:30 -\n{}:20".format(i + 8, i + 9),
                             relief="groove", borderwidth=1, bg="lightgray")
            label.grid(row=i + 1, column=0, sticky="nsew")

        for i in range(7):
            for j in range(12):
                label = tk.Label(self.syllabus_frame,text="", relief="groove", borderwidth=1)
                label.grid(row=j+1, column=i+1, sticky="nsew")
                self.labels.append(label)

    def set_mode(self, mode):
        self.mode = mode

    def set_data(self, name, hours):
        pass

    def open_management_view(self):
        management_view = self.cont.get_frame(Views.SummaryView)
        management_view.set_mode(self.mode)
        self.cont.show_frame(Views.SummaryView)
