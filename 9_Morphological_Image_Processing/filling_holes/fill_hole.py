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

def rellenar(A, B, iterMax = 100, gui=0):
# Rellenar huecos de una imagen
#   
# Recibe: 
#   - A: imagen binaria que tiene una parte hueca/vacia adentro
#   - B: elemento estructurado
#   - iterMax: numero de iteraciones maximas para el rellenado
#   - gui: opcion para realizar el graficado interactivo
# Retorna: 
#   - X: imagen binaria con el relleno

    # Valor inicial X0=Imagen con un pixel blanco en la parte a rellenar
    (m, n) = A.shape
    X = np.zeros((m, n))
    cx = np.floor((m + 1) / 2).astype('int')
    cy = np.floor((n + 1) / 2).astype('int')
    X[cx, cy] = 1
    
    # Aplicacion del rellenado iterativamente en un bucle
    for k in range(iterMax):
        # Aplicacion de la dilatacion binaria
        C = nd.binary_dilation(X, B).astype(A.dtype)
        # Primero se invierte logicamente A y luego se aplica la operacion and logico 
        X = np.logical_and(C, np.invert(A))

        # Si se desea, el graficado interactivo
        if gui:
            plt.subplot(122) # posicionamiento de la nueva imagen
            plt.title("Iteracion: " + str(k)) 
            plt.imshow(X, cmap='gray', vmin = 0, vmax = 1, interpolation='none')
            # muestra matriz como imagen
            plt.pause(0.1) # pausa de la ventana en 0.1s

    return X

A = plt.imread("imagen7.jpg") # lectura de imagen en escala a grises

# la imagen no esta en escala de grises pero sus canales son iguales
A = A[:, :, 0] # Se utiliza uno de los canales de colores 
A = im2double(A) # Se normaliza la imagen
A = binaria(A) # elimina valores intermedios

# Creacion del elemento estructurado
B = np.ones((4, 4), A.dtype)

plt.figure(1) # creacion de nueva figura para graficado
plt.subplot(121) # posicionamiento de imagen
plt.title("Imagen Original")
plt.imshow(A, cmap='gray', vmin = 0, vmax = 1, interpolation='none')
# muestra matriz como imagen

plt.ion() # activa la interactividad de la ventana

# Iteracion para rellenar el hueco de la imagen
X = rellenar(A, B, 100, 1)

plt.ioff() # desactiva la interactividad

plt.subplot(122) # posicionamiento de la nueva imagen
plt.title("Iteracion: 100 [Finalizado]") 
plt.imshow(X, cmap='gray', vmin = 0, vmax = 1, interpolation='none')

plt.show() # despliega y bloque la ventana