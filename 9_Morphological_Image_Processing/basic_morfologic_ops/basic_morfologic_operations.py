import matplotlib.pyplot as plt
import imageio
import numpy as np


def binaria(X):
    # Toma una imagen en blanco y negro y retorna una imagen de valores de 0 y 255
    # Entradas: - una imagen en blanco y negro.
    # Salidas: - una imagen binaria con valores de 0 o 255.
    m = len(X)
    n = len(X[0])
    z = np.size(X[0, 0])
    Y = np.zeros([m, n, z])
    Y[X >= 127] = 255
    Y[X < 127] = 0
    return Y[:, :, 0]


def complemento(A):
    # Función que toma una imagen y obtiene el contrario o su complemento.
    # Entradas: - una imagen binaria de valores de 0 y 255.
    # Salidas: - salida con el negativo o complemento de A.
    A = binaria(A)
    A = 255 - A
    return A


def union(A, B):
    # Función que toma dos imagenes del mismo tamaño y obtiene
    # la operación morfologica de unión entre ambas.
    # Entradas: - A: imagen binaria
    #           - B: imagen binaria
    # salidas: - imagen con el resultado de la unión entre A y B.
    A = binaria(A)
    B = binaria(B)
    C = np.logical_or(A, B)
    return C

def interseccion(A, B):
    # Función que toma dos imagenes del mismo tamaño y obtiene
    # la operación morfológica de intersección entre ambas.
    # Entradas: - A: imagen binaria.
    #           - B: imagen binaria.
    # Salidas: - imagen con el resultado de la intersección
    #            entre A y B
    A = binaria(A)
    B = binaria(B)
    C = np.logical_and(A, B)
    return C

def diferencia(A, B):
    # Función que toma dos imagenes del mismo tamaño y obtiene
    # la operación morfológica de diferencia entre ambas.
    # Entradas: - A: imagen binaria.
    #           - B: imagen binaria.
    # Salidas: - imagen con el resultado de la diferencia entre
    #            A y B.
    A = binaria(A)
    B = binaria(B)
    C = A - B
    return binaria(C)

A = plt.imread("imagen2.jpg")
B = plt.imread("imagen3.jpg")

plt.figure()
plt.subplot(241)
plt.title("Imagen original A")
plt.imshow(binaria(A), cmap="gray")

plt.subplot(242)
plt.title("Imagen original B")
plt.imshow(binaria(B), cmap="gray")

C = complemento(A)
plt.subplot(243)
plt.title("Complemento de A")
plt.imshow(C, cmap="gray")

X = complemento(B)
plt.subplot(244)
plt.title("Complemento de B")
plt.imshow(X, cmap="gray")

D = union(A, B)
plt.subplot(245)
plt.title("Union A y B")
plt.imshow(D, cmap="gray")

E = interseccion(A, B)
plt.subplot(246)
plt.title("Intersección A y B")
plt.imshow(E, cmap="gray")

F = diferencia(A, B)
plt.subplot(247)
plt.title("Diferencia A y B")
plt.imshow(F, cmap="gray")
plt.show()
