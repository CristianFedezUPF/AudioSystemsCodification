import os


def task4(input_path):
    output_path = "output_T4.mp4"

    option = input("Write 1 to convert your file to mono," +
                   " 2 to convert your file to stereo: -> ")

    command = ""
    if option == "1":
        # -af filtergraph brings stereo in phase before downmixing
        # -c:v copy so that it directly copies the video part (much faster)
        # -ac 1 converts to mono (1 audio channel)
        command = "ffmpeg -i " + input_path + " -ac 1 " \
                    "-af \"asplit[a]," \
                    "aphasemeter=video=0,ametadata=select:" \
                    "key=lavfi.aphasemeter.phase:value=-0.005:function=less," \
                    "pan=1c|c0=c0,aresample=async=1:first_pts=0,[a]amix\" " \
                    "-c:v copy " \
                  + output_path
    if option == "2":
        # basically copies mono file to both channels
        # -ac 2 converts to stereo (2 audio channels)
        command = "ffmpeg -i " + input_path + " -ac 2 " + "-c:v copy "\
                  + output_path

    os.system(command)


"""
Images attached to delivery from Sonic Visualizer, original stereo signal
(audio channels are different signals),
stereo to mono signal, (stereo channels mixed to one single channel), 
mono to stereo signal,
(convert previous mono signal to stereo, mono channel is replicated in both)
"""
