import os


# Cut N seconds, similar to task 1from Seminar 2, cuts video and removes audio
def cut_n_seconds(input_path: str, output_path: str, start, end):
    """
    :param input_path
    :param output_path
    :param start: Starting time in format hh:mm:ss or in seconds (int or str)
    :param end: Ending time in format hh:mm:ss or in seconds (int or str)
    :return: None
    """
    command = "ffmpeg -ss " + str(start) + " -to " + str(end) + " -i " \
              + input_path \
              + " -c copy -an " + output_path
    os.system(command)


# https://trac.ffmpeg.org/wiki/Encode/MP3 quality settings with -b:a <bitrate>
def task2(input_path: str):
    cut_path = input_path.split(".")[0] + "cut.mp4"
    time = 60
    # cut 60 seconds of video and remove audio
    cut_n_seconds(input_path, cut_path, 0, time)
    # cut 60 seconds of audio to MP3 file 256kbps
    command1 = "ffmpeg -i " + input_path + \
               " -ss 00:00:00 -to " + str(time) + \
               " -b:a 256k -map 0:a:0 outputT2.mp3"
    os.system(command1)
    # cut 60 seconds of audio to AAC file 96kbps
    command2 = "ffmpeg -i " + input_path + \
               " -ss 00:00:00 -to " + str(time) + \
               " -b:a 96k -map 0:a:0 outputT2.aac"
    os.system(command2)
    # create container with video and both audios, don't reencode
    command3 = "ffmpeg -i " + cut_path \
               + " -i outputT2.mp3 -i outputT2.aac" \
                 " -map 0 -map 1 -map 2 -codec  copy outputT2.mp4"
    os.system(command3)


if __name__ == "__main__":
    print("You should run main.py file")
