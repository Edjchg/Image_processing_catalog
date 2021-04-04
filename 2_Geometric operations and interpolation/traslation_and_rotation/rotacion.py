
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image


def mediana_kernel3x3(A, x, y):
    kernel_array = np.squeeze(np.asarray(A[x-1:x+2, y-1:y+2]))
    print(kernel_array)
    return np.uint8(np.median(kernel_array))

def filtro_mediana(img):
    m, n = img.size
    A = np.array(img, dtype=np.uint8)
    for x in range(m):
        for y in range(n):
            if A[x, y] == np.uint8(0):
                A[x,y] = mediana_kernel3x3(A, x, y)
    img_salida = Image.fromarray(A, 'L')
    img_salida.save('img_salida_ro_filtrada.jpg')
    return img.convert('L'), img_salida.convert('L')
    
              


def traslacion(theta = np.pi/4, img = Image.open('barbara.jpg', 'r').convert('L')):
    A = np.array(img, dtype= np.uint8)
    m, n = img.size
    B = np.zeros((m, n), dtype=np.uint8)
    
    x_c = m//2
    y_c = n//2

    for x in range(m-1):
        for y in range(n-1):
            a0 = np.cos(theta)
            a1 = np.sin(theta)
            a2 = x_c - a0*x_c - a1*y_c
            x_t = round(a0*x + a1*y + a2)

            b0 = -np.sin(theta)
            b1 = np.cos(theta)
            b2 = y_c - b0*y_c - b1*y_c
            y_t = round(b0*x + b1*y + b2)

            if x_t>=0 and y_t>=0 and x_t<m and y_t<n:
                B[x_t, y_t] = np.uint8(A[x, y])
    
    img_salida = Image.fromarray(B, 'L')
    img_salida.save('img_salida_ro.jpg')
    return img.convert('L'), img_salida.convert('L')
      


print("Rotacion de una imagen \n")

gf = plt.figure()

img_e, img_s = traslacion()  

_ ,img_s_f = filtro_mediana(img_s)

gf.add_subplot(1, 3, 1)
plt.imshow(img_e, cmap='gray')
plt.title("Imagen original")
gf.add_subplot(1, 3, 2)
plt.imshow(img_s, cmap='gray')
plt.title("Imagen con rotacion")
gf.add_subplot(1, 3, 3)
plt.imshow(img_s_f, cmap='gray')
plt.title("Imagen con rotacion con filtro mediana")
plt.show()