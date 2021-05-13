import numpy as np
import imageio as im
import matplotlib.pyplot as plt
# Importacion de bibliotecas matematica, manejo imagenes y graficado

def trans_gamma(A):
# Transformada gamma (potencia)
#   realiza un cambio en el "brillo" de la imagen dependiendo del valor de
#   gamma
#   gamma > 1 : se aclara ; 0 < gamma < 1 : se oscurece
# Realiza la siguiente operacion:
#   B = c*A^gamma
#   donde c = 1 ; gamma
# Recibe: una matriz de imagen en valores de 8 bits
# Retorna: una matriz resultante de imagen de valores de 8 bits

    A = A.astype(np.double) # conversion de tipos de int a double

    B = np.zeros((len(A),len(A[0]))) 
        # crea una matriz de ceros con tamano de A

    # se definen los valores de c y b para la conversion lineal negativa
    c = 1 
    gamma = 1.5

    B_dot = np.dot(c,A) # producto punto entre matrices 
    B = np.float_power(B_dot, gamma) # suma vectorial entre matrices

    # La siguiente parte se realiza por problemas en la conversion de valores
    #   de double a uint8 mayores a 255
    # Si no se realiza, existe una distorsion en la imagen
    x = 0 # inicia contador de filas
    for line in B:
        y = 0 # inicia contador de columnas
        for pixel in line:
            if pixel > 255:
                B[x][y] = 255 # si el pixel es mayor que 255, se limita a 255
            y+=1 
        x+=1

    B = B.astype(np.uint8) # conversion de tipos de double a uint8

    return B

A = im.imread("boat.jpg") # lectura de imagen original escala a grises 512*512
    # Nota: image.io utiliza arrays de numpy por lo que sus tipos son 
    #   compatibles

print(A.shape)

plt.figure(1) # creacion de nueva figura para graficado
plt.subplot(121) # posicionamiento de imagen original
plt.title("Imagen Original") # titulo de la imagen original
plt.imshow(A, cmap=plt.get_cmap('gray')) # muestra matriz original como imagen

B = trans_gamma(A) # aplicacion de la transformada gamma

plt.subplot(122) # posicionamiento de imagen transformada
plt.title("Imagen Modificada Transformada Negativa") 
    # titulo de la imagen transformada
plt.imshow(B, cmap=plt.get_cmap('gray'))
    # muestra matriz transformada como imagen en escala de grises

plt.show() # despliega la grafica