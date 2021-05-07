import numpy as np
import matplotlib.image as im
import matplotlib.pyplot as plt
# Importacion de bibliotecas matematica, manejo imagenes y graficado

def estir_hist(A):
# Estiramiento del histograma
#  Esta técnica consiste en una transformación lineal que expande parte del 
#  histrograma original, tal que la intensidad original que está en un rango 
#  en [r_max, r_min], ocupa toda la escala [0, 255]
#
# Recibe: una matriz de imagen en escala de gris con valores de 8 bits
# Retorna:
# - B: una matriz resultante de imagen de valores de 8bits

    # Obtencion de las dimensiones de la imagen de entrada
    m = len(A)
    n = len(A[0])

    B = np.zeros((m,n)) # matriz de ceros con tamano de A
    A1 = A.astype(np.double) # conversion de tipos de int a double

    rmax = np.max(A) # se extrae el valor maximo
    rmin = np.min(A) # se extrae el valor minimo

    # Metodo de estiramiento del histograma
    for i in range(m):
        for j in range(n):
            B[i, j] = (255 / (rmax - rmin)) * (A1[i, j] - rmin)

    B = np.ceil(B).astype(np.uint8) # conversion de tipos de double a uint8
    # Requiere de un redondeo

    return B


def imhist_py(input):
# Calculo de histograma
#   realiza el calculo de histograma para una imagen en escala de grises
#
# Basado en la segunda forma de calcular el histograma
#
# Recibe: una matriz de imagen en escala de gris con valores de 8 bits
# Retorna: un vector que representa el histograma de valores

    H = np.zeros(256); # crea un vector del tamano de rango de la escala de grises

    # Itera sobre cada nivel de gris para saber su frecuencia
    for i in range(256):
        H[i] = sum(sum(input==i)) # suma de valores iguales encontrados

    return H


A = im.imread("sydney.jpg") # lectura de imagen en escala a grises
    # Nota: image.io utiliza arrays de numpy por lo que sus tipos son 
    #   compatibles

plt.figure(1) # creacion de nueva figura para graficado
plt.subplot(221) # posicionamiento de imagen
plt.title("Imagen Original") # titulo de la imagen
plt.imshow(A, cmap='gray', vmin = 0, vmax = 255, interpolation='none') 
# muestra matriz como imagen

plt.subplot(222) # posicionamiento de imagen
plt.title("Histograma de la Imagen Original") 
H1 = imhist_py(A) # calculo del histograma por metodo implementado
plt.bar(range(256), H1) # graficacion del histograma
plt.xlim([0, 255]) # limite de la graficacion en el eje x

B = estir_hist(A) # estiramiento del histograma aplicado a la imagen

plt.subplot(223) # posicionamiento de imagen
plt.title("Imagen con Histograma Estirado") # titulo de la imagen
plt.imshow(B, cmap='gray', vmin = 0, vmax = 255, interpolation='none') 
# muestra matriz como imagen

plt.subplot(224) # posicionamiento del histograma
plt.title("Histograma de la Imagen con Histograma Estirado") 
H2 = imhist_py(B) # calculo del histograma por metodo implementado
plt.bar(range(256), H2) # graficacion del histograma
plt.xlim([0, 255]) # limite de la graficacion en el eje x

plt.show() # despliega la grafica
