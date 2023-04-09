import os


# ID для notebook
def iD_name():
    number = os.listdir(path="Notebook_folder/notebooks")
    return len(number)