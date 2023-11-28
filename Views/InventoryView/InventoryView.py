import tkinter as tk
from tkinter import ttk
import Views


class InventoryView(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.mode = None
        self.title = tk.StringVar(value="Envanter")
        self.preload_func = self.populate_tree_view
        self.cont = controller

        title_frame = tk.Frame(self)
        back_button = tk.Button(title_frame, text="←", command=lambda: controller.show_frame(Views.MainScreenView))
        title_label = tk.Label(title_frame, textvariable=self.title)
        back_button.pack(side="left")
        title_label.pack(side="left", fill="x")
        title_frame.pack(side="top", fill="x", pady=5, padx=5)

        summary_frame = tk.Frame(self)
        summary_frame.columnconfigure(0, weight=1)
        summary_frame.rowconfigure(0, weight=1)
        self.tree_view = ttk.Treeview(summary_frame)
        self.tree_view.configure(selectmode="browse")
        self.tree_view.grid(row=0, column=0, sticky="nsew")

        self.tree_view['columns'] = ('id', 'malzeme', 'stok', 'fiyat')

        self.tree_view.column('#0', width=0, stretch=tk.NO)
        self.tree_view.column('id', width=50, stretch=tk.NO)
        self.tree_view.column("malzeme", width=400, anchor=tk.W)
        self.tree_view.column("stok", width=25, anchor=tk.CENTER)
        self.tree_view.column("fiyat", width=25, anchor=tk.CENTER)

        self.tree_view.heading("id", text="", anchor=tk.W)
        self.tree_view.heading("malzeme", text="Malzeme", anchor=tk.W)
        self.tree_view.heading("stok", text="Stok", anchor=tk.CENTER)
        self.tree_view.heading("fiyat", text="Son Fiyat", anchor=tk.CENTER)

        button_frame = tk.Frame(summary_frame)
        add_item_button = tk.Button(button_frame, text="Yeni Malzeme Ekle", height=5,
                                    command=lambda: self.cont.show_frame(Views.AddInventoryView))
        modify_item_button = tk.Button(button_frame, text="Düzenle", height=5, command=self.open_modify_inventory_view)
        remove_item_button = tk.Button(button_frame, text="Malzeme Sil", height=5, command=self.remove_inventory_item)

        add_item_button.pack(side="top", fill="x", pady=20, padx=10)
        modify_item_button.pack(side="top", fill="x", pady=20, padx=10)
        remove_item_button.pack(side="bottom", fill="x", pady=20, padx=10)
        button_frame.grid(row=0, column=1, sticky="ns")

        summary_frame.pack(side="top", expand=True, fill="both", padx=10, pady=10)

        self.populate_tree_view()

    def remove_inventory_item(self):
        if self.tree_view.selection():
            def remove_inventory_query(inventory_id, popup):
                inventory_query = "DELETE FROM inventory WHERE ID={}".format(inventory_id)
                self.cont.sql_query(inventory_query)
                result = self.cont.commit()
                if result:
                    popup.destroy()
                pass

            selected_item = self.tree_view.selection()[0]
            item_data = self.tree_view.item(selected_item)
            entity_id = item_data['values'][0]
            entity_name = item_data['values'][1]
            entity_stock = item_data['values'][2]
            popup = tk.Toplevel(self)
            popup.title("Envanterden Sil")

            # Set the size of the popup window
            popup_width = 300
            popup_height = 200
            popup.geometry(f"{popup_width}x{popup_height}")

            # Calculate position x and y coordinates
            x_left = self.winfo_x()
            y_top = self.winfo_y()
            root_width = self.winfo_width()
            root_height = self.winfo_height()
            x_center = x_left + (root_width - popup_width) // 2
            y_center = y_top + (root_height - popup_height) // 2

            popup.geometry(f"+{x_center}+{y_center}")

            popup_text = "Envanter'den {} öğesi ve stok bilgisi {} adet silinecek. Onaylıyor musunuz?:".format(
                entity_name, entity_stock)
            tk.Label(popup, text=popup_text, wraplength=250).pack(pady=20, side="top")
            button_frame = tk.Frame(popup)
            button_frame.pack(pady=20, side="top")
            send_button = tk.Button(button_frame, text="SİL", command=lambda: remove_inventory_query(entity_id, popup))
            send_button.pack(side="left", padx=10)
            cancel_button = tk.Button(button_frame, text="İptal", command=popup.destroy)
            cancel_button.pack(side="left", padx=10)

    def open_modify_inventory_view(self):
        if self.tree_view.selection():
            selected_item = self.tree_view.selection()[0]
            item_data = self.tree_view.item(selected_item)
            entity_id = item_data['values'][0]
            management_view = self.cont.get_frame(Views.ModifyInventoryView)
            management_view.entry_data = entity_id
            self.cont.show_frame(Views.ModifyInventoryView)

    def populate_tree_view(self):
        for item in self.tree_view.get_children():
            self.tree_view.delete(item)

        inventory_query = "SELECT ID, MATERIAL_NAME, REMAINING, CONCAT(PRICE, ' ₺') FROM inventory"
        inventory_list = self.cont.sql_query(inventory_query)

        for inventory in inventory_list:
            self.tree_view.insert('', 'end', values=inventory)
