from tkinter import *
from tkinter.ttk import *
from tk_object import tk
from helpers import clean_screen
# from PIL import Image, ImageTk
import os
import json

base_folder = os.path.dirname(__file__)


def buy_product(button):
    _, product_id = button.cget('text').split()
    product_id = int(product_id)
    with open("database/current_user.txt", "r") as file:
        current_logged_user = file.read()
    with open("database/users.txt", "r+") as file:
        users = file.readlines()
        file.seek(0)
        for user in users:
            current_user = json.loads(user)
            if current_user.get("username") == current_logged_user:
                current_user['products'].append(product_id)
            file.write(json.dumps(current_user))
            file.write("\n")
    with open("database/products.txt", "r+") as file:
        products = file.readlines()
        file.seek(0)
        for product in products:
            current_product = json.loads(product)
            if current_product["id"] == product_id and current_product["count"] > 0:
                current_product["count"] -= 1
            file.write(json.dumps(current_product))
            file.write("\n")
    render_products()


def render_products():
    clean_screen()
    with open("database/products.txt", "r") as file:
        products = file.readlines()
        column_counter = 0
        for product in products:
            current_product = json.loads(product)
            Label(tk, text=current_product.get('name')).grid(row=0, column=column_counter)

            # image = Image.open(os.path.join(os.path.join(base_folder, "images"), current_product.get("img_path")))
            # image = image.resize((100, 100))
            # photo = ImageTk.PhotoImage(image)
            # img_label = Label(image=photo)
            # img_label.image = photo
            # img_label.grid(row=1, column=column_counter)

            button = Button(tk, text=f"Buy {current_product.get('id')}")
            button.configure(command=lambda b=button: buy_product(b))
            Label(tk, text=current_product.get('count')).grid(row=2, column=column_counter)
            button.grid(row=3, column=column_counter)
            column_counter += 1