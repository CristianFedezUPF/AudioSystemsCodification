from tkinter import *
from tkinter import ttk
from main import init_window


def clear_frame(frame: Frame):
    for widget in frame.winfo_children():
        widget.destroy()
    frame.update()


def show_message_frame(frame: Frame, message: str):
    clear_frame(frame)
    ttk.Label(frame, text=message).grid(column=0, row=0, sticky=EW)
    frame.update()


def reset_to_menu(frame: Frame):
    clear_frame(frame)
    init_window(frame)


def append_message_frame(frame: Frame, message: str, row=1, column=1,
                         sticky=""):
    ttk.Label(frame, text=message).grid(column=column, row=row, sticky=sticky)
    frame.update()
