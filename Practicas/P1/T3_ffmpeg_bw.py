import ffmpeg
input_image_path = "aloy.jpg"
output_image_path = "aloy_bw.jpg"


def img_bw(input_path, output_path, width):
    """Use FFMPEG to convert image to black and white, also resizes
    to desired width, keeping aspect ratio.

     Input:
            input_path (String) - where the image is stored
            output_path (String) - where the resulting image should be stored
            width (Int) - desired width
    """
    (
        ffmpeg
        .input(input_path)
        .filter("format", "gray")
        .filter("scale", width, -1)
        .output(output_path)
        .run(cmd='/usr/local/bin/ffmpeg')
        # cmd path to ffmpeg installation so that PyCharm on MacOS detects it
    )


img_bw(input_image_path, output_image_path, 1024)
print("The image is converted in a satisfactory way to grayscale, and ffmpeg" +
      "already applies the hardest JPEG compression it can.\nWe can see some" +
      " JPEG artifacting if we zoom in on the image")
