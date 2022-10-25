# I followed Wikipedia site for DCT-IV and MD-DCT IV
# https://en.wikipedia.org/wiki/Discrete_cosine_transform
# and this page
# https://arm-software.github.io/CMSIS_5/DSP/html/group__DCT4__IDCT4.html
import numpy as np


def dct(array: np.ndarray):
    """Implementation of the 1D DCT-IV"""
    def _inner_iter():
        summation = 0
        for j in range(0, n):
            summation += array[j] * np.cos(
                (np.pi / n) * (j + 1 / 2) * (i + 1 / 2))
        return (2 / n) ** (1 / 2) * summation

    n = len(array)
    output = [0] * n
    for i in range(0, n):
        output[i] = _inner_iter()
    return output


def idct(array):
    # The DCT4 matrices become involutory (i.e. they are self-inverse) by
    # multiplying with an overall scale factor of sqrt(2/N)
    return dct(array)


def dct2(matrix: np.ndarray):
    """Implementation of the Multi-Dimensional DCT-IV"""
    def _inner_iter():
        summation = 0
        for n in range(0, rows):
            for m in range(0, cols):
                summation += matrix[n][m] * \
                             np.cos((2*m + 1)*(2*i + 1)*np.pi/(4*rows)) * \
                             np.cos((2*n + 1)*(2*j + 1)*np.pi/(4*cols))

        return summation

    size = np.shape(matrix)
    rows = size[0]
    cols = size[1]
    output = np.zeros_like(matrix)
    for i in range(0, rows):
        for j in range(0, cols):
            output[i][j] = _inner_iter()
    return output


np.set_printoptions(suppress=True)  # prevent numpy scientific notation

ex = np.array([235, 230, 239, 240, 210, 180, 210])
ex_o = dct(ex)
print("*** 1D DCT ***")
print("Original array:")
print(ex)
print()
print("DCT array:")
print(np.round(ex_o, 3))
print("See how the DCT concentrates " +
      "most information in the first coefficients")
print()
print("Inverse DCT:")
print(np.round(idct(ex_o), 3))
print()

print("*** 2D DCT ***")
ex2 = np.array([[235, 230, 239, 240, 210, 180, 210],
                [235, 230, 239, 240, 210, 180, 210],
                [235, 230, 239, 240, 210, 180, 210],
                [235, 230, 239, 240, 210, 180, 210],
                [235, 230, 239, 240, 210, 180, 210]])
ex2_o = dct2(ex2)
print("Original array:")
print(ex2)
print()
print("DCT array:")
print(np.round(ex2_o, 3))
