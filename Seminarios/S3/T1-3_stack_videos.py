import os

"""
Stacks 4 video files, by default CRF (Constant Rate Factor, 
which defines quality) of output file = 25, preset HEVC 'medium'.
crf -> [5, 50]
preset_idx -> [0, 9]
presets = ["ultrafast", "superfast", "veryfast", "faster", "fast",
                   "medium", "slow", "slower", "veryslow", "placebo"]
"""


def task3(input1: str, input2: str, input3: str, input4: str, tags: list,
          output_path: str, crf=25, preset_idx=5):
    if not (os.path.isfile(input1) or
            os.path.isfile(input2) or
            os.path.isfile(input3) or
            os.path.isfile(input4)):
        print("One or more of the files were not found. Try again.")
        return
    if not 5 <= crf <= 50:
        print("CRF needs to be between 5 and 50.")
        return
    if not 0 <= preset_idx <= 9:
        print("HEVC preset needs to be between 0-9 to go "
              "from 'ultrafast' to 'placebo'")
        return
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


if __name__ == "__main__":
    input_path1 = input("Type the first video path here: ")
    tag1 = input("Type the first video tag (tags will appear "
                 "in the top left of every video) here: ")
    input_path2 = input("Type the second video path here: ")
    tag2 = input("Type the second video tag here: ")
    input_path3 = input("Type the third video path here: ")
    tag3 = input("Type the third video tag here: ")
    input_path4 = input("Type the fourth video path here: ")
    tag4 = input("Type the fourth video tag here: ")
    tags = [tag1, tag2, tag3, tag4]

    output = input("Type the output file path here: ")
    task3(input_path1, input_path2, input_path3, input_path4,
          tags, output)
