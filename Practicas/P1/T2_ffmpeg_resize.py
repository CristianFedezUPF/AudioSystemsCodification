import ffmpeg


# !Uses ffmpeg-python module since lab instructions specified to use only Python
def img_resize(input_path, output_path, width):
    """"Use FFMPEG to resize image to the given width, respecting aspect ratio

        Input:
            input_path (String) - where the image is stored
            output_path (String) - where the resulting image should be stored
            width (Int) - desired with
    """
    (
        ffmpeg
        .input(input_path)
        .filter("scale", width, -1)
        .output(output_path)
        .run(cmd='/usr/local/bin/ffmpeg')
        # c md path to ffmpeg installation so that PyCharm on MacOS detects it
    )


input_image_path = "aloy.jpg"
w = 1024
output_image_path = "aloy" + str(w) + ".jpg"
img_resize(input_image_path, output_image_path, w)

w = 512
output_image_path = "aloy" + str(w) + ".jpg"
img_resize(input_image_path, output_image_path, w)

w = 256
output_image_path = "aloy" + str(w) + ".jpg"
img_resize(input_image_path, output_image_path, w)
