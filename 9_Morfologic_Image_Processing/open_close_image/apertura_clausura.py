from scipy import ndimage
import matplotlib.pyplot as plt
import numpy as np

from skimage.morphology import (erosion, dilation, opening, closing,  # noqa
                                white_tophat)


def binaria(X):
    m = len(X)
    n = len(X[0])
    z = np.size(X[0, 0])
    Y = np.zeros([m, n, z])
    Y[X >= 127] = 255
    Y[X < 127] = 0
    return Y[:, :, 0]


def apertura(A, B):
    A = binaria(A)
    B = binaria(B)
    C = ndimage.binary_opening(A, B)
    return C

def clausura(A, B):
    A = binaria(A)
    B = binaria(B)
    C = ndimage.binary_closing(A, B)
    return C


A = plt.imread("imagen5.jpg")
B = np.ones([3, 3])*255

plt.figure()
plt.subplot(131)
plt.title("Imagen original")
plt.imshow(binaria(A), cmap="gray")

C = apertura(A, B)
plt.subplot(132)
plt.title("Imagen con apertura")
plt.imshow(C, cmap="gray")

D = clausura(A, B)
plt.subplot(133)
plt.title("Imagen con clausura")
plt.imshow(D, cmap="gray")

plt.show()
