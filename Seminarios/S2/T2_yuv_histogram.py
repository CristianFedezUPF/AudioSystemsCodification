import os

# Command is:
# ""ffpmpeg -i input.mp4 -vf "split=2[a][b],
# [b]histogram,format=yuva444p[hh],[a][hh]overlay"
# output.mp4""


def task2(input_path):
    # takes input video and YUV histogram and overlays them
    print("Task 2 - Overlay YUV histogram")
    output_path = "output_T2.mp4"
    command = "ffmpeg -i " + input_path + " -vf split=2[a][b]," + \
              "[b]histogram,format=yuva444p[hh],[a][hh]overlay " + \
              output_path
    os.system(command)
