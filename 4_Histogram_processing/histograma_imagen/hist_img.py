import numpy as np
import matplotlib.image as im
import matplotlib.pyplot as plt
# Importacion de bibliotecas matematica, manejo imagenes y graficado

def imhist_py(A):
# Calculo de histograma
#   realiza el calculo de histograma para una imagen en escala de grises
#
# Basado en la segunda forma de calcular el histograma
#
# Recibe: una matriz de imagen en escala de gris con valores de 8 bits
# Retorna: un vector que representa el histograma de valores

    B = np.zeros(256); # crea un vector del tamano de rango de la escala de grises

    # Itera sobre cada nivel de gris para saber su frecuencia
    for i in range(256):
        B[i] = sum(sum(A==i)) # suma de valores iguales encontrados

    return B

A = im.imread("peppers.jpg") # lectura de imagen en escala a grises 512*512
    # Nota: image.io utiliza arrays de numpy por lo que sus tipos son 
    #   compatibles

plt.figure(1) # creacion de nueva figura para graficado
plt.subplot(121) # posicionamiento de imagen
plt.title("Imagen") # titulo de la imagen
plt.imshow(A, cmap='gray', vmin = 0, vmax = 255, interpolation='none')
# muestra matriz como imagen

B1 = imhist_py(A) # obtencion del histograma

plt.subplot(122) # posicionamiento del histograma
plt.title("Histograma de la imagen") 
plt.bar(range(256), B1) # graficacion del histograma
plt.xlim((0, 255)) # limite de la graficacion en el eje x

plt.show() # despliega la grafica