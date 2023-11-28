import tkinter as tk
from tkinter import ttk
import Views


class AddInventoryView(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.mode = None
        self.title = tk.StringVar(value="Envanter Ekle")
        self.preload_func = self.get_max_id
        self.cont = controller

        title_frame = tk.Frame(self)
        back_button = tk.Button(title_frame, text="←", command=lambda: controller.show_frame(Views.InventoryView))
        title_label = tk.Label(title_frame, textvariable=self.title)
        back_button.pack(side="left")
        title_label.pack(side="left", fill="x")
        title_frame.pack(side="top", fill="x", pady=5, padx=5)

        self.inventory_item_frame = tk.Frame(self)
        self.inventory_item_frame.pack(side="top", fill="both", expand=True, padx=25, pady=25)

        tk.Label(self.inventory_item_frame, text="Stok Numarası").grid(row=0, column=0, sticky="w", padx=10, pady=10)
        tk.Label(self.inventory_item_frame, text="Envanter Adı").grid(row=1, column=0, sticky="w", padx=10, pady=10)
        tk.Label(self.inventory_item_frame, text="Miktar").grid(row=2, column=0, sticky="w", padx=10, pady=10)
        tk.Label(self.inventory_item_frame, text="Fiyat").grid(row=3, column=0, sticky="w", padx=10, pady=10)

        self.envanter_no_label = tk.Label(self.inventory_item_frame, text="0")
        self.name_label = tk.Entry(self.inventory_item_frame)
        self.quantity_label = tk.Entry(self.inventory_item_frame)
        self.price_label = tk.Entry(self.inventory_item_frame)

        self.envanter_no_label.grid(row=0, column=1, sticky="we", padx=10, pady=10)
        self.name_label.grid(row=1, column=1, sticky="w", padx=10, pady=10)
        self.quantity_label.grid(row=2, column=1, sticky="w", padx=10, pady=10)
        self.price_label.grid(row=3, column=1, sticky="w", padx=10, pady=10)

        add_inventory_button = tk.Button(self.inventory_item_frame, command=self.add_inventory_action,
                                         text="Envantere Ekle")
        add_inventory_button.grid(row=4, column=0, columnspan=2, sticky="sew")

    def get_max_id(self):
        max_inventory_id_query = "SELECT MAX(ID) FROM inventory"
        result = self.cont.sql_query(max_inventory_id_query)
        self.envanter_no_label.config(text=result[0][0] + 1)

    def add_inventory_action(self):
        id = self.envanter_no_label.cget("text")
        name = self.name_label.get()
        quantity = self.quantity_label.get()
        price = self.price_label.get()
        try:
            quantity = float(quantity)
            price = float(price)

        except ValueError:
            print("Invalid quantity. Must be float")
            self.commit_fail_popup()
            return False

        insert_inventory_query = "INSERT INTO inventory (MATERIAL_NAME, REMAINING, PRICE) " \
                                 "VALUES('{}', '{}', '{}')".format(name, quantity, price)
        # TODO: Add sql query for accounting
        self.cont.sql_query(insert_inventory_query)
        commit_result = self.cont.commit()
        if commit_result:
            self.cont.show_frame(Views.InventoryView)
        else:
            self.commit_fail_popup()

    def commit_fail_popup(self):
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
