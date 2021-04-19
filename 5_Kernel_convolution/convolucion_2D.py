import numpy as np
import matplotlib.pyplot as plt
import imageio
from scipy import ndimage


def convolucion_2D(A, B):
    m = len(A)
    print(m)
    n = len(A[0])
    print(n)
    p = len(B)
    print(p)
    q = len(B[0])
    print(q)
    columnas = m + p - 1
    filas = n + q - 1

    C = np.zeros((columnas, filas))

    for i in range(0, columnas):
        for j in range(0, filas):
            r = max(0, i - p + 1)
            val_fin_s_1 = min(i, m)
            # for r in range(val_ini_s_1, val_fin_s_1):
            while r < val_fin_s_1 + 1:
                s = max(0, j - q + 1)
                val_fin_s_2 = min(j, n)
                # for s in range(val_ini_s_2, val_fin_s_2):
                while s < val_fin_s_2 + 1:
                    if 0 <= r < m and 0 <= s < n and 0 <= i - r < p and 0 <= j - s < q:
                        C[i][j] += A[r][s] * B[i - r][j - s]
                        s += 1
                    else:
                        break

                r += 1

    return C


# A = [[1, 0, 1], [4, 3, 1], [-1, 0, 2], [3, 0, -1]]
# B = [[1, -1, 2, 3], [-4, 0, 1, 5], [3, 2, -1, 0]]
# A = [[1, 2, 3, 9], [4, 5, 6, 10], [7, 8, 9, 11]]
# B = [
#      [2, 4],
#      [3, 2]
#     ]

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
