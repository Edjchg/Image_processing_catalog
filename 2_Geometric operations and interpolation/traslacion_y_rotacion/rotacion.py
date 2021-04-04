
import numpy as np # Operaciones matematicas con matrices.
import matplotlib.pyplot as plt # Graficacion de figuras
from PIL import Image # Carga y creacion de imagenes.


def mediana_kernel3x3(A, x, y):
    #   Funcion auxilar toma un kernel 3x3 alrededor de la posicon
    #   (x,y) para obtener la mediana del arreglo de valores.
    #   Entrada: 
    #           A = matriz de la imagen
    #           x = posicion del pixels en x
    #           y = posicion del pixels en y
    #   Salida:
    #           Valor de la mediana
    kernel_array = np.squeeze(np.asarray(A[x-1:x+2, y-1:y+2]))
    return np.uint8(np.median(kernel_array))

def filtro_mediana(img, s = True, n_salida = "filtro_mediana.jpg"):
    #   Aplica el filtro mediana a una imagen en escala 
    #   de grises y cuando el valor del pixels es absolutamente 
    #   negro.
    #   Entrada:
    #           img = Imagen en escala de grises
    #   Salida:
    #           Imagen filtrada en escala de grises
    m, n = img.size
    A = np.array(img, dtype=np.uint8)
    # Se recorre toda la imagen en busca de 
    # pixeles negros para ser remplazados con
    # el filtrado.
    for x in range(m): 
        for y in range(n):
            if A[x, y] == np.uint8(0):
                A[x,y] = mediana_kernel3x3(A, x, y)
    #imagen de salida
    img_salida = Image.fromarray(A, 'L')
    #Guardado de la imagen
    if s:
        img_salida.save(n_salida)
    return img.convert('L'), img_salida.convert('L')
    
def rotacion(theta = np.pi/4, img = Image.open('barbara.jpg', 'r').convert('L'),
        s= True, n_salida= "rotacion.jpg"):
    #   Funcion rotacion de una imagen en escala de grises,
    #   el proceso consiste en rotar una imagen hacia la derecha
    #   segun el angulo de rotacion theta.
    #   Entrada:
    #           theta = angulo de rotacion en radianes(default = pi/4)
    #           img = imagen a color o escala de grises 
    #           s = guardar resultado(True/False) (defualt = True)
    #           n_salida = nombre imagen de salida con extension(defualt = rotacion.jpg)
    A = np.array(img, dtype= np.uint8) # Conversion de imagen de entreda en matriz
    m, n = img.size
    B = np.zeros((m, n), dtype=np.uint8) #Imagen de salida
    
    #Centro de rotacion, parte entera
    x_c = m//2     
    y_c = n//2 

    for x in range(m-1):
        for y in range(n-1):
            #Calculo de la nueva posicion x del pixels
            a0 = np.cos(theta)
            a1 = np.sin(theta)
            a2 = x_c - a0*x_c - a1*y_c
            x_t = round(a0*x + a1*y + a2)
            #Calculo de la nueva posicion y del pixels
            b0 = -np.sin(theta)
            b1 = np.cos(theta)
            b2 = y_c - b0*y_c - b1*y_c
            y_t = round(b0*x + b1*y + b2)
            #Solo se coloca el pixels si la posicion 
            # no sobrepasa el tamano de la imagen original.
            if x_t>=0 and y_t>=0 and x_t<m and y_t<n:
                B[x_t, y_t] = np.uint8(A[x, y])
    
    #Imagen de salida a escala de grises
    img_salida = Image.fromarray(B, 'L')
    #Guardado de la imagen
    if s:
        img_salida.save(n_salida)
    return img.convert('L'), img_salida.convert('L')
      


print("Rotacion de una imagen \n")
gf = plt.figure()
img_e, img_s = rotacion()  
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