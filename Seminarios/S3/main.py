from tkinter import *
from tkinter import ttk
import tasks_tkinter_UI_handler as UI_handler

"""
Main file to start up Tkinter window with an UI to perform all tasks
and conversions from this seminar.
"""


def main():
    # init tkinter window
    root = Tk()
    root.title("Video Converter")
    root.minsize(540, 200)
    mainframe = ttk.Frame(root, padding="3 3 12 12")
    mainframe.grid(column=0, row=0, sticky=NSEW)

    # so that they are able to resize
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)
    mainframe.columnconfigure(0, weight=1)
    mainframe.rowconfigure(0, weight=1)
    mainframe.columnconfigure(1, weight=1)
    mainframe.rowconfigure(1, weight=1)
    mainframe.columnconfigure(2, weight=1)
    mainframe.rowconfigure(2, weight=1)

    # init main window with various options
    UI_handler.init_window(mainframe)

    for child in mainframe.winfo_children():
        child.grid_configure(padx=5, pady=5)

    root.mainloop()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
