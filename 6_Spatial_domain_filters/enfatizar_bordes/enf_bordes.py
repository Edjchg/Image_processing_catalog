import matplotlib.pyplot as plt
import imageio
from scipy import signal
import numpy as np
def filtro_laplaciano(imagen):
    # Esta función toma una imagen y aplica sobre esta la convolución con
    # el kernel tipico del filtro Laplaciano.
    # Entradas: - imagen_str: la ruta de la imagen deseada.
    # Salidas: la imagen con la convolución aplicada.
    # Leyendo la imagen.
    # Tomando el kernel tipico del filtro Laplaciano.
    B = [[1, 1, 1],
         [1, -8, 1],
         [1, 1, 1]]
    return signal.convolve2d(imagen, B, mode="same",boundary="symm", fillvalue=0)
def enfatizar_bordes(imagen_str, c):
    # Esta función toma una imagen y enfatiza sus bordes mediante el filtro
    # Laplaciano.
    # Enrtradas: - imagen_str: ruta de la imagen deseada.
    #            - c: factor de intensidad de los bordes resaltados.
    # Salidas: - Imagen con los bordes enfatizados.
    # Leyendo la imagen.
    A = imageio.imread(imagen_str)
    # Aplicando el filtro del Laplaciano.
    B = filtro_laplaciano(A)
    # Aplicando la formula para enfatizar los bordes de la iamgen.
    C = A + c*B
    return C
# Pribando enfatizacion de bordes con el filtro del Laplaciano.
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



