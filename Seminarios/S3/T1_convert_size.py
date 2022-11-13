import os

"""
Converts input file to 4 size options using console input, 720p, 480p,
360x240 or 160x120.
"""


def task1(input_path: str):
    if not os.path.isfile(input_path):
        print("Input file not found.")
        return
    option = -1
    output_path = input_path.split(".")[0]
    command = ""
    while option not in ("1", "2", "3", "4"):
        option = input("Convert to: 720p (1), 480p (2),"
                       " 360x240 (3), 160x120 (4): ")
    if option == "1":
        output_path += "720.mp4"
        command = "ffmpeg -i " + input_path + " -vf scale=1280:720 -c:a copy "\
                  + output_path
    elif option == "2":
        output_path += "480.mp4"
        command = "ffmpeg -i " + input_path + " -vf scale=640:480 -c:a copy "\
                  + output_path
    elif option == "3":
        output_path += "360x240.mp4"
        command = "ffmpeg -i " + input_path + " -vf scale=360:240 -c:a copy "\
                  + output_path
    elif option == "4":
        output_path += "160x120.mp4"
        command = "ffmpeg -i " + input_path + " -vf scale=160:120 -c:a copy " \
                  + output_path
    os.system(command)


if __name__ == "__main__":
    input1 = input("Type the path of your input video here: ")
    task1(input1)
