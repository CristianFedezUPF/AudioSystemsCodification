import os

# use ffprobe which is bundled with ffmpeg
# ffprobe gathers information from multimedia streams and prints it in human-
# and machine-readable fashion.
# Command is: "ffprobe -i input.mp4 -show_format -pretty"


def task1(input_path):
    command = "ffprobe -i " + input_path + " -show_format -pretty"
    os.system(command)


if __name__ == "__main__":
    print("You should run main.py file")
