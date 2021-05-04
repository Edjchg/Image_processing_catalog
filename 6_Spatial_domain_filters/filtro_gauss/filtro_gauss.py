import matplotlib.pyplot as plt
import imageio
from scipy import ndimage
import numpy as np
def aplicar_filtro_gauss(imagen_str):
    # Esta función toma una imagen y aplica sobre esta la convolución con
    # el kernel tipico del filtro gaussiano.
    # Entradas: - imagen_str: la ruta de la imagen deseada.
    # Salidas: la imagen con la convolución aplicada.
    # Leyendo la imagen.
    A = imageio.imread(imagen_str)
    # Calculando el kernel tipico del filtro de Gauss.
    B = (1/16)*np.array([[1, 2, 1], [2, 4, 2], [1, 2, 1]])
    # Aplicando la convolución a las matrices de A y B.
    C = ndimage.convolve(A, B, mode='constant', cval=1.0)
    return C
# Probando el filtro de Gauss.
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
