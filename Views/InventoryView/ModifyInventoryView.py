import tkinter as tk
from tkinter import ttk
import Views


class ModifyInventoryView(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.mode = None
        self.title = tk.StringVar(value="Envanter Düzenle")
        self.preload_func = self.load_entity_data
        self.entry_data = None
        self.cont = controller
        self.quantity_variable = tk.StringVar()
        self.button_text_var = tk.StringVar()
        self.origin_value = 0

        title_frame = tk.Frame(self)
        back_button = tk.Button(title_frame, text="←", command=lambda: controller.show_frame(Views.InventoryView))
        title_label = tk.Label(title_frame, textvariable=self.title)
        back_button.pack(side="left")
        title_label.pack(side="left", fill="x")
        title_frame.pack(side="top", fill="x", pady=5, padx=5)

        self.inventory_item_frame = tk.Frame(self)
        self.inventory_item_frame.pack(side="top", fill="both", expand=True, padx=25, pady=25)

        tk.Label(self.inventory_item_frame, text="Stok Numarası").grid(row=0, column=0, sticky="we", padx=10, pady=10)
        tk.Label(self.inventory_item_frame, text="Envanter Adı").grid(row=1, column=0, sticky="we", padx=10, pady=10)
        tk.Label(self.inventory_item_frame, text="Yeni Miktar").grid(row=2, column=0, sticky="w", padx=10, pady=10)
        tk.Label(self.inventory_item_frame, text="Satın Alım Fiyatı").grid(row=3, column=0, sticky="w", padx=10,
                                                                           pady=10)

        self.envanter_no_label = tk.Label(self.inventory_item_frame, text="0")
        self.name_label = tk.Label(self.inventory_item_frame, text="")
        self.quantity_label = tk.Entry(self.inventory_item_frame, textvariable=self.quantity_variable)
        self.quantity_variable.trace_add("write", self.on_quantity_update)
        self.price_label = tk.Entry(self.inventory_item_frame)

        self.envanter_no_label.grid(row=0, column=1, sticky="we", padx=10, pady=10)
        self.name_label.grid(row=1, column=1, sticky="w", padx=10, pady=10)
        self.quantity_label.grid(row=2, column=1, sticky="w", padx=10, pady=10)
        self.price_label.grid(row=3, column=1, sticky="w", padx=10, pady=10)

        self.modify_inventory_button = tk.Button(self.inventory_item_frame, command=self.modify_inventory_action,
                                                 textvariable=self.button_text_var)
        self.modify_inventory_button.grid(row=4, column=0, columnspan=2, sticky="sew")

    def load_entity_data(self):
        if self.entry_data is None:
            pass
        else:
            inventory_id_query = "SELECT ID, MATERIAL_NAME, REMAINING, PRICE FROM inventory WHERE ID={}".format(
                self.entry_data)
            result = self.cont.sql_query(inventory_id_query)[0]
            id_inv = result[0]
            name = result[1]
            remaining = result[2]
            price = result[3]
            self.envanter_no_label.config(text=id_inv)
            self.name_label.config(text=name)
            self.quantity_variable.set(str(remaining))
            self.origin_value = remaining
            self.price_label.delete(0, tk.END)
            self.price_label.insert(0, price)
            self.on_quantity_update()

    def modify_inventory_action(self):
        update_query = "UPDATE inventory " \
                       "SET " \
                       "REMAINING = {}, " \
                       "PRICE = {} " \
                       "WHERE ID = {};".format(self.quantity_variable.get(), self.price_label.get(), self.entry_data)
        try:
            self.cont.sql_query(update_query)
        except:
            self.send_sms_command()


        result = self.cont.commit()
        if result:
            self.cont.show_frame(Views.InventoryView)
        else:
            print("update fail: ", update_query)


    def send_sms_command(self):
            popup = tk.Toplevel(self)
            popup.title("Error")

            # Set the size of the popup window
            popup_width = 300
            popup_height = 200
            popup.geometry(f"{popup_width}x{popup_height}")
            popup.resizable(False, False)

            # Calculate position x and y coordinates
            x_left = self.winfo_x()
            y_top = self.winfo_y()
            root_width = self.winfo_width()
            root_height = self.winfo_height()
            x_center = x_left + (root_width - popup_width) // 2
            y_center = y_top + (root_height - popup_height) // 2

            popup.geometry(f"+{x_center}+{y_center}")
            tk.Label(popup, text="Remaining asa cannot be lower than 5").pack(pady=20)



    def on_quantity_update(self, *args):
        current_value = self.quantity_variable.get()
        try:
            current_value = float(current_value)
        except ValueError:
            print(current_value, self.origin_value)
            return False

        if current_value > self.origin_value:
            self.button_text_var.set("Satın Alım Yap")
        elif current_value < self.origin_value:
            self.button_text_var.set("Envanterden eksilt")
        else:
            self.button_text_var.set("Envanteri Düzenle")
