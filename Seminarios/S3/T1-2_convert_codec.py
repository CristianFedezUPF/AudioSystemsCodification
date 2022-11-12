import os


def task2(input_path: str):
    first_options = ["VP8", "VP9", "HEVC", "AV1"]
    output_path = input_path.split(".")[0]
    command = ""
    option = ""
    max_allowed_bitrate = 8  # MBPS
    while option not in ("1", "2", "3", "4"):
        option = input("Convert to: VP8 (1), VP9 (2),"
                       " HEVC (3), AV1 (4): ")
    if option == "1":
        crf = 25
        output_path += "VP8.mkv"
        command = "ffmpeg -i " + input_path + " -c:v libvpx -crf " \
                  + str(crf) + " -b:v " + str(max_allowed_bitrate) \
                  + "M -c:a libvorbis " + output_path
        os.system(command)
        print("Converted to VP8 at Variable Bitrate at constant quality mode "
              "CRF = 25, max bitrate allowed 8 MB/s (recommmended mode), "
              "audio in Vorbis")
    if option == "2":
        crf = 25
        output_path += "VP9.mkv"
        command1 = "ffmpeg -i " + input_path + " -c:v libvpx-vp9 -b:v 0 " \
            + "-crf " + str(crf) + " -pass 1 -an -f null /dev/null"
        command2 = "ffmpeg -i " + input_path + " -c:v libvpx-vp9 -b:v 0 " \
            + "-crf " + str(crf) + " -pass 2 -c:a libvorbis " + output_path
        command = command1 + " && " + command2
        os.system(command)
        print("Converted to VP9 at Two Pass constant quality mode "
              "CRF = 25 (recommmended mode), "
              "audio in Vorbis")
    if option == "3":
        crf = 25
        output_path += "HEVC.mkv"
        presets = ["ultrafast", "superfast", "veryfast", "faster", "fast",
                   "medium", "slow", "slower", "veryslow", "placebo"]
        command = "ffmpeg -i " + input_path + " -c:v libx265 -crf " \
            + str(crf) + " -preset " + presets[5] + " -c:a libvorbis " \
            + output_path
        os.system(command)
        print("Converted to HEVC at Constant Rate Factor (constant quality) at"
              " 'medium' compression efficiency preset, "
              "CRF = 25 (recommmended mode), audio in Vorbis")
    if option == "4":
        crf = 25
        output_path += "AV1.mkv"
        command1 = "ffmpeg -i " + input_path + " -c:v libaom-av1 -crf " \
            + str(crf) + " -b:v 0 -g 300 -tile-columns 2 -tile-rows 2" \
            " -row-mt 1 -threads 8 -cpu-used 6 -pass 1 -an -f null /dev/null"
        command2 = "ffmpeg -i " + input_path + " -c:v libaom-av1 -crf " \
            + str(crf) + " -b:v 0 -g 300 -tile-columns 2 -tile-rows 2" \
            " -row-mt 1 -threads 8 -cpu-used 6 -pass 2 " \
            "-c:a libvorbis " + output_path
        command = command1 + " && " + command2
        os.system(command)
        print("Converted to AV1 at Two Pass constant quality mode "
              "CRF = 25 (recommmended mode), speed preset 6 (faster,"
              " default is 1), 2x2 tiles for multithreading,"
              " audio in Vorbis")


if __name__ == "__main__":
    print("You should perhaps run main.py file")
    task2("bbb720/bbb720.mp4")
