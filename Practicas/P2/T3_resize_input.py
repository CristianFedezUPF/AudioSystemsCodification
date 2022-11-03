import math
import os


# reusing different resize video/audio commands from other exercises,
# with a 'decision tree' from user input
def task3(input_path: str, output_path: str):
    command = ""
    option = int(input("Do you want to resize video (0) or audio (1)? -> "))
    if option == 0:
        keep_aspect = int(input("Do you want to keep the aspect ratio of the"
                                " input (0) or resize to any value (1) -> "))
        if keep_aspect == 0:
            width_or_height = int(input("Do you want to modify width (0)"
                                        " or height (1) -> "))
            if width_or_height not in (0, 1):
                print("Incorrect option, returning...")
                return
            # round value down to nearest even number
            value = str(
                math.floor(int(input("Input desired value -> ")) / 2) * 2)
            if width_or_height == 0:
                command = "ffmpeg -i " + input_path + " -vf scale=" + value \
                          + ":-2 -c:a copy " + output_path
            if width_or_height == 1:
                command = "ffmpeg -i " + input_path + " -vf scale=-2:" + value \
                          + " " + output_path
        elif keep_aspect == 1:
            width = str(math.floor(int(input("Input width -> ")) / 2) * 2)
            height = str(math.floor(int(input("Input height -> ")) / 2) * 2)
            command = "ffmpeg -i " + input_path + " -vf scale=" + width + ":" \
                      + height + " " + output_path
        else:
            print("Incorrect option, returning...")
            return
    elif option == 1:
        value = input("Input bitrate -> ")
        command = "ffmpeg -i " + input_path + " -b:a " + value + "k " \
                  + output_path
    else:
        print("Incorrect option, returning...")
        return
    os.system(command)


if __name__ == "__main__":
    print("You should run main.py file")
