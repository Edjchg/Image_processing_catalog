import numpy as np
import scipy.ndimage as nd
import matplotlib.pyplot as plt
# Importacion de bibliotecas matematica, manejo imagenes, graficado y 
# operaciones morfologicas

# Creacion de las funciones im2double e im2uint8 por la falta de 
# equivalentes en Python
def im2double(im):
    info = np.iinfo(im.dtype) # Consiguie el tipo de dato de la imagen
    # Divide todos los valores por el maximo
    return im.astype(np.float64) / info.max 

def im2uint8(im):
    info = np.iinfo(np.uint8) # Consiguie el tipo de dato de la imagen
    # Multiplica por el valor maximo
    temp = im*info.max
    temp[temp>info.max] = info.max
    temp[temp<info.min] = info.min
    return temp.astype(np.uint8) 

# Definicion de la funcion binaria en python
def binaria(X):
    # Toma una imagen en blanco y negro y retorna una imagen de valores de 0 y 1
    # Entradas: - una imagen en blanco y negro.
    # Salidas: - una imagen binaria con valores de 0 o 1
    (m, n) = X.shape
    Y = np.zeros((m, n)).astype(np.bool8) # se utiliza el tipo booleano de 8 bits
    Y[X >= 0.5] = 1
    Y[X < 0.5] = 0
    return Y

def b_interno(A, B):
# Extraccion de borde interno de la imagen
#   Realiza la operacion: A - (A erosion B)
#   
# Recibe: 
#   - A: imagen binaria a extraer el borde
#   - B: elemento estructurado en el cual realizar la extraccion
# Retorna: 
#   - D: imagen binaria con borde interno

    # Aplicacion de la erosion binaria
    C = nd.binary_erosion(A, B).astype(A.dtype)
    # Primero se invierte logicamente C y luego se aplica la operacion and logico 
    D = np.logical_and(A, np.invert(C))

    return D

def b_externo(A, B):
# Extraccion de borde externo de la imagen
#   Realiza la operacion: (A dilatacion B) - A
#   
# Recibe: 
#   - A: imagen binaria a extraer el borde
#   - B: elemento estructurado en el cual realizar la extraccion
# Retorna: 
#   - D: imagen binaria con borde externo

    # Aplicacion de la dilatacion binaria
    C = nd.binary_dilation(A, B).astype(A.dtype)
    # Primero se invierte logicamente A y luego se aplica la operacion and logico 
    D = np.logical_and(C, np.invert(A))

    return D

def grad_morf(A, B):
# Extraccion de la gradiente morfologica de la imagen
#   Realiza la operacion: (A dilatacion B) - (A erosion B)
#   
# Recibe: 
#   - A: imagen binaria a extraer el borde
#   - B: elemento estructurado en el cual realizar la extraccion
# Retorna: 
#   - E: imagen binaria con gradiente morfologica

    # Aplicacion de la dilatacion binaria entre A y B
    C = nd.binary_dilation(A, B).astype(A.dtype)
    # Aplicacion de la erosion binaria entre A y B
    D = nd.binary_erosion(A, B).astype(A.dtype)
    # Primero se invierte logicamente D y luego se aplica la operacion and logico 
    E = np.logical_and(C, np.invert(D))

    return E

A = plt.imread("imagen6.jpg") # lectura de imagen en escala a grises

# la imagen no esta en escala de grises pero sus canales son iguales
A = A[:, :, 0] # Se utiliza uno de los canales de colores 
A = im2double(A) # Se normaliza la imagen
A = binaria(A) # elimina valores intermedios

# Creacion del elemento estructurado
B = np.ones((3, 3), A.dtype)

plt.figure(1) # creacion de nueva figura para graficado
plt.subplot(141) # posicionamiento de imagen
plt.title("Imagen Original")
plt.imshow(A, cmap='gray', vmin = 0, vmax = 1, interpolation='none')
# muestra matriz como imagen

# Borde interno
BI = b_interno(A, B)

# Borde externo
BE = b_externo(A, B)

# Gradiente morfologica
GM = grad_morf(A, B)

plt.subplot(142) # posicionamiento de la nueva imagen
plt.title("Imagen Borde Interno") 
plt.imshow(BI, cmap='gray', vmin = 0, vmax = 1, interpolation='none')
# muestra matriz como imagen

plt.subplot(143) # posicionamiento de la nueva imagen
plt.title("Imagen Borde Externo") 
plt.imshow(BE, cmap='gray', vmin = 0, vmax = 1, interpolation='none')
# muestra matriz como imagen

plt.subplot(144) # posicionamiento de la nueva imagen
plt.title("Imagen Gradiente Morfológica") 
plt.imshow(GM, cmap='gray', vmin = 0, vmax = 1, interpolation='none')
# muestra matriz como imagen

plt.show() # despliega la grafica