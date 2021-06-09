import matplotlib.pyplot as plt
import imageio
# from scipy import signal
import numpy as np


def otsu_umbral(A):
    m = len(A)
    n = len(A[0])
    # Paso 0:
    # _, q = np.histogram(A, bins=256, range=(0, 256))
    q, _ = np.histogram(A, bins=255, range=(0, 255))
    # Paso 1:
    h = q / (m * n)
    k = len(h)
    p_vector = np.zeros(k)
    p = 0
    # Paso 2
    for i in range(0, k):
        p += h[i]
        p_vector[i] = p

    # Paso 3
    m_c = np.zeros(k)
    m_ = 0
    for i in range(0, k):
        m_ += i * h[i]
        m_c[i] = m_
    # Paso 4
    mg = m_c[-1]
    print(mg)
    # Paso 5
    vector_sigma = np.zeros(k)
    for i in range(0, k):
        denominador = p_vector[i] * (1 - p_vector[i])
        if denominador == 0:
            vector_sigma[i] = 0
        else:
            vector_sigma[i] = ((mg * p_vector[i] - m_c[i]) ** 2) / (p_vector[i] * (1 - p_vector[i]))

    # Paso 6
    T = np.where(vector_sigma == np.max(vector_sigma))
    T = T[0][0]
    print(np.max(vector_sigma))

    B = np.zeros((m, n, 3))
    B[np.where(A > T)] = 255
    B[np.where(A <= T)] = 0
    return B.astype(np.uint8)


A = imageio.imread("imagen4.jpg")
B = otsu_umbral(A)

plt.figure()
plt.subplot(121)
plt.title("Imagen original")
plt.imshow(A)
plt.subplot(122)
plt.title("Imagen segmentada")
plt.imshow(B, cmap="gray")
plt.show()
