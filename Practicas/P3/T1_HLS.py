import os

# command from this tutorial:
# https://ottverse.com/hls-packaging-using-ffmpeg-live-vod/


def task1(input_path: str):
    # Read input and convert to multiple resolutions
    command = "ffmpeg -i " + input_path + \
              " -filter_complex \"[0:v]split=3[v1][v2][v3]; " \
              "[v1]copy[v1out]; " \
              "[v2]scale=w=854:h=480[v2out]; " \
              "[v3]scale=w=480:h=360[v3out]\" "
    # Transcode videos to different bitrates
    command += "-map [v1out] -c:v:0 libx264 -x264-params " \
               "\"nal-hrd=cbr:force-cfr=1\" -b:v:0 5M -maxrate:v:0 5M " \
               "-minrate:v:0 5M -bufsize:v:0 10M -preset slow -g 48 " \
               "-sc_threshold 0 -keyint_min 48 "
    command += "-map [v2out] -c:v:1 libx264 -x264-params " \
               "\"nal-hrd=cbr:force-cfr=1\" -b:v:1 3M -maxrate:v:1 3M " \
               "-minrate:v:1 3M -bufsize:v:1 3M -preset slow -g 48 " \
               "-sc_threshold 0 -keyint_min 48 "
    command += "-map [v3out] -c:v:2 libx264 -x264-params " \
               "\"nal-hrd=cbr:force-cfr=1\" -b:v:2 1M -maxrate:v:2 1M " \
               "-minrate:v:2 1M -bufsize:v:2 1M -preset slow -g 48 " \
               "-sc_threshold 0 -keyint_min 48 "
    # Audio as well
    command += "-map a:0 -c:a:0 aac -b:a:0 96k -ac 2 " \
               "-map a:0 -c:a:1 aac -b:a:1 96k -ac 2 " \
               "-map a:0 -c:a:2 aac -b:a:2 48k -ac 2 "
    # Create HLS Playlists (m3u8)
    command += "-f hls \
                -hls_time 2 \
                -hls_playlist_type vod \
                -hls_flags independent_segments \
                -hls_segment_type mpegts \
                -hls_segment_filename stream_%v/data%02d.ts \
                -master_pl_name master.m3u8 \
                -strftime_mkdir 1 \
                -var_stream_map \"v:0,a:0 v:1,a:1 v:2,a:2\" stream_%v.m3u8"

    os.system(command)


if __name__ == "__main__":
    input_path = ""
    valid_path = False
    while not valid_path:
        input_path = input("Input the path to your file here: ")
        valid_path = os.path.isfile(input_path)
        if not valid_path:
            print("File not found, try again.")
    task1(input_path)
