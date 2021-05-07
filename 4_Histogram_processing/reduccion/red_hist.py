import numpy as np
import matplotlib.image as im
import matplotlib.pyplot as plt
# Importacion de bibliotecas matematica, manejo imagenes y graficado

def red_hist(A):
# Reduccion del histograma
#  Esta técnica modifica el histograma original de tal manera que comprime 
#  la dinámica de escala de grises [r_min, r_max] a otra escala.
#
# Recibe: una matriz de imagen en escala de gris con valores de 8 bits
# Retorna:
# - B: una matriz resultante de imagen de valores de 8bits

    # Obtencion de las dimensiones de la imagen de entrada
    m = len(A)
    n = len(A[0])

    B = np.zeros((m,n)) # matriz de ceros con tamano de A
    A = A.astype(np.double) # conversion de tipos de int a double

    # Definicion de constantes para la reduccion
    alpha = 50 
    beta = 50

    rmax = np.max(A) # se extrae el valor maximo
    rmin = np.min(A) # se extrae el valor minimo

    smax = rmax - alpha # se obtiene smax para reducir
    smin = rmin + beta # se obitene smin para reducir

    # Metodo de reduccion del histograma
    temp = (smax - smin) / (rmax - rmin) # se calcula un temporal
    # Se utilizan los metodos de numpy para las operaciones en matrices
    # Equivale a:
    #   (A.-rmin).*temp.-smin
    B = np.add(np.dot(np.subtract(A, rmin), temp), smin)

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


A = im.imread("boat.jpg") # lectura de imagen en escala a grises
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

B = red_hist(A) # reduccion del histograma aplicado a la imagen

plt.subplot(223) # posicionamiento de imagen
plt.title("Imagen con Histograma Reducido") # titulo de la imagen
plt.imshow(B, cmap='gray', vmin = 0, vmax = 255, interpolation='none') 
# muestra matriz como imagen

plt.subplot(224) # posicionamiento del histograma
plt.title("Histograma de la Imagen con Histograma Reducido") 
H2 = imhist_py(B) # calculo del histograma por metodo implementado
plt.bar(range(256), H2) # graficacion del histograma
plt.xlim([0, 255]) # limite de la graficacion en el eje x

plt.show() # despliega la grafica