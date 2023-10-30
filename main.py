import mysql.connector
import tkinter as tk



mydb = mysql.connector.connect(
    host="5.75.140.90",
    user="bil071",
    password='Bil071-24'
)

cursor = mydb.cursor()
cursor.execute("SHOW DATABASES")



root = tk.Tk()
for x in cursor:
    label = tk.Label(root, text=str(x))
    label.pack()
root.mainloop()