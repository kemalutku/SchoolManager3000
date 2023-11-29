import tkinter as tk
from tkinter import ttk
import Views


class AddRemoveRelationView(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.rm_activity_dropdown = None
        self.activity_day = None
        self.add_activity_dropdown = None
        self.add_course_dropdown = None
        self.rm_course_dropdown = None
        self.mode = None
        self.entry_data = None
        self.title = tk.StringVar(value="Ders Ekle/Sil")
        self.preload_func = None
        self.cont = controller
        self.activity_entries = []

        title_frame = tk.Frame(self)
        back_button = tk.Button(title_frame, text="←", command=lambda: self.open_management_view())
        title_label = tk.Label(title_frame, textvariable=self.title)
        back_button.pack(side="left")
        title_label.pack(side="left", fill="x")
        title_frame.pack(side="top", fill="x", pady=5, padx=5)

        self.add_remove_frame = tk.Frame(self)
        self.add_remove_frame.pack(side="top", fill="both", expand=True)
        self.add_relation_frame = tk.Frame(self.add_remove_frame)
        self.add_relation_frame.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")
        self.remove_relation_frame = tk.Frame(self.add_remove_frame)
        self.remove_relation_frame.grid(row=0, column=1, padx=20, pady=20, sticky="nsew")

        self.add_remove_frame.columnconfigure(0, weight=1)
        self.add_remove_frame.columnconfigure(1, weight=1)
        self.add_relation_frame.columnconfigure(0, weight=1)
        self.add_relation_frame.columnconfigure(1, weight=1)
        self.remove_relation_frame.columnconfigure(0, weight=1)
        self.remove_relation_frame.columnconfigure(1, weight=1)

    def set_mode(self, mode):
        self.mode = mode
        if mode == Views.STUDENT or mode == Views.EMPLOYEE:

            tk.Label(self.add_relation_frame, text="DERS EKLE").grid(row=0, column=0, sticky="we", padx=20, pady=20,
                                                                     columnspan=2)
            tk.Label(self.add_relation_frame, text="Öğrenci Numarası").grid(row=1, column=0, sticky="w")
            tk.Label(self.add_relation_frame, text="Ad").grid(row=2, column=0, sticky="w")
            tk.Label(self.add_relation_frame, text="Soyad").grid(row=3, column=0, sticky="w")
            tk.Label(self.add_relation_frame, text="Ders").grid(row=4, column=0, sticky="w")

            tk.Label(self.add_relation_frame, text="").grid(row=1, column=1, sticky="w")
            tk.Label(self.add_relation_frame, text="").grid(row=2, column=1, sticky="w")
            tk.Label(self.add_relation_frame, text="").grid(row=3, column=1, sticky="w")

            self.add_course_dropdown = ttk.Combobox(self.add_relation_frame)
            self.add_course_dropdown.grid(row=4, column=1, sticky="w")
            add_course_names_query = "SELECT c.COURSE_NAME FROM course c WHERE c.ID NOT IN (SELECT cs.COURSE_ID" \
                                     " FROM student_section ss JOIN course_section cs ON ss.SECTION_ID = cs.ID" \
                                     " WHERE ss.STUDENT_ID = {}) ORDER BY c.COURSE_NAME;".format(self.entry_data)
            add_course_names = [row[0] for row in self.cont.sql_query(add_course_names_query)]
            self.add_course_dropdown['values'] = add_course_names

            student_id = self.entry_data
            student_id_entry = tk.Entry(self.add_relation_frame)
            student_id_entry.insert(0, str(student_id))
            student_id_entry['state'] = 'disabled'
            student_id_entry.grid(row=1, column=1, sticky="w")

            sname_query = "SELECT s.FIRST_NAME, s.LAST_NAME " \
                          "FROM student s WHERE s.ID = {}".format(self.entry_data)
            sname = self.cont.sql_query(sname_query)

            add_student_name_entry = tk.Entry(self.add_relation_frame)
            add_student_name_entry.insert(0, str(sname[0][0]))
            add_student_name_entry['state'] = 'disabled'
            add_student_name_entry.grid(row=2, column=1, sticky="w")
            add_student_surname_entry = tk.Entry(self.add_relation_frame)
            add_student_surname_entry.insert(0, str(sname[0][1]))
            add_student_surname_entry['state'] = 'disabled'
            add_student_surname_entry.grid(row=3, column=1, sticky="w")

            add_relation_button = tk.Button(self.add_relation_frame, text="Ders Ekle",
                                            command=self.add_relation_action)
            add_relation_button.grid(row=5, column=0, columnspan=2, sticky="we")

            #########################################################################

            tk.Label(self.add_relation_frame, text="AKTİVİTE EKLE").grid(row=6, column=0, sticky="we", padx=20, pady=20,
                                                                         columnspan=2)
            tk.Label(self.add_relation_frame, text="Öğrenci Numarası").grid(row=7, column=0, sticky="w")
            tk.Label(self.add_relation_frame, text="Ad").grid(row=8, column=0, sticky="w")
            tk.Label(self.add_relation_frame, text="Soyad").grid(row=9, column=0, sticky="w")
            tk.Label(self.add_relation_frame, text="Aktivite").grid(row=10, column=0, sticky="w")
            tk.Label(self.add_relation_frame, text="Gün").grid(row=11, column=0, sticky="w")
            tk.Label(self.add_relation_frame, text="Saat(hh:mm:ss)").grid(row=12, column=0, sticky="w")

            tk.Label(self.add_relation_frame, text="").grid(row=7, column=1, sticky="w")
            tk.Label(self.add_relation_frame, text="").grid(row=8, column=1, sticky="w")
            tk.Label(self.add_relation_frame, text="").grid(row=9, column=1, sticky="w")

            a_student_id = self.entry_data
            a_student_id_entry = tk.Entry(self.add_relation_frame)
            a_student_id_entry.insert(0, str(a_student_id))
            a_student_id_entry['state'] = 'disabled'
            a_student_id_entry.grid(row=7, column=1, sticky="w")

            sname_query = "SELECT s.FIRST_NAME, s.LAST_NAME " \
                          "FROM student s WHERE s.ID = {}".format(self.entry_data)
            sname = self.cont.sql_query(sname_query)

            a_add_student_name_entry = tk.Entry(self.add_relation_frame)
            a_add_student_name_entry.insert(0, str(sname[0][0]))
            a_add_student_name_entry['state'] = 'disabled'
            a_add_student_name_entry.grid(row=8, column=1, sticky="w")
            a_add_student_surname_entry = tk.Entry(self.add_relation_frame)
            a_add_student_surname_entry.insert(0, str(sname[0][1]))
            a_add_student_surname_entry['state'] = 'disabled'
            a_add_student_surname_entry.grid(row=9, column=1, sticky="w")
            activity_name = tk.Entry(self.add_relation_frame)
            activity_name.grid(row=10, column=1, sticky="w")
            days_of_week = ["MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY", "SATURDAY", "SUNDAY"]
            self.activity_day = ttk.Combobox(self.add_relation_frame, values=days_of_week)
            self.activity_day.grid(row=11, column=1, sticky="w")
            activity_time = tk.Entry(self.add_relation_frame)
            activity_time.grid(row=12, column=1, sticky="w")
            self.activity_entries.append(activity_time)
            self.activity_entries.append(activity_name)

            add_activity_button = tk.Button(self.add_relation_frame, text="Aktivite Ekle",
                                            command=self.add_activity_action)
            add_activity_button.grid(row=13, column=0, columnspan=2, sticky="we")

            # **********************************************************************

            tk.Label(self.remove_relation_frame, text="AKTİVİTE SİL").grid(row=6, column=0, sticky="we", padx=20,
                                                                           pady=20,
                                                                           columnspan=2)
            tk.Label(self.remove_relation_frame, text="Öğrenci Numarası").grid(row=7, column=0, sticky="w")
            tk.Label(self.remove_relation_frame, text="Ad").grid(row=8, column=0, sticky="w")
            tk.Label(self.remove_relation_frame, text="Soyad").grid(row=9, column=0, sticky="w")
            tk.Label(self.remove_relation_frame, text="Aktivite").grid(row=10, column=0, sticky="w")

            tk.Label(self.remove_relation_frame, text="").grid(row=7, column=1, sticky="w")
            tk.Label(self.remove_relation_frame, text="").grid(row=8, column=1, sticky="w")
            tk.Label(self.remove_relation_frame, text="").grid(row=9, column=1, sticky="w")
            self.rm_activity_dropdown = ttk.Combobox(self.remove_relation_frame)
            self.rm_activity_dropdown.grid(row=10, column=1, sticky="w")
            rm_activity_names_query = "SELECT DISTINCT ACTIVITY_NAME FROM" \
                                      " student_activities WHERE " \
                                      "STUDENT_ID = {};".format(self.entry_data)
            rm_activity_names = [row[0] for row in self.cont.sql_query(rm_activity_names_query)]
            self.rm_activity_dropdown['values'] = rm_activity_names

            rm_act_student_id_entry = tk.Entry(self.remove_relation_frame)
            rm_act_student_id_entry.insert(0, str(self.entry_data))
            rm_act_student_id_entry['state'] = 'disabled'
            rm_act_student_id_entry.grid(row=7, column=1, sticky="w")

            sname_query = "SELECT s.FIRST_NAME, s.LAST_NAME " \
                          "FROM student s WHERE s.ID = {}".format(self.entry_data)
            sname = self.cont.sql_query(sname_query)

            rm_act_student_name_entry = tk.Entry(self.remove_relation_frame)
            rm_act_student_name_entry.insert(0, str(sname[0][0]))
            rm_act_student_name_entry['state'] = 'disabled'
            rm_act_student_name_entry.grid(row=8, column=1, sticky="w")
            rm_act_student_surname_entry = tk.Entry(self.remove_relation_frame)
            rm_act_student_surname_entry.insert(0, str(sname[0][1]))
            rm_act_student_surname_entry['state'] = 'disabled'
            rm_act_student_surname_entry.grid(row=9, column=1, sticky="w")

            remove_act_relation_button = tk.Button(self.remove_relation_frame, text="Aktivite Sil",
                                                   command=self.rm_activity_action)
            remove_act_relation_button.grid(row=11, column=0, columnspan=2, sticky="we")

            # **********************************************************************

            #########################################################################
            tk.Label(self.remove_relation_frame, text="DERS SİL").grid(row=0, column=0, sticky="we", padx=20, pady=20,
                                                                       columnspan=2)
            tk.Label(self.remove_relation_frame, text="Öğrenci Numarası").grid(row=1, column=0, sticky="w")
            tk.Label(self.remove_relation_frame, text="Ad").grid(row=2, column=0, sticky="w")
            tk.Label(self.remove_relation_frame, text="Soyad").grid(row=3, column=0, sticky="w")
            tk.Label(self.remove_relation_frame, text="Ders").grid(row=4, column=0, sticky="w")

            tk.Label(self.remove_relation_frame, text="").grid(row=1, column=1, sticky="w")
            tk.Label(self.remove_relation_frame, text="").grid(row=2, column=1, sticky="w")
            tk.Label(self.remove_relation_frame, text="").grid(row=3, column=1, sticky="w")
            self.rm_course_dropdown = ttk.Combobox(self.remove_relation_frame)
            self.rm_course_dropdown.grid(row=4, column=1, sticky="w")
            rm_course_names_query = "SELECT c.COURSE_NAME FROM course c JOIN course_section cs ON c.ID = cs.COURSE_ID" \
                                    " JOIN student_section ss ON cs.ID = ss.SECTION_ID" \
                                    " WHERE ss.STUDENT_ID = {};".format(self.entry_data)
            rm_course_names = [row[0] for row in self.cont.sql_query(rm_course_names_query)]
            self.rm_course_dropdown['values'] = rm_course_names

            student_id_entry = tk.Entry(self.remove_relation_frame)
            student_id_entry.insert(0, str(self.entry_data))
            student_id_entry['state'] = 'disabled'
            student_id_entry.grid(row=1, column=1, sticky="w")

            sname_query = "SELECT s.FIRST_NAME, s.LAST_NAME " \
                          "FROM student s WHERE s.ID = {}".format(self.entry_data)
            sname = self.cont.sql_query(sname_query)

            rm_student_name_entry = tk.Entry(self.remove_relation_frame)
            rm_student_name_entry.insert(0, str(sname[0][0]))
            rm_student_name_entry['state'] = 'disabled'
            rm_student_name_entry.grid(row=2, column=1, sticky="w")
            rm_student_surname_entry = tk.Entry(self.remove_relation_frame)
            rm_student_surname_entry.insert(0, str(sname[0][1]))
            rm_student_surname_entry['state'] = 'disabled'
            rm_student_surname_entry.grid(row=3, column=1, sticky="w")

            remove_relation_button = tk.Button(self.remove_relation_frame, text="Ders Sil",
                                               command=self.rm_relation_action)
            remove_relation_button.grid(row=5, column=0, columnspan=2, sticky="we")

        elif mode == Views.ACTIVITY:
            pass

    def open_management_view(self):
        management_view = self.cont.get_frame(Views.SummaryView)
        management_view.set_mode(self.mode)
        self.cont.show_frame(Views.SummaryView)

    def add_relation_action(self):
        selected_course = self.add_course_dropdown.get()
        student_id = self.entry_data
        set_id = "SET @StudentID = {};".format(student_id)
        set_course = "SET @CourseName = '{}';".format(selected_course)
        add_query = "INSERT INTO student_section (STUDENT_ID, SECTION_ID) " \
                    "VALUES (@StudentID, (SELECT ID FROM course_section " \
                    "WHERE COURSE_ID = (SELECT ID FROM course WHERE COURSE_NAME = @CourseName)));"
        add_course_query = [set_id, set_course, add_query]

        for query in add_course_query:
            self.cont.sql_query(query)
            self.cont.commit()

        commit_result = self.cont.commit
        if commit_result:
            self.add_course_commit_success_popup()
        else:
            self.add_course_commit_fail_popup()

    def rm_relation_action(self):
        selected_course = self.rm_course_dropdown.get()
        student_id = self.entry_data
        set_id = "SET @StudentID = {};".format(student_id)
        set_course = "SET @CourseName = '{}';".format(selected_course)
        rm_query = "DELETE FROM student_section WHERE STUDENT_ID = @StudentID AND SECTION_ID IN " \
                   "(SELECT ID FROM course_section WHERE COURSE_ID = (SELECT ID FROM course " \
                   "WHERE COURSE_NAME = @CourseName));"
        rm_course_query = [set_id, set_course, rm_query]
        for query in rm_course_query:
            self.cont.sql_query(query)
            self.cont.commit()
        commit_result = self.cont.commit
        if commit_result:
            self.add_course_commit_success_popup()
        else:
            self.add_course_commit_fail_popup()

    def add_course_commit_fail_popup(self):
        popup = tk.Toplevel(self)
        popup.title("Başarısız!")
        popup_width = 300
        popup_height = 100
        popup.geometry(f"{popup_width}x{popup_height}")

        # Calculate position x and y coordinates
        x_left = self.winfo_x()
        y_top = self.winfo_y()
        root_width = self.winfo_width()
        root_height = self.winfo_height()
        x_center = x_left + (root_width - popup_width) // 2
        y_center = y_top + (root_height - popup_height) // 2

        popup.geometry(f"+{x_center}+{y_center}")

        tk.Label(popup, text="Başarısız. Lütfen girdiğiniz alanları ve internet bağlantısınızı kontrol edin!",
                 wraplength=200).pack(pady=20, side="top")

    def add_course_commit_success_popup(self):
        popup = tk.Toplevel(self)
        popup.title("Başarılı!")
        popup_width = 300
        popup_height = 100
        popup.geometry(f"{popup_width}x{popup_height}")

        # Calculate position x and y coordinates
        x_left = self.winfo_x()
        y_top = self.winfo_y()
        root_width = self.winfo_width()
        root_height = self.winfo_height()
        x_center = x_left + (root_width - popup_width) // 2
        y_center = y_top + (root_height - popup_height) // 2

        popup.geometry(f"+{x_center}+{y_center}")

        tk.Label(popup, text="Başarılı!",
                 wraplength=200).pack(pady=20, side="top")

    def cakisma_popup(self):
        popup = tk.Toplevel(self)
        popup.title("Çakışma Var!")
        popup_width = 300
        popup_height = 100
        popup.geometry(f"{popup_width}x{popup_height}")

        # Calculate position x and y coordinates
        x_left = self.winfo_x()
        y_top = self.winfo_y()
        root_width = self.winfo_width()
        root_height = self.winfo_height()
        x_center = x_left + (root_width - popup_width) // 2
        y_center = y_top + (root_height - popup_height) // 2

        popup.geometry(f"+{x_center}+{y_center}")

        tk.Label(popup, text="Çakışma Var!",
                 wraplength=200).pack(pady=20, side="top")

    def add_activity_action(self):
        student_id = self.entry_data
        activity_day = self.activity_day.get()
        activity_time = self.activity_entries[0].get()
        activity_name = self.activity_entries[1].get()
        busy_hours_query = """
            SELECT DISTINCT sa.START_HOUR
            FROM student_activities sa
            WHERE sa.STUDENT_ID = {} AND sa.DAY_OF_WEEK = '{}'
            UNION
            SELECT DISTINCT sh.START_HOUR
            FROM section_hours sh
            JOIN course_section cs ON sh.SEC_ID = cs.ID
            JOIN student_section ss ON cs.ID = ss.SECTION_ID
            WHERE ss.STUDENT_ID = {} AND sh.DAY_OF_WEEK = '{}';
        """.format(student_id, activity_day, student_id, activity_day)
        busy_result = self.cont.sql_query(busy_hours_query)
        busy_result = [
            "{:02}:{:02}:{:02}".format(
                int(item[0].total_seconds()) // 3600,
                (int(item[0].total_seconds()) % 3600) // 60,
                int(item[0].total_seconds()) % 60,
            )
            for item in busy_result
        ]

        if activity_time not in busy_result:
            add_activity_query = "INSERT INTO student_activities " \
                                 "(STUDENT_ID, START_HOUR, DAY_OF_WEEK, ACTIVITY_NAME) VALUES" \
                                 " ({}, '{}', '{}', " \
                                 "'{}');".format(student_id, activity_time, activity_day, activity_name)
            self.cont.sql_query(add_activity_query)
            commit_result = self.cont.commit()
            if commit_result is None:
                self.add_course_commit_success_popup()
            else:
                self.add_course_commit_fail_popup()
        else:
            self.cakisma_popup()

    def rm_activity_action(self):
        print("düğme çalışıyor")
        student_id = self.entry_data
        activity_name = self.rm_activity_dropdown.get()
        act_remove_query = "DELETE FROM student_activities " \
                           "WHERE ACTIVITY_NAME = '{}' AND STUDENT_ID = {};".format(activity_name, student_id)
        self.cont.sql_query(act_remove_query)
        commit_result = self.cont.commit()
        if commit_result is None:
            self.add_course_commit_success_popup()
        else:
            self.add_course_commit_fail_popup()
