import data_time
import modul_add

str_menu = ""

def menu_init(m):
    global str_menu
    str_menu = m
def menu(m):
    if m == "add":
        modul_add.add_note()
    elif m == "sort":
        data_time.sort()
    elif m == "exit":
        exit()