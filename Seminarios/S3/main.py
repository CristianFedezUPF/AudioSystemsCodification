from tkinter import *
from tkinter import ttk
from functools import partial
import tasks_tkinter as tasks
import utils_tkinter as utils


def convert_res(mainframe):
    utils.clear_frame(mainframe)
    input_file = StringVar()
    input_entry = ttk.Entry(mainframe, width=20, textvariable=input_file)
    input_entry.grid(column=2, row=0, sticky=EW)
    ttk.Label(mainframe, text="Input file: ").grid(column=1, row=0, sticky=W,
                                                   padx=10)

    resolution = StringVar(value='1')
    _720p = ttk.Radiobutton(mainframe, text='720p', variable=resolution,
                            value='1')
    _480p = ttk.Radiobutton(mainframe, text='480p', variable=resolution,
                            value='2')
    _360x240 = ttk.Radiobutton(mainframe, text='360x240', variable=resolution,
                               value='3')
    _160x120 = ttk.Radiobutton(mainframe, text='160x120', variable=resolution,
                               value='4')
    _720p.grid(column=0, row=1, padx=20, pady=5)
    _480p.grid(column=1, row=1, padx=20)
    _360x240.grid(column=2, row=1, padx=20)
    _160x120.grid(column=3, row=1, padx=20)

    b1 = ttk.Button(mainframe, text="Convert!",
                    command=lambda: tasks.convert_resolution(input_file.get(),
                                                             resolution.get(),
                                                             mainframe))
    b1.grid(column=3, row=2, sticky=W)

    b2 = ttk.Button(mainframe, text="< Back",
                    command=partial(utils.reset_to_menu, mainframe))
    b2.grid(column=0, row=0, sticky=W)


def convert_codec(mainframe):
    utils.clear_frame(mainframe)
    upper_row = ttk.Frame(mainframe, padding="3 3 12 12")
    upper_row.grid(column=1, row=0)

    b1 = ttk.Button(upper_row, text="< Back",
                    command=partial(utils.reset_to_menu, mainframe))
    b1.grid(column=0, row=0, sticky=W)

    input_label = ttk.Label(upper_row, text="Input file: ")
    input_label.grid(column=1, row=0, sticky=W, padx=10)

    input_file = StringVar()
    input_entry = ttk.Entry(upper_row, width=35, textvariable=input_file)
    input_entry.grid(column=2, row=0, sticky=EW)

    mid_row = ttk.Frame(mainframe, padding="3 3 12 12")
    mid_row.grid(column=1, row=1)

    codec = StringVar(value='1')
    _VP8 = ttk.Radiobutton(mid_row, text='VP8', variable=codec,
                           value='1')
    _VP9 = ttk.Radiobutton(mid_row, text='VP9', variable=codec,
                           value='2')
    _HEVC = ttk.Radiobutton(mid_row, text='HEVC', variable=codec,
                            value='3')
    _AV1 = ttk.Radiobutton(mid_row, text='AV1', variable=codec,
                           value='4')
    _VP8.grid(column=0, row=1, padx=20, pady=5)
    _VP9.grid(column=1, row=1, padx=20)
    _HEVC.grid(column=2, row=1, padx=20)
    _AV1.grid(column=3, row=1, padx=20)

    lower_row = ttk.Frame(mainframe, padding="3 3 12 12")
    lower_row.grid(column=1, row=2)

    crf_label = ttk.Label(lower_row, text="Constant Rate Factor"
                                          " (quality) [5-50] default 25: ")
    crf_label.grid(column=0, row=2, sticky=W, padx=10)

    crf = StringVar()
    crf_entry = ttk.Entry(lower_row, width=5, textvariable=crf)
    crf_entry.grid(column=1, row=2, sticky=EW, padx=10)

    b2 = ttk.Button(lower_row, text="Convert!",
                    command=lambda: tasks.convert_codec(input_file.get(),
                                                        codec.get(),
                                                        mainframe, crf=crf))
    b2.grid(column=2, row=2, sticky=W)


def stack_4_videos(mainframe):
    utils.clear_frame(mainframe)

    b2 = ttk.Button(mainframe, text="< Back",
                    command=partial(utils.reset_to_menu, mainframe))
    b2.grid(column=0, row=0, sticky=W)

    inputs = ttk.Frame(mainframe, padding="3 3 12 12")
    inputs.grid(column=1, row=1, sticky=W)

    ttk.Label(inputs, text="Tags appear "
                           "overlayed in\n"
                           "the top-left of "
                           "every video.").grid(column=3, row=0, pady=5)

    input1_file = StringVar()
    input1_entry = ttk.Entry(inputs, width=30, textvariable=input1_file)
    input1_entry.grid(column=1, row=1, sticky=EW)
    input1_label = ttk.Label(inputs, text="Input 1 path (Top-left): ")
    input1_label.grid(column=0, row=1, sticky=W, padx=10)

    input1_tag = StringVar()
    input1_tag_entry = ttk.Entry(inputs, width=8, textvariable=input1_tag)
    input1_tag_entry.grid(column=3, row=1, sticky=EW)
    input1_tag_label = ttk.Label(inputs, text="Tag: ")
    input1_tag_label.grid(column=2, row=1, sticky=W, padx=10)

    input2_file = StringVar()
    input2_entry = ttk.Entry(inputs, width=30, textvariable=input2_file)
    input2_entry.grid(column=1, row=2, sticky=EW)
    input2_label = ttk.Label(inputs, text="Input 2 path (Top-right): ")
    input2_label.grid(column=0, row=2, sticky=W, padx=10)

    input2_tag = StringVar()
    input2_tag_entry = ttk.Entry(inputs, width=8, textvariable=input2_tag)
    input2_tag_entry.grid(column=3, row=2, sticky=EW)
    input2_tag_label = ttk.Label(inputs, text="Tag: ")
    input2_tag_label.grid(column=2, row=2, sticky=W, padx=10)

    input3_file = StringVar()
    input3_entry = ttk.Entry(inputs, width=30, textvariable=input3_file)
    input3_entry.grid(column=1, row=3, sticky=EW)
    input3_label = ttk.Label(inputs, text="Input 3 path (Bottom-left): ")
    input3_label.grid(column=0, row=3, sticky=W, padx=10)

    input3_tag = StringVar()
    input3_tag_entry = ttk.Entry(inputs, width=8, textvariable=input3_tag)
    input3_tag_entry.grid(column=3, row=3, sticky=EW)
    input3_tag_label = ttk.Label(inputs, text="Tag: ")
    input3_tag_label.grid(column=2, row=3, sticky=W, padx=10)

    input4_file = StringVar()
    input4_entry = ttk.Entry(inputs, width=30, textvariable=input4_file)
    input4_entry.grid(column=1, row=4, sticky=EW)
    input4_label = ttk.Label(inputs, text="Input 4 path (Bottom-right): ")
    input4_label.grid(column=0, row=4, sticky=W, padx=10)

    input4_tag = StringVar()
    input4_tag_entry = ttk.Entry(inputs, width=8, textvariable=input4_tag)
    input4_tag_entry.grid(column=3, row=4, sticky=EW)
    input4_tag_label = ttk.Label(inputs, text="Tag: ")
    input4_tag_label.grid(column=2, row=4, sticky=W, padx=10)

    output_file = StringVar()
    output_entry = ttk.Entry(inputs, width=30, textvariable=output_file)
    output_entry.grid(column=1, row=5, sticky=EW)
    output_label = ttk.Label(inputs, text="Output path: ")
    output_label.grid(column=0, row=5, sticky=W, padx=10)

    b2 = ttk.Button(mainframe, text="< Back",
                    command=partial(utils.reset_to_menu, mainframe))
    b2.grid(column=0, row=0, sticky=W)

    tags = [input1_tag, input2_tag, input3_tag, input4_tag]
    b1 = ttk.Button(mainframe, text="Stack!",
                    command=lambda: tasks.stack_videos(input1_entry.get(),
                                                       input2_entry.get(),
                                                       input3_entry.get(),
                                                       input4_entry.get(),
                                                       [tag.get()
                                                        for tag in tags],
                                                       output_entry.get(),
                                                       mainframe))
    b1.grid(column=3, row=2, sticky=W)


def init_window(mainframe):
    ttk.Label(mainframe, text="What do you want to do?").grid(column=1, row=0,
                                                              sticky=W)
    options = ttk.Frame(mainframe, padding="3 3 12 12")
    options.grid(column=1, row=1)

    b1 = ttk.Button(options, text="Convert resolution",
                    command=partial(convert_res, mainframe))
    b1.grid(column=0, row=1, sticky=W)

    b2 = ttk.Button(options, text="Convert codec",
                    command=partial(convert_codec, mainframe))
    b2.grid(column=1, row=1, sticky=W)

    b3 = ttk.Button(options, text="Stack 4 videos",
                    command=partial(stack_4_videos, mainframe))
    b3.grid(column=2, row=1, sticky=W)


def main():
    root = Tk()
    root.title("Video Converter")

    mainframe = ttk.Frame(root, padding="3 3 12 12")
    mainframe.grid(column=0, row=0, sticky=NSEW)
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)

    init_window(mainframe)

    for child in mainframe.winfo_children():
        child.grid_configure(padx=5, pady=5)

    root.mainloop()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
