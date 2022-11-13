import os


def task3(input1: str, input2: str, input3: str, input4: str, tags: list,
          output_path: str, crf=25, preset_idx=5):
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
    print("You should perhaps run main.py file")
    task3("bbb720/bbb720VP8.mkv", "bbb720/bbb720VP9.mkv",
          "bbb720/bbb720HEVC.mkv", "bbb720/bbb720AV1.mkv",
          ["VP8", "VP9", "HEVC", "AV1"], "bbb720_comparison.mkv")
