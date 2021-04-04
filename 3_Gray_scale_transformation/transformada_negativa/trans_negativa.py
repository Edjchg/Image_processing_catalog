import numpy as np
import imageio as im
import matplotlib.pyplot as plt
# Importacion de bibliotecas matematica, manejo imagenes y graficado

def trans_negativa(A):
# Transformada negativa
#   realiza una inversion en los valores de la imagen en la escala de grises
#   (0, ..., 255)
# Realiza la siguiente operacion:
#   B = c*A + b
#   donde c = -1 ; b = 255
# Recibe: una matriz de imagen en valores de 8 bits
# Retorna: una matriz resultante de imagen de valores de 8 bits

    A = A.astype(np.double) # conversion de tipos de int a double

    B = np.zeros((len(A),len(A[0]))) 
        # crea una matriz de ceros con tamano de A

    # se definen los valores de c y b para la conversion lineal negativa
    c = -1 
    b = 255

    B_dot = np.dot(c,A) # producto punto entre matrices 
    B = np.add(B_dot, b) # suma vectorial entre matrices
    B = B.astype(np.uint8) # conversion de tipos de double a uint8

    return B

A = im.imread("boat.jpg") # lectura de imagen original escala a grises 512*512
    # Nota: image.io utiliza arrays de numpy por lo que sus tipos son 
    #   compatibles

plt.figure(1) # creacion de nueva figura para graficado
plt.subplot(121) # posicionamiento de imagen original
plt.title("Imagen Original") # titulo de la imagen original
plt.imshow(A, cmap=plt.get_cmap('gray')) # muestra matriz original como imagen

B = trans_negativa(A) # aplicacion de la transformada negativa

plt.subplot(122) # posicionamiento de imagen transformada
plt.title("Imagen Modificada Transformada Negativa") 
    # titulo de la imagen transformada
plt.imshow(B, cmap=plt.get_cmap('gray'))
    # muestra matriz transformada como imagen en escala de grises

plt.show() # despliega la grafica