import matplotlib.pyplot as plt
import imageio
from scipy import ndimage
import numpy as np


def aplicar_filtro_gauss(imagen_str):
    A = imageio.imread(imagen_str)
    B = (1/16)*np.array([[1, 2, 1], [2, 4, 2], [1, 2, 1]])
    print(B)
    C = ndimage.convolve(A, B, mode='constant', cval=1.0)
    return C

A = imageio.imread("boat.jpg")
B = aplicar_filtro_gauss("boat.jpg")
plt.figure()
plt.subplot(121)
plt.title("Imagen original")
plt.imshow(A, cmap='gray')
plt.subplot(122)
plt.title("Filtro Gaussiano")
plt.imshow(B, cmap='gray')
plt.show()
