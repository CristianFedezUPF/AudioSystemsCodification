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


# https://trac.ffmpeg.org/wiki/Encode/MP3 quality
def task2(input_path: str):
    cut_path = input_path.split(".")[0] + "cut.mp4"
    time = 10
    cut_n_seconds(input_path, cut_path, 0, time)
    command1 = "ffmpeg -i " + input_path + \
               " -ss 00:00:00 -to " + str(time) + \
               " -b:a 256k -map a outputT2.mp3"
    os.system(command1)
    command2 = "ffmpeg -i " + input_path + \
               " -ss 00:00:00 -to " + str(time) + \
               " -b:a 96k -map a outputT2.aac"
    os.system(command2)
    command3 = "ffmpeg -i " + cut_path \
               + " -i outputT2.mp3 -i outputT2.aac" \
                 " -map 0 -map 1 -map 2 -codec  copy outputT2.mp4"
    os.system(command3)
