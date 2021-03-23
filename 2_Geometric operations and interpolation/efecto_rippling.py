import imageio
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import math


def efecto_rippling(imagen):
    A = Image.open(imagen)
    A = A.resize((128, 128), Image.ANTIALIAS)
    A.save("barbara1.jpg")
    A = imageio.imread("barbara1.jpg")
    m = len(A)
    n = len(A[0])
    r = len(A[0][0])

    theta = math.pi / 4

    x_c = m // 2
    y_c = n // 2
    B = np.zeros((m, n, r), dtype=np.uint8)
    #B = np.zeros((m, n, r))
    frames = 50
    Y = np.zeros((m, n, r, frames), dtype=np.uint8)
    #Y = np.zeros((m, n, r, frames))
    L_x = L_y = 75
    A_x = A_y = 5

    for i in range(0, 10):
        Y[:, :, 0, i] = A[:, :, 0]
        Y[:, :, 1, i] = A[:, :, 1]
        Y[:, :, 2, i] = A[:, :, 2]

    while A_y < 200:
        i += 1
        for x in range(1, m):
            for y in range(1, n):
                a_0 = math.cos(theta)
                a_1 = math.sin(theta)
                a_2 = x_c - a_0 * x_c - a_1 * y_c
                x_t = round(x + A_x * math.sin(2 * math.pi * y / L_x))
                b_0 = -math.sin(theta)
                b_1 = math.cos(theta)
                b_2 = y_c - b_0 * x_c - b_1 * y_c
                y_t = round(y + A_y * math.sin(2 * math.pi * x / L_y))

                if 0 <= x_t < m and 0 <= y_t < n:
                    B[x_t, y_t, :] = A[x, y, :]

        Y[:, :, 0, i] = B[:, :, 0]
        Y[:, :, 1, i] = B[:, :, 1]
        Y[:, :, 2, i] = B[:, :, 2]
        A_x += 5
        A_y += 5

    video = imageio.get_writer("video_salida.mp4")
    for i in range(0, 50):
        video.append_data(Y[:, :, :, i])
    video.close()
    
efecto_rippling("barbara.jpg")

