'''
Student ID: u3301989
Assignment: 1, Part5
Date Created: April 11 2026.
Last Updated: April 15
'''

import tkinter as tk
from tkinter import messagebox
from controller import InventoryController

class InventoryGUI:
    def __init__(self):
        self.controller = InventoryController()

        self.main_window = tk.Tk()
        self.main_window.title("Inventory Management System")
        self.main_window.geometry("600x300")
        self.main_window.resizable(False, False)

        #Frame
        self.frame1 = tk.Frame(self.main_window)
        self.frame2 = tk.Frame(self.main_window)
        self.frame3 = tk.Frame(self.main_window)
        self.frame4 = tk.Frame(self.main_window)
        self.frame5 = tk.Frame(self.main_window)

        self.title_lbl = tk.Label(self.frame1, text="Inventory Management System", font=("Arial", 14))
        self.title_lbl.pack(side=tk.LEFT)

        # LEFT LISTBOX
        self.listbox = tk.Listbox(self.frame2, width=25, height=12)
        self.listbox.pack(side=tk.LEFT, pady=10)

        # RIGHT DISPLAY AREA
        self.display = tk.Text(self.frame2, width=40, height=12, bg="#dfe8c6")
        self.display.pack(side=tk.LEFT)

        #BUTTON
        self.add_btn = tk.Button(self.frame3, text="Add Item", width=12, command=self.add_item)
        self.add_btn.pack(side=tk.LEFT)

        self.show_btn = tk.Button(self.frame3, text="Show Details", width=12, command=self.show_details)
        self.show_btn.pack(side=tk.LEFT)

        self.update_btn = tk.Button(self.frame3, text="Update Item", width=12, command=self.update_item)
        self.update_btn.pack(side=tk.LEFT)

        self.delete_btn = tk.Button(self.frame3, text="Delete Item", width=12, command=self.delete_item)
        self.delete_btn.pack(side=tk.LEFT)

        self.exit_btn = tk.Button(self.frame3, text="Exit", width=12, command=self.main_window.destroy)
        self.exit_btn.pack(side=tk.LEFT)

        #FRAME PACKED
        self.frame1.pack()
        self.frame2.pack()
        self.frame3.pack()
        self.frame4.pack()
        self.frame5.pack()

        self.main_window.mainloop()

    def refresh_list(self):
        self.listbox.delete(0, tk.END)
        for product in self.controller.get_products():
            self.listbox.insert(tk.END, product.get_name())

    def add_item(self):
        self.popup("Add Product")

    def update_item(self):
        index = self.listbox.curselection()[0]
        product = self.controller.get_product(index)
        self.popup("Update Product", index, product)


    def delete_item(self):
        index = self.listbox.curselection()[0]
        product = self.controller.get_product(index)

        confirm = messagebox.askyesno(
            "Confirm Delete",
            f"Are you sure you want to delete '{product.get_name()}'?"
        )

        if confirm:
            self.controller.delete_product(index)
            self.refresh_list()
            self.display.delete("1.0", tk.END)


    def show_details(self):
        index = self.listbox.curselection()[0]
        product = self.controller.get_product(index)

        self.display.delete("1.0", tk.END)
        self.display.insert(tk.END,
            f"Name: {product.get_name()}\n"
            f"Price: ${product.get_price()}\n"
            f"Description: {product.get_description()}"
            )

    # POPUP WINDOW
    def popup(self, title, index=None, product=None):
        self.window = tk.Toplevel()
        self.window.title(title)
        self.window.geometry("200x200")

        name_var = tk.StringVar()
        price_var = tk.StringVar()
        desc_var = tk.StringVar()

        if product:
            name_var.set(product.get_name())
            price_var.set(product.get_price())
            desc_var.set(product.get_description())

        self.name_lbl = tk.Label(self.window, text="Name")
        self.name_lbl.pack()
        self.name_ent = tk.Entry(self.window, textvariable=name_var)
        self.name_ent.pack()

        self.price_lbl = tk.Label(self.window, text="Price")
        self.price_lbl.pack()
        self.price_ent = tk.Entry(self.window, textvariable=price_var)
        self.price_ent.pack()

        self.desc_lbl = tk.Label(self.window, text="Description")
        self.desc_lbl.pack()
        self.desc_ent = tk.Entry(self.window, textvariable=desc_var)
        self.desc_ent.pack()

        def submit():
            name = name_var.get()
            price = float(price_var.get())
            desc = desc_var.get()

            if product:
                self.controller.update_product(index, name, price, desc)
            else:
                self.controller.add_product(name, price, desc)

            self.refresh_list()
            self.window.destroy()

        self.submit_btn = tk.Button(self.window, text="Submit", command=submit)
        self.submit_btn.pack(pady=5)