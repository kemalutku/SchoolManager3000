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

    def get_max_id(self):
        max_inventory_id_query = "SELECT MAX(ID) FROM inventory"
        result = self.cont.sql_query(max_inventory_id_query)
        self.envanter_no_label.config(text=result)