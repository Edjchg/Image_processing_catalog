import imageio
import numpy as np
import matplotlib.pyplot as plt



def rango_reducido_bilateral(A, r, p):

    n = len(A[1])
    Y_2 = np.random.normal(-1, 1, size=(n, r))
    print("shape " + str(len(Y_2)) + "," + str(len(Y_2[0])))
    for k in range(0, p):
        Y_1 = np.dot(A, Y_2)
        Y_2 = np.dot(A.T, Y_1)

    (Q, R) = np.linalg.qr(Y_2)
    QR = Q[:, 1:r]
    B = np.dot(A, QR)
    C = QR.T

    return B, C


I_color = imageio.imread("img1.jpg")
A = I_color[:, :, 0]
print(len(A), len(A[0]))
r = 200

B2, C2 = rango_reducido_bilateral(A, r, 3)
Ar2 = np.dot(B2, C2)

plt.figure(1)
plt.subplot(121)
plt.title("Original")
plt.imshow(A, cmap=plt.get_cmap('gray'))

plt.subplot(122)
plt.title("Rango reducido")
plt.imshow(Ar2, cmap=plt.get_cmap('gray'))
plt.show()
