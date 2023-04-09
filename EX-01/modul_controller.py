import view
import modul_menu

def button_click():
    value_m = view.menu()
    modul_menu.menu(value_m)
    if value_m == "exit":
        return exit
    elif value_m != "exit":
        button_click()