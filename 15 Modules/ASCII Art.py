from pyfiglet import figlet_format


def print_msg(message):
    ascii_art = figlet_format(message)
    return ascii_art


print(print_msg(input()))