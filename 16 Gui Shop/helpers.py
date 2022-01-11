from tk_object import tk


def clean_screen():
    for element in tk.grid_slaves():
        element.destroy()