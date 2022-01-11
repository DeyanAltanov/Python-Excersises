from tkinter import Button, Entry, Label
from tk_object import tk
from helpers import clean_screen
from products import render_products
import json


def login(username, password):
    with open("database/users_credentials.txt", "r") as file:
        lines = file.readlines()
        for line in lines:
            u, p = line.split(", ")
            if u == username and p == password:
                with open("database/current_user.txt", "w") as current_user_file:
                    current_user_file.write(username)
                render_products()
                return

        render_login(errors=True)


def register(**user):
    user.update({"products": []})
    with open("database/users.txt", "a", newline='\n') as file:
        file.write(json.dumps(user))
        file.write('\n')
    with open("database/users_credentials.txt", "a", newline='') as file:
        file.write(f"{user.get('username')}, {user.get('password')}")
    render_login()


def render_login(errors=None):
    clean_screen()
    Label(tk, text='Enter username:').grid(row=1, column=0)
    username = Entry(tk)
    username.grid(row=2, column=0)
    Label(tk, text='Enter password:').grid(row=3, column=0)
    password = Entry(tk, show='*')
    password.grid(row=4, column=0)
    if errors:
        Label(tk, text='Invalid username, or password.').grid(row=5, column=0)
    Button(tk, text='Enter', bg='green', command=lambda: login(username.get(), password.get())).grid(row=6, column=0)


def render_register():
    clean_screen()
    Label(tk, text='Username:').grid(row=1, column=0)
    username = Entry(tk)
    username.grid(row=2, column=0)
    Label(tk, text='Password:').grid(row=3, column=0)
    password = Entry(tk, show='*')
    password.grid(row=4, column=0)
    Label(tk, text='First name:').grid(row=5, column=0)
    first_name = Entry(tk)
    first_name.grid(row=6, column=0)
    Label(tk, text='Last name:').grid(row=7, column=0)
    last_name = Entry(tk)
    last_name.grid(row=8, column=0)
    Button(tk, text='Register', bg='green', command=lambda: register(username=username.get(), password=password.get(), first_name=first_name.get(), last_name=last_name.get())).grid(row=9, column=0)


def render_main_enter_screen():
    Button(tk, text='Login', bg='green', fg='white', command=render_login).grid(row=0, column=0)
    Button(tk, text='Register', bg='yellow', command=render_register).grid(row=0, column=1)