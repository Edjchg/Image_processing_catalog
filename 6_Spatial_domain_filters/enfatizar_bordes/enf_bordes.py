import matplotlib.pyplot as plt
import imageio
from scipy import signal
import numpy as np

def filtro_laplaciano(imagen):
    B = [[1, 1, 1],
         [1, -8, 1],
         [1, 1, 1]]
    return signal.convolve2d(imagen, B, mode="same",boundary="symm", fillvalue=0)

def enfatizar_bordes(imagen_str, c):
    A = imageio.imread(imagen_str)
    B = filtro_laplaciano(A)
    C = A + c*B
    return C


A = imageio.imread("baby_yoda.jpg")
B = enfatizar_bordes("baby_yoda.jpg", 4)
plt.figure()
plt.subplot(121)
plt.title("Imagen original")
plt.imshow(A, cmap='gray')
plt.subplot(122)
plt.title("Bordes enfatizados")
plt.imshow(B, cmap='gray')
plt.show()



