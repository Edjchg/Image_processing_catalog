import matplotlib.pyplot as plt
import imageio
from scipy import signal
import numpy as np


def aplicar_filtro_sobel(imagen_str):
    A = imageio.imread(imagen_str)

    Bx = [[-1, -2, -1],
          [0, 0, 0],
          [1, 2, 1]]

    By = [[-1, 0, 1],
          [-2, 0, 2],
          [-1, 0, 1]]

    Cx = signal.convolve2d(A, Bx)
    Cy = signal.convolve2d(A, By)
    C = np.sqrt(np.square(Cx) + np.square(Cy))
    C = C.astype(np.uint8)
    return C


A = imageio.imread("baby_yoda.jpg")
B = aplicar_filtro_sobel("baby_yoda.jpg")
plt.figure()
plt.subplot(121)
plt.title("Imagen original")
plt.imshow(A, cmap='gray')
plt.subplot(122)
plt.title("Filtro Sobel")
plt.imshow(B, cmap='gray')
plt.show()
