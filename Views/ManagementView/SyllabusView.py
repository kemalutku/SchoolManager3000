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
        self.preload_func = None
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
        for label in self.labels:
            try:
                label.configure(bg='systemWindowBackgroundColor')
            except:
                label.configure(bg='white')
            label.config(text="")

        for name, hour, day in values:
            if day is not None:
                day_value = WEEK_MAPPING[day]
                try:
                    hour_value = int(str(hour)[:2]) - 8
                except ValueError:
                    hour_value = int(str(hour)[:1]) - 8
                target_box = 12 * day_value + hour_value
                target_label = self.labels[target_box]
                target_label.config(text=name)
                target_label.configure(bg="lightblue")

    def get_data(self):
        if self.mode == Views.STUDENT:
            QUERY = (
                '(SELECT '
                'c.COURSE_NAME, '
                'sh.START_HOUR , '
                'sh.DAY_OF_WEEK FROM student s '
                'LEFT OUTER JOIN  student_section ss ON s.ID = ss.STUDENT_ID '
                'LEFT OUTER JOIN course_section cs ON cs.ID = ss.SECTION_ID '
                'LEFT OUTER JOIN course c ON c.ID = cs.COURSE_ID '
                'LEFT OUTER JOIN section_hours sh ON cs.ID = sh.SEC_ID '
                'WHERE s.ID = "{}")'
                'UNION'
                '( SELECT '
                'sa.ACTIVITY_NAME, '
                'sa.START_HOUR, '
                'sa.DAY_OF_WEEK '
                'FROM student s '
                'LEFT JOIN student_activities sa ON sa.STUDENT_ID = s.ID '
                'WHERE s.ID = "{}" )').format(
                self.entry_data, self.entry_data)
        elif self.mode == Views.EMPLOYEE:
            QUERY= ("SELECT  "
                    "c.COURSE_NAME, sh.START_HOUR ,sh.DAY_OF_WEEK "
                    "FROM employee e LEFT JOIN teacher t ON t.EMP_ID = e.ID "
                    "LEFT JOIN course_section cs ON cs.TEACHER_ID = t.ID "
                    "LEFT JOIN section_hours sh ON sh.SEC_ID = cs.ID "
                    "LEFT JOIN course c ON c.ID =cs.COURSE_ID "
                    "WHERE e.ID = {} "
                    "UNION "
                    "SELECT ea.ACTIVITY_NAME , ea.START_HOUR  , ea.DAY_OF_WEEK "
                    "FROM employee e "
                    "LEFT JOIN employee_activities ea ON e.ID =ea.EMP_ID "
                    "WHERE e.ID ={};").format(self.entry_data, self.entry_data)
        elif self.mode == Views.ACTIVITY:
            QUERY = ("SELECT c.course_name, sh.start_hour, sh.day_of_week "
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
