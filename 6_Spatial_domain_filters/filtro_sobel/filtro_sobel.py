import matplotlib.pyplot as plt
import imageio
from scipy import signal
import numpy as np
def aplicar_filtro_sobel(imagen_str):
    # Esta función toma una imagen y aplica sobre esta la convolución con
    # el kernel tipico del filtro Laplaciano.
    # Entradas: - imagen_str: la ruta de la imagen deseada.
    # Salidas: la imagen con la convolución aplicada.
    # Leyendo la imagen.
    A = imageio.imread(imagen_str)
    # Tomando el kernel para filtrar los bordes horizontales.
    Bx = [[-1, -2, -1],
          [0, 0, 0],
          [1, 2, 1]]
    # Tomando el kernel para filtrar los bordes verticales.
    By = [[-1, 0, 1],
          [-2, 0, 2],
          [-1, 0, 1]]
    # Aplicando el filtro de bordes horizontales.
    Cx = signal.convolve2d(A, Bx)
    # Aplicando el filtro de bordes verticales.
    Cy = signal.convolve2d(A, By)
    # Obteniendo las distancias entre los bordes horizontales y verticales.
    C = np.sqrt(np.square(Cx) + np.square(Cy))
    # Convirtiendo la imagen resultante a tipo uint8.
    C = C.astype(np.uint8)
    return C
# Probando el filtro Sobel.
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
