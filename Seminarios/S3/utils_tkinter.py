from tkinter import *
from tkinter import ttk
import tasks_tkinter_UI_handler as UI_handler

"""
Various small tkinter util functions to clear the frame, show messages, ...
"""


def clear_frame(frame: Frame):
    for widget in frame.winfo_children():
        widget.destroy()
    frame.update()


def show_message_frame(frame: Frame, message: str, padx=5):
    clear_frame(frame)
    ttk.Label(frame, text=message).grid(column=0, row=0, sticky=EW, padx=padx)
    frame.update()


def reset_to_menu(frame: Frame):
    clear_frame(frame)
    UI_handler.init_window(frame)


def append_message_frame(frame: Frame, message: str, row=1, column=1,
                         sticky=""):
    ttk.Label(frame, text=message).grid(column=column, row=row, sticky=sticky)
    frame.update()


if __name__ == "__main__":
    print("You should run main.py file")
