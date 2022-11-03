import os


# help from https://stackoverflow.com/a/29610897
# Command takes output from ffprobe, greps to get the lines which have stream
# info for 'Audio' and further searches using 'sed' to return only the codec.
# popen().read() executes command and returns command line output
# which is stored in a variable
def task4(input_path):
    command_audio = "ffprobe -i " + input_path + " -show_format -pretty " \
                    "2>&1 >/dev/null | grep Stream.*Audio" \
                    " | sed -e 's/.*Audio: //' -e 's/[, ].*//'"
    audios = os.popen(command_audio).read().split("\n")
    audios.remove("")
    print("File audio tracks: " + ", ".join(audios))
    command_video = "ffprobe -i " + input_path + " -show_format -pretty " \
                    "2>&1 >/dev/null | grep Stream.*Video" \
                    " | sed -e 's/.*Video: //' -e 's/[, ].*//'"
    videos = os.popen(command_video).read().split("\n")
    videos.remove("")
    print("File video tracks: " + ", ".join(videos))
    print()
    check_broadcasting_standards(audios, videos)


# finds if audio and video codecs found comply with diff broadcasting standards
def check_broadcasting_standards(audio_list: list, video_list: list):
    dvb_audio = ["aac", "ac3", "mp3"]
    dvb_video = ["mpeg2video", "h264"]
    isdb_audio = ["aac"]
    isdb_video = ["mpeg2video", "h264"]
    atsc_audio = ["ac3"]
    atsc_video = ["mpeg2video", "h264"]
    dtmb_audio = ["dra", "aac", "ac3", "mp2", "mp3"]
    dtmb_video = ["mpeg2video", "h264", "avs", "avs+"]
    audio_stds = []
    check_compliance(audio_list, dvb_audio, "DVB", audio_stds)
    check_compliance(audio_list, isdb_audio, "ISDB", audio_stds)
    check_compliance(audio_list, atsc_audio, "ATSC", audio_stds)
    check_compliance(audio_list, dtmb_audio, "DTMB", audio_stds)
    print("File audio is compliant with: " + ", ".join(audio_stds))

    video_stds = []
    check_compliance(video_list, dvb_video, "DVB", video_stds)
    check_compliance(video_list, isdb_video, "ISDB", video_stds)
    check_compliance(video_list, atsc_video, "ATSC", video_stds)
    check_compliance(video_list, dtmb_video, "DTMB", video_stds)
    print("File video is compliant with: " + ", ".join(video_stds))
    output = set(audio_stds).intersection(set(video_stds))
    print("Overall, file is fully compliant with: " + ", ".join(output))


def check_compliance(file_codecs: list, bcast_codecs: list,
                     broadcast: str, standards: list):
    if [i for i in file_codecs if i in bcast_codecs]:
        standards.append(broadcast)


if __name__ == "__main__":
    print("You should run main.py file")
