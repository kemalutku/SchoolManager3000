import tkinter as tk
import Views

WEEK_MAPPING = {
    "MONDAY": 0,
    "TUESDAY": 1,
    "WEDNESDAY": 2,
    "THURSDAY": 3,
    "FRIDAY": 4,
    "SATURDAY": 5,
    "SUNDAY": 6
}


class SyllabusView(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.mode = None
        self.entry_data = None
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
                label = tk.Label(self.syllabus_frame, text="", relief="groove", borderwidth=1)
                label.grid(row=j + 1, column=i + 1, sticky="nsew")
                self.labels.append(label)

    def set_mode(self, mode):
        self.mode = mode
        self.get_data()

    def set_data(self, values):
        for hour, day in values:
            day_value = WEEK_MAPPING[day]
            hour_value = int(str(hour)[:2]) - 9
            target_box = 12 * day_value + hour_value
            target_label = self.labels[target_box]
            target_label.configure(bg="blue")

    def get_data(self):
        if self.mode == Views.STUDENT:
            pass
        elif self.mode == Views.EMPLOYEE:
            pass
        elif self.mode == Views.ACTIVITY:
            QUERY = ("SELECT sh.start_hour, sh.day_of_week "
                     "FROM course c "
                     "LEFT JOIN course_section cs ON c.id = cs.course_id "
                     "LEFT JOIN section_hours sh ON sh.sec_id = cs.id "
                     "WHERE c.id={}").format(self.entry_data)
            result = self.cont.sql_query(QUERY)
            if result:
                self.set_data(result)

    def open_management_view(self):
        management_view = self.cont.get_frame(Views.SummaryView)
        management_view.set_mode(self.mode)
        self.cont.show_frame(Views.SummaryView)
