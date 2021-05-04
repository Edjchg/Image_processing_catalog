import numpy as np
import matplotlib.pyplot as plt
import imageio
from scipy import ndimage
def convolucion_2D(A, B):
    # La función de convolución permite obtener la operación de convolucion
    # discreta entre dos matrices.
    # Entradas: - A: en general acá iría la matriz que corresponde
    #                a la imagen.
    #           - B: en generar acá iría la matriz que corresponde
    #                a la ventana.
    # Salidas: Una matriz que corresponde a una imágen con el resultado
    #          de la convolución.
    # Obteniendo la cantidad de columnas de una imagen.
    m = len(A)
    # Obteniendo la cantidad de filas de una imagen.
    n = len(A[0])
    # Obteniendo la cantidad de columnas de la ventana.
    p = len(B)
    # Obteniendo la cantidad de filas de la ventana.
    q = len(B[0])
    # Calculando la cantidad de columnas final de la imagen resultante.
    columnas = m + p - 1
    # Calculando la cantidad de filas final de la imagen resultante.
    filas = n + q - 1
    # Generando una matriz de ceros que será donde se guardan los
    # resultados de la cnvolución.
    C = np.zeros((columnas, filas))
    for i in range(0, columnas): # Recorriendo las columnas.
        for j in range(0, filas): # Recorriendo las filas.
            r = max(0, i - p + 1) # Tomando el valor inicial de r.
            val_fin_s_1 = min(i, m) # Tomando el valor final de r.
            while r < val_fin_s_1 + 1: # Iterando r hasta su valor final.
                s = max(0, j - q + 1) # Tomando el valor inicial de s.
                val_fin_s_2 = min(j, n) # Tomando el valor final de s.
                while s < val_fin_s_2 + 1: # Iterando s hasta su valor final.
                    # Verificando que r, s, i-r y j-s estén dentro del rango de
                    # imagen resultante.
                    if 0 <= r < m and 0 <= s < n and 0 <= i - r < p and 0 <= j - s < q:
                        # Realizando la suma correspondiente a la convolución.
                        C[i][j] += A[r][s] * B[i - r][j - s]
                        s += 1
                    else:
                        break
                r += 1
    return C
# Probando la convolución.
A = imageio.imread("boat.jpg")
B = [[1, 2, 1],
     [0, 0, 0],
     [-1, -2, -1]]
C = convolucion_2D(A, B)
C2 = ndimage.convolve(A, B, mode='constant', cval=1.0)
plt.figure()
plt.subplot(121)
plt.title("Convolucion manual")
plt.imshow(C, cmap='gray')
plt.subplot(122)
plt.title("Convolución Python")
plt.imshow(C2, cmap='gray')
plt.show()
