import os


def task3(input_path):
    output_path = "output_T3.mp4"

    height = input("Write 720, 480, 240 or 120, for 720p, 480p, 360x240 or " +
                   "160x120, or any other number for the vertical resolution" +
                   "(will be 16:9): -> ")
    if height == "360":
        width = str(240)
    elif height == "120":
        width = str(160)
    else:
        width = str(int(height) * 16 / 9)

    # applies -vf (videofilter) scale to resize video to desired size
    command = "ffmpeg -i " + input_path + " -vf scale=" + width + ":" \
              + height + " " + output_path
    os.system(command)
