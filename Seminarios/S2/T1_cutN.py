import os

# Command is:
# ffmpeg -ss 00:01:00 -to 00:02:00 -i input.mp4 -c copy output.mp4
"""
-i: This specifies the input file. In that case, it is (input.mp4). 
-ss: Used with -i, this seeks in the input file (input.mp4) to position. 
00:01:00: This is the time your trimmed video will start with. 
-to: This specifies duration from start (00:01:40) to end (00:02:12). 
00:02:00: This is the time your trimmed video will end with. 
-c copy: This is an option to trim via stream copy. (NB: Very fast)
 """


def task1(input_path):
    print("Task 1 - Cut video")
    output_path = "output_T1.mp4"
    start = input("Input starting time in format hh:mm:ss or in seconds -> ")
    end = input("Input ending time in format hh:mm:ss or in seconds -> ")

    command = "ffmpeg -ss " + start + " -to " + end + " -i " \
              + input_path \
              + " -c copy " + output_path
    os.system(command)
