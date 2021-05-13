import numpy as np
import imageio as im
import matplotlib.pyplot as plt
# Importacion de bibliotecas matematica, manejo imagenes y graficado

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

def filt_prom_geom(B):
# Filtro promedio geometrico
#   Elimina el ruido aditivo de una imagen en escala de grises
#
# Recibe: una matriz de doubles en escala de gris con ruido
# Retorna: una matriz de uint8 en escala de gris sin ruido

    (m, n) = B.shape # se extraen las dimensiones de la imagen
    A_t = np.zeros((m, n))

    # Filtrado en esquinas (4)
    # Esquina 1
    # Pixel a modificar: B(0,0)
    # Pixeles: B(0,0), B(0,1), B(1,0), B(1,1)
    W = B[0, 0] * B[0, 1] * B[1, 0] * B[1, 1]
    A_t[0, 0] = W ** (1/4)
    # Esquina 2
    # Pixel a modificar: B(0,n-1)
    # Pixeles: B(0,n-1), B(0,n-2), B(1,n-1), B(1,n-2)
    W = B[0, n-1] * B[0, n-2] * B[1, n-1] * B[1, n-2]
    A_t[0, n-1] = W ** (1/4)
    # Esquina 3
    # Pixel a modificar: B(m-1,0)
    # Pixeles: B(m-1,0), B(m-1,1), B(m-2,0), B(m-2,1)
    W = B[m-1, 0] * B[m-1, 1] * B[m-2, 0] * B[m-2, 1]
    A_t[m-1, 0] = W ** (1/4)
    # Esquina 4
    # Pixel a modificar: B(m-1,n-1)
    # Pixeles: B(m-1,n-1), B(m-1,n-2), B(m-2,n-1), B(m-2,n-2)
    W = B[m-1, n-1] * B[m-1, n-2] * B[m-2, n-1] * B[m-2, n-2]
    A_t[m-1, n-1] = W ** (1/4)


    # Filtrado en bordes
    # Borde superior
    # Pixel a modificar: B(0,y)
    for y in range(1, n-1):
        Wf1 = B[0, y-1] * B[0, y] * B[0, y+1]
        Wf2 = B[1, y-1] * B[1, y] * B[1, y+1]
        A_t[0, y] =  (Wf1 * Wf2) ** (1/6)
    # Borde inferior
    # Pixel a modificar: B(m-1,y)
        Wf1 = B[m-2, y-1] * B[m-2, y] * B[m-2, y+1]
        Wf2 = B[m-1, y-1] * B[m-1, y] * B[m-1, y+1]
        A_t[m-1, y] = (Wf1 * Wf2) ** (1/6)
    # Borde derecho
    # Pixel a modificar: B(x,n-1)
    for x in range(1, m-1):
        Wc1 = B[x-1, n-2] * B[x, n-2] * B[x+1, n-2]
        Wc2 = B[x-1, n-1] * B[x, n-1] * B[x+1, n-1]
        A_t[x, n-1] =  (Wc1 * Wc2) ** (1/6)
    # Borde izquierdo
    # Pixel a modificar: B(x,0)
        Wc1 = B[x-1, 0] * B[x, 0] * B[x+1, 0]
        Wc2 = B[x-1, 1] * B[x, 1] * B[x+1, 1]
        A_t[x, 0] =  (Wc1 * Wc2) ** (1/6)


    # Filtrado en centros
    # Pixel a modificar: B(x,y)
    for x in range(1, m-1):
        for y in  range(1, n-1):
            Wf1 = B[x-1, y-1] * B[x-1, y] * B[x-1, y+1] # Fila 1
            Wf2 = B[x, y-1] * B[x, y] * B[x, y+1] # Fila 2
            Wf3 = B[x+1, y-1] * B[x+1, y] * B[x+1, y+1] # Fila 3
            A_t[x, y] = (Wf1 * Wf2 * Wf3) ** (1/9)

    return im2uint8(A_t)

A = im.imread("edificio_china.jpg") # lectura de imagen en escala a grises

# Crear un ruido aditivo
A = im2double(A) # Se normaliza la imagen
A = A[:, :, 0] # Se utiliza uno de los canales de colores 
# la imagen no esta en escala de grises pero sus canales son iguales
(m, n) = A.shape # se extraen las dimensiones de la imagen
N = 0.05 * np.random.randn(m, n) # Se consigue una matrix aleatoria de floats
B = A + N # La imagen con ruido, con valores double normalizados

B1 = im2uint8(B)

plt.figure(1) # creacion de nueva figura para graficado
plt.subplot(121) # posicionamiento de imagen
plt.title("Imagen con ruido")
plt.imshow(B1, cmap='gray', vmin = 0, vmax = 255, interpolation='none')
# muestra matriz como imagen

# Filtro Promedio Geometrico
B = filt_prom_geom(A)

plt.subplot(122) # posicionamiento de la nueva imagen
plt.title("Imagen Filtrada Geometrico") 
plt.imshow(B, cmap='gray', vmin = 0, vmax = 255, interpolation='none')
# muestra matriz como imagen

plt.show() # despliega la grafica