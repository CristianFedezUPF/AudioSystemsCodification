# Exercises by Cristian Fernandez Moreno
# NIA: 229611
def rgb_to_yuv(rgb):
    """Converts a RGB list or tuple to YUV values using the known formulas.
        Output is rounded (screens can't display decimal values)

        Input: rgb - List or Tuple
        Output: Tuple of YUV values
    """
    r = rgb[0]
    g = rgb[1]
    b = rgb[2]
    y = 0.257 * r + 0.504 * g + 0.098 * b + 16
    u = -0.148 * r - 0.291 * g + 0.439 * b + 128
    v = 0.439 * r - 0.368 * g - 0.071 * b + 128
    return round(y), round(u), round(v)


def yuv_to_rgb(yuv):
    """Converts a YUV list or tuple to RGB values using the known formulas.
        Output is rounded (screens can't display decimal values)

        Input: yuv - List or Tuple
        Output: Tuple of RGB values
    """
    y = yuv[0]
    u = yuv[1]
    v = yuv[2]
    r = 1.164 * (y - 16) + 1.596 * (v - 128)
    g = 1.164 * (y - 16) - 0.813 * (v - 128) - 0.391 * (u - 128)
    b = 1.164 * (y - 16) + 2.018 * (u - 128)
    return round(r), round(g), round(b)


# Examples
rgb_sample = (255, 255, 255)
print("Original RGB value: ")
print(rgb_sample)
yuv_sample = rgb_to_yuv(rgb_sample)
print("Converted YUV value: ")
print(yuv_sample)
rgb_converted = yuv_to_rgb(yuv_sample)
print("Conversion back to RGB: ")
print(rgb_converted)

print("\n")

# Examples
rgb_sample = (28, 157, 47)
print("Original RGB value: ")
print(rgb_sample)
yuv_sample = rgb_to_yuv(rgb_sample)
print("Converted YUV value: ")
print(yuv_sample)
rgb_converted = yuv_to_rgb(yuv_sample)
print("Conversion back to RGB: ")
print(rgb_converted)
