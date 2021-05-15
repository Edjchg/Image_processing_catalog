
import imageio #Cargar imagenes
import matplotlib.pyplot as plt #Graficos
import numpy as np#Libreria matematica

"""
Calculo de la trasformada discreta de fourier usando 
la formula.
"""
def dft_formula(nombre_imagen):
    A = imageio.imread(nombre_imagen)
    m,n=A.shape[0],A.shape[1]
    F=np.zeros((m,n))
    j=np.complex(0,1)
    for u in range(m):
        print(u)
        for v in range(n):
            for x in range(m):
                for y in range(n):
                    F[u,v] += A[x, y]*np.exp((-j*2*np.pi*((u*x)/m+(v*y)/n)))
    return F

"""
Aplicacion de la tranformada discreta de fourier 
en 2 dimenciones usando la funcion de numpy
"""
def dft_2d(nombre_imagen):
    A = imageio.imread(nombre_imagen)
    B = np.fft.fft2(A)
    return B

img = "animal.jpg"

A = imageio.imread(img)
B = dft_2d(img)
print(B[0,1])
C=dft_formula(img)
print(C[0,1])
plt.figure()
#Imagen original
plt.subplot(221),plt.title("Imagen original")
plt.imshow(A, cmap='gray')
#Imagen con fft2
plt.subplot(222),plt.title("Tranformada discreta de fourier numpy")
plt.imshow(np.log(1 + np.abs(B)), cmap='gray')
#Imagen con fft2 con la formula
plt.subplot(223),plt.title("Tranformada discreta de fourier con formula")
plt.imshow(np.log(1 + np.abs(C)), cmap='gray')
#Imagen con fft2 inversa
plt.subplot(224),plt.title("Imagen transformada inversa")
plt.imshow(np.abs(np.fft.ifft2(C)), cmap='gray')
plt.show()

#Imagen con fft2 inversa
plt.subplot(221),plt.title("Imagen transformada inversa")
plt.imshow(np.abs(np.fft.ifft2(np.fft.fftshift(C))), cmap='gray')
plt.show()
