import os
from tkinter import *
import utils_tkinter as utils
from main import init_window


def convert_resolution(input_path: str, option: str, mainframe: Frame):
    if not os.path.isfile(input_path):
        utils.append_message_frame(mainframe, "File not found, try again.",
                                   row=2, column=3, sticky=NSEW)
        return
    utils.show_message_frame(mainframe, "Converting...")
    output_path = input_path.split(".")[0]
    command = ""
    while option not in ("1", "2", "3", "4"):
        option = input("Convert to: 720p (1), 480p (2),"
                       " 360x240 (3), 160x120 (4): ")
    if option == "1":
        output_path += "720.mp4"
        command = "ffmpeg -i " + input_path + " -vf scale=1280:720 -c:a copy " \
                  + output_path
    elif option == "2":
        output_path += "480.mp4"
        command = "ffmpeg -i " + input_path + " -vf scale=640:480 -c:a copy " \
                  + output_path
    elif option == "3":
        output_path += "360x240.mp4"
        command = "ffmpeg -i " + input_path + " -vf scale=360:240 -c:a copy " \
                  + output_path
    elif option == "4":
        output_path += "160x120.mp4"
        command = "ffmpeg -i " + input_path + " -vf scale=160:120 -c:a copy " \
                  + output_path
    os.system(command)
    utils.clear_frame(mainframe)
    init_window(mainframe)


def convert_codec(input_path: str, option: str, mainframe: Frame,
                  crf=25, hevc_preset_idc=5):
    if not os.path.isfile(input_path):
        utils.append_message_frame(mainframe, "File not found, try again.",
                                   row=2, column=3, sticky=NSEW)
        return
    utils.show_message_frame(mainframe, "Converting...")
    output_path = input_path.split(".")[0]
    max_allowed_bitrate = 8  # MBPS
    if option == "1":
        output_path += "VP8.mkv"
        command = "ffmpeg -i " + input_path + " -c:v libvpx -crf " \
                  + str(crf) + " -b:v " + str(max_allowed_bitrate) \
                  + "M -c:a libvorbis " + output_path
        os.system(command)
        print("Converted to VP8 at Variable Bitrate at constant quality mode "
              "CRF = " + str(crf) + " , max bitrate allowed "
                                    "8 MB/s (recommmended mode), "
                                    "audio in Vorbis")
    if option == "2":
        output_path += "VP9.mkv"
        command1 = "ffmpeg -i " + input_path + " -c:v libvpx-vp9 -b:v 0 " \
                   + "-crf " + str(crf) + " -pass 1 -an -f null /dev/null"
        command2 = "ffmpeg -i " + input_path + " -c:v libvpx-vp9 -b:v 0 " \
                   + "-crf " + str(crf) + " -pass 2 -c:a libvorbis " \
                   + output_path
        command = command1 + " && " + command2
        os.system(command)
        print("Converted to VP9 at Two Pass constant quality mode "
              "CRF = " + str(crf) + " (recommmended mode), "
                                    "audio in Vorbis")
    if option == "3":
        output_path += "HEVC.mkv"
        presets = ["ultrafast", "superfast", "veryfast", "faster", "fast",
                   "medium", "slow", "slower", "veryslow", "placebo"]
        command = "ffmpeg -i " + input_path + " -c:v libx265 -crf " \
                  + str(crf) + " -preset " + presets[hevc_preset_idc] \
                  + " -c:a libvorbis " \
                  + output_path
        os.system(command)
        print("Converted to HEVC at Constant Rate Factor (constant quality) at "
              + presets[hevc_preset_idc] + " compression efficiency preset, "
              "CRF = " + str(crf) + " (recommmended mode), audio in Vorbis")
    if option == "4":
        output_path += "AV1.mkv"
        command1 = "ffmpeg -i " + input_path + " -c:v libaom-av1 -crf " \
                   + str(crf) + " -b:v 0 -g 300 -tile-columns 2 -tile-rows 2" \
                                " -row-mt 1 -threads 8 -cpu-used 6 " \
                                "-pass 1 -an -f null /dev/null"
        command2 = "ffmpeg -i " + input_path + " -c:v libaom-av1 -crf " \
                   + str(crf) + " -b:v 0 -g 300 -tile-columns 2 -tile-rows 2" \
                                " -row-mt 1 -threads 8 -cpu-used 6 -pass 2 " \
                                "-c:a libvorbis " + output_path
        command = command1 + " && " + command2
        os.system(command)
        print("Converted to AV1 at Two Pass constant quality mode "
              "CRF = " + str(crf) + " (recommmended mode),"
                                    " speed preset 6 (faster,"
                                    " default is 1), 2x2 tiles"
                                    " for multithreading,"
                                    " audio in Vorbis")
        utils.clear_frame(mainframe)
        init_window(mainframe)


def stack_videos(input1: str, input2: str, input3: str, input4: str, tags: list,
                 output_path: str, mainframe: Frame, crf=25, preset_idx=5):
    if not (os.path.isfile(input1) or
            os.path.isfile(input2) or
            os.path.isfile(input3) or
            os.path.isfile(input4)):
        utils.append_message_frame(mainframe, "File not found, try again.",
                                   row=2, column=3, sticky=NSEW)
        return
    utils.show_message_frame(mainframe, "Converting...")
    inputs = "ffmpeg" \
             " -i " + input1 + \
             " -i " + input2 + \
             " -i " + input3 + \
             " -i " + input4 + " "
    filters = "-filter_complex \""
    text1 = "[0]drawtext=text='" + tags[0] + "'" + \
            ":fontsize=20:x=5:y=5[v0]; "
    text2 = "[1]drawtext=text='" + tags[1] + "'" + \
            ":fontsize=20:x=5:y=5[v1]; "
    text3 = "[2]drawtext=text='" + tags[2] + "'" + \
            ":fontsize=20:x=5:y=5[v2]; "
    text4 = "[3]drawtext=text='" + tags[3] + "'" + \
            ":fontsize=20:x=5:y=5[v3]; "
    video_stack = "[v0][v1][v2][v3]xstack=inputs=4" \
                  ":layout=0_0|w0_0|0_h0|w0_h0[v]\" "

    filters += text1 + text2 + text3 + text4 + video_stack
    presets = ["ultrafast", "superfast", "veryfast", "faster", "fast",
               "medium", "slow", "slower", "veryslow", "placebo"]
    h265_options = "-c:v libx265 -crf " + str(crf) + " -preset " \
                   + presets[preset_idx] + " "
    output = "-map \"[v]\" -map 1:a " + h265_options + output_path
    command = inputs + filters + output
    os.system(command)
    utils.clear_frame(mainframe)
    init_window(mainframe)


if __name__ == "__main__":
    print("You should run main.py file")
