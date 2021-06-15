import matplotlib.pyplot as plt
import imageio
# from scipy import signal
import numpy as np


def otsu_umbrales(A):
    # Función que toma una imagen y calcula dos valores de corte para
    # segmentar la imagen en 3 tonos de gris.
    # Entradas: - A: imagen en blanco y negro.
    # Salidas: - imagen segmentada con tres tonos de gris.
    m = len(A)
    n = len(A[0])
    # Paso 0:
    q, _ = np.histogram(A, bins=255, range=(0, 255))
    # Paso 1:
    h = q / (m * n)
    k = len(h)
    p_vector = np.zeros(k)
    p = 0
    # Paso 2:
    for i in range(0, k):
        p_vector[i] = np.sum(h[0:i])
    # Paso 3
    m_c = np.zeros(k)
    for i in range(0, k):
        sum_result = 0
        for j in range(0, i):
            sum_result += (j) * h[j]
        m_c[i] = sum_result
    # Paso 4
    m_g = m_c[-1]
    # Paso 5
    var_sigma = np.zeros((k, k))
    for k1 in range(0, k):
        for k2 in range(0, k):
            if k1 < k2:
                P1 = np.sum(h[0:k1])
                P2 = np.sum(h[k1+1:k2])
                P3 = np.sum(h[k2+1:k])
                sum_m1 = 0
                sum_m2 = 0
                sum_m3 = 0
                for i in range(0, k1):
                    sum_m1 += (i - 1) * h[i]

                for i in range(k1, k2):
                    sum_m2 += (i - 1) * h[i]

                for i in range(k2, k):
                    sum_m3 += (i - 1) * h[i]
                m1 = 0
                m2 = 0
                m3 = 0
                if P1 != 0:
                    m1 = sum_m1 / P1
                if P2 != 0:
                    m2 = sum_m2 / P2
                if P3 != 0:
                    m3 = sum_m3 / P3
                var_sigma[k1, k2] = (P1 * (m1 - m_g) ** 2) + (P2 * (m2 - m_g) ** 2) + (P3 * (m3 - m_g) ** 2)
    # Paso 6
    T1, T2 = np.where(var_sigma == np.max(var_sigma))
    T1 = T1[0]
    T2 = T2[0]
    B = np.zeros((m, n, 3))
    print(A[T1,T2])
    B[A > T2] = 255
    B[np.logical_and(T1 < A, A <= T2)] = 255//2
    B[A < T1] = 0
    return B.astype(np.uint8)

A = plt.imread("imagen6.jpg")
B = otsu_umbrales(A)
plt.figure()
plt.subplot(121)
plt.title("Imagen original")
plt.imshow(A)
plt.subplot(122)
plt.title("Imagen segmentada")
plt.imshow(B, cmap="gray")
plt.show()
