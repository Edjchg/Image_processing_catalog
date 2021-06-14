import matplotlib.pyplot as plt
import imageio
import numpy as np


def binaria(X):
    m = len(X)
    n = len(X[0])
    z = np.size(X[0, 0])
    Y = np.zeros([m, n, z])
    Y[X >= 127] = 255
    Y[X < 127] = 0
    return Y[:, :, 0]


def complemento(A):
    A = binaria(A)
    A = 255 - A
    return A


def union(A, B):
    A = binaria(A)
    B = binaria(B)
    C = np.logical_or(A, B)
    return C

def interseccion(A, B):
    A = binaria(A)
    B = binaria(B)
    C = np.logical_and(A, B)
    return C

def diferencia(A, B):
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
