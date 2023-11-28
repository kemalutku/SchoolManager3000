import tkinter as tk
from tkinter import ttk
import Views


class AddRemoveRelationView(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.add_course_dropdown = None
        self.rm_course_dropdown = None
        self.mode = None
        self.entry_data = None
        self.title = tk.StringVar(value="Ders Ekle/Sil")
        self.preload_func = None
        self.cont = controller

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
                                     " WHERE ss.STUDENT_ID = {});".format(self.entry_data)
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
        print(commit_result)

    def rm_relation_action(self):
        pass

    def add_course_commit_fail_popup(self):
        popup = tk.Toplevel(self)
        popup.title("Kayıt Başarısız!")
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

        tk.Label(popup, text="Kayıt Başarısız. Lütfen girdiğiniz alanları ve internet bağlantısınızı kontrol edin!",
                 wraplength=200).pack(pady=20, side="top")

    def add_course_commit_success_popup(self):
        popup = tk.Toplevel(self)
        popup.title("Kayıt Başarılı!")
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

        tk.Label(popup, text="Kayıt Başarılı!",
                 wraplength=200).pack(pady=20, side="top")
