'''
Student ID: u3301989
Assignment: 1, Part5
Date Created: April 10, 2026
Last Updated: April 15
'''

import tkinter as tk
from controller5 import InventoryController

class InventoryGUI:
    def __init__(self):
        self.controller = InventoryController()

        self.window = tk.Tk()
        self.window.title("Inventory Management System")
        self.window.geometry("600x400")
        self.window.resizable(False, False)

        # ===== TOP TITLE =====
        tk.Label(self.window, text="Inventory Management System", font=("Arial", 14)).pack(pady=10)

        # MAIN FRAME
        main_frame = tk.frame(self.window)
        main_frame.pack(side=tk.LEFT)

        # LEFT LISTBOX
        self.listbox = tk.Listbox(main_frame, width=25, height=12)
        self.listbox.pack(side=tk.LEFT, padx=10)

        # RIGHT DISPLAY AREA
        self.display = tk.Text(main_frame, width=40, height=12, bg="#dfe8c6")
        self.display.pack(side=tk.LEFT)

        # ===== BUTTON FRAME =====
        btn_frame = tk.Frame(self.window)
        btn_frame.pack(pady=10)

        tk.Button(btn_frame, text="Add Item", width=12, command=self.add_item).pack(side=tk.LEFT, padx=5)
        tk.Button(btn_frame, text="Show Details", width=12, command=self.show_details).pack(side=tk.LEFT, padx=5)
        tk.Button(btn_frame, text="Update Item", width=12, command=self.update_item).pack(side=tk.LEFT, padx=5)
        tk.Button(btn_frame, text="Delete Item", width=12, command=self.delete_item).pack(side=tk.LEFT, padx=5)
        tk.Button(btn_frame, text="Exit", width=12, command=self.window.destroy).pack(side=tk.LEFT, padx=5)

        self.window.mainloop()

    # ===== FUNCTIONS =====
    def refresh_list(self):
        self.listbox.delete(0, tk.END)
        for product in self.controller.get_products():
            self.listbox.insert(tk.END, product.get_name())

    def add_item(self):
        self.popup("Add Product")

    def update_item(self):
        try:
            index = self.listbox.curselection()[0]
            product = self.controller.get_product(index)
            self.popup("Update Product", index, product)
        except:
            pass

    def delete_item(self):
        try:
            index = self.listbox.curselection()[0]
            self.controller.delete_product(index)
            self.refresh_list()
            self.display.delete("1.0", tk.END)
        except:
            pass

    def show_details(self):
        try:
            index = self.listbox.curselection()[0]
            product = self.controller.get_product(index)

            self.display.delete("1.0", tk.END)
            self.display.insert(tk.END,
                f"Name: {product.get_name()}\n"
                f"Price: ${product.get_price()}\n"
                f"Description: {product.get_description()}"
            )
        except:
            pass

    # ===== POPUP WINDOW =====
    def popup(self, title, index=None, product=None):
        win = tk.Toplevel()
        win.title(title)

        name_var = tk.StringVar()
        price_var = tk.StringVar()
        desc_var = tk.StringVar()

        if product:
            name_var.set(product.get_name())
            price_var.set(product.get_price())
            desc_var.set(product.get_description())

        tk.Label(win, text="Name").pack()
        tk.Entry(win, textvariable=name_var).pack()

        tk.Label(win, text="Price").pack()
        tk.Entry(win, textvariable=price_var).pack()

        tk.Label(win, text="Description").pack()
        tk.Entry(win, textvariable=desc_var).pack()

        def submit():
            name = name_var.get()
            price = float(price_var.get())
            desc = desc_var.get()

            if product:
                self.controller.update_product(index, name, price, desc)
            else:
                self.controller.add_product(name, price, desc)

            self.refresh_list()
            win.destroy()

        tk.Button(win, text="Submit", command=submit).pack(pady=5)

if __name__ == "__main__":
    InventoryGUI()