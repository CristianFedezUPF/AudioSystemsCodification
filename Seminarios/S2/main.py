import T1_cutN
import T2_yuv_histogram
import T3_resize_video
import T4_switch_stereo_mono
import textwrap

# ! before starting script make sure you have a bbb.mp4 file, or change the
# filename below
input_path = "bbb.mp4"

option = ""
while not (option == "q" or option == "Q"):
    print(textwrap.dedent("""\
            Task 1: Trim video duration
            Task 2: Overlay YUV histogram on top of video
            Task 3: Resize video
            Task 4: Convert from stereo to mono or from mono to stereo"""))
    option = input("Choose 1, 2, 3, 4 for tasks or 'q' to exit: ")
    if option == "1":
        T1_cutN.task1(input_path)
    elif option == "2":
        T2_yuv_histogram.task2(input_path)
    elif option == "3":
        T3_resize_video.task3(input_path)
    elif option == "4":
        T4_switch_stereo_mono.task4(input_path)
    elif option != "q" and option != "Q":
        print("Invalid option")
print("Thanks! Bye!")
