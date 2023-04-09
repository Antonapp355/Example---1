import os


def new_folder():
    if not os.path.isdir("Notebook_folder"):
        os.mkdir("Notebook_folder")
        os.mkdir("Notebook_folder/notebooks")