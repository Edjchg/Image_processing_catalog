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

def filt_contr_prom(B, R=1):
# Filtro contra armonico promedio
#   Elimina el ruido aditivo de una imagen en escala de grises
#
# Recibe: 
#   B - una matriz de doubles en escala de gris con ruido
#   R - Una constante entera positiva
# Retorna: una matriz de uint8 en escala de gris sin ruido

    (m, n) = B.shape # se extraen las dimensiones de la imagen
    A_t = np.zeros((m, n))

    # Preparacion de matrices pre-potenciadas para facilitar calculos
    BR1 = np.power(B, R + 1)
    BR = np.power(B, R)

    # Filtrado en esquinas (4)

    # Esquina 1
    # Pixel a modificar: B(0,0)
    # Pixeles: B(0,0), B(0,1), B(1,0), B(1,1)
    # Sumatoria numerador (R+1)
    Wn = BR1[0, 0] + BR1[0, 1] + BR1[1, 0] + BR1[1, 1]
    # Sumatoria denominador (R)
    Wd = BR[0, 0] + BR[0, 1] + BR[1, 0] + BR[1, 1]
    A_t[0, 0] = Wn / Wd

    # Esquina 2
    # Pixel a modificar: B(0,n-1)
    # Pixeles: B(0,n-1), B(0,n-2), B(1,n-1), B(1,n-2)
    # Sumatoria numerador (R+1)
    Wn = BR1[0, n-1] + BR1[0, n-2] + BR1[1, n-1] + BR1[1, n-2]
    # Sumatoria denominador (R)
    Wd = BR[0, n-1] + BR[0, n-2] + BR[1, n-1] + BR[1, n-2]
    A_t[0, n-1] = Wn / Wd

    # Esquina 3
    # Pixel a modificar: B(m-1,0)
    # Pixeles: B(m-1,0), B(m-1,1), B(m-2,0), B(m-2,1)
    # Sumatoria numerador (R+1)
    Wn = BR1[m-1, 0] + BR1[m-1, 1] + BR1[m-2, 0] + BR1[m-2, 1]
    # Sumatoria denominador (R)
    Wd = BR[m-1, 0] + BR[m-1, 1] + BR[m-2, 0] + BR[m-2, 1]
    A_t[m-1, 0] = Wn / Wd

    # Esquina 4
    # Pixel a modificar: B(m-1,n-1)
    # Pixeles: B(m-1,n-1), B(m-1,n-2), B(m-2,n-1), B(m-2,n-2)
    # Sumatoria numerador (R+1)
    Wn = BR1[m-1, n-1] + BR1[m-1, n-2] + BR1[m-2, n-1] + BR1[m-2, n-2]
    # Sumatoria denominador (R)
    Wd = BR[m-1, n-1] + BR[m-1, n-2] + BR[m-2, n-1] + BR[m-2, n-2]
    A_t[m-1, n-1] = Wn / Wd


    # Filtrado en bordes
    # Borde superior
    # Pixel a modificar: B(0,y)
    for y in range(1, n-1):
        # Sumatoria numerador (R+1)
        Wnf1 = BR1[0, y-1] + BR1[0, y] + BR1[0, y+1] # Fila 1
        Wnf2 = BR1[1, y-1] + BR1[1, y] + BR1[1, y+1] # Fila 2
        Wn = Wnf1 + Wnf2
        # Sumatoria denominador (R)
        Wdf1 = BR[0, y-1] + BR[0, y] + BR[0, y+1] # Fila 1
        Wdf2 = BR[1, y-1] + BR[1, y] + BR[1, y+1] # Fila 2
        Wd = Wdf1 + Wdf2
        A_t[0, y] =  Wn / Wd
    # Borde inferior
    # Pixel a modificar: B(m-1,y)
        # Sumatoria numerador (R+1)
        Wnf1 = BR1[m-2, y-1] + BR1[m-2, y] + BR1[m-2, y+1] # Fila 1
        Wnf2 = BR1[m-1, y-1] + BR1[m-1, y] + BR1[m-1, y+1] # Fila 2
        Wn = Wnf1 + Wnf2
        # Sumatoria denominador (R)
        Wdf1 = BR[m-2, y-1] + BR[m-2, y] + BR[m-2, y+1] # Fila 1
        Wdf2 = BR[m-1, y-1] + BR[m-1, y] + BR[m-1, y+1] # Fila 2
        Wd = Wdf1 + Wdf2
        A_t[m-1, y] = Wn / Wd
    # Borde derecho
    # Pixel a modificar: B(x,n-1)
    for x in range(1, m-1):
        # Sumatoria numerador (R+1)
        Wnc1 = BR1[x-1, n-2] + BR1[x, n-2] + BR1[x+1, n-2] # Col 1
        Wnc2 = BR1[x-1, n-1] + BR1[x, n-1] + BR1[x+1, n-1] # Col 2
        Wn = Wnc1 + Wnc2
        # Sumatoria denominador (R)
        Wdc1 = BR[x-1, n-2] + BR[x, n-2] + BR[x+1, n-2] # Col 1
        Wdc2 = BR[x-1, n-1] + BR[x, n-1] + BR[x+1, n-1] # Col 2
        Wd = Wdc1 + Wdc2
        A_t[x, n-1] =  Wn / Wd
    # Borde izquierdo
    # Pixel a modificar: B(x,0)
        # Sumatoria numerador (R+1)
        Wnc1 = BR1[x-1, 0] + BR1[x, 0] + BR1[x+1, 0] # Col 1
        Wnc2 = BR1[x-1, 1] + BR1[x, 1] + BR1[x+1, 1] # Col 2
        Wn = Wnc1 + Wnc2
        # Sumatoria denominador (R)
        Wdc1 = BR[x-1, 0] + BR[x, 0] + BR[x+1, 0] # Col 1
        Wdc2 = BR[x-1, 1] + BR[x, 1] + BR[x+1, 1] # Col 2
        Wd = Wdc1 + Wdc2
        A_t[x, 0] =  Wn / Wd


    # Filtrado en centros
    # Pixel a modificar: B(x,y)
    for x in range(1, m-1):
        for y in  range(1, n-1):
            # Sumatoria numerador (R+1)
            Wnf1 = BR1[x-1, y-1] + BR1[x-1, y] + BR1[x-1, y+1] # Fila 1
            Wnf2 = BR1[x, y-1] + BR1[x, y] + BR1[x, y+1] # Fila 2
            Wnf3 = BR1[x+1, y-1] + BR1[x+1, y] + BR1[x+1, y+1] # Fila 3
            Wn = Wnf1 + Wnf2 + Wnf3
            # Sumatoria denominador (R)
            Wdf1 = BR[x-1, y-1] + BR[x-1, y] + BR[x-1, y+1] # Fila 1
            Wdf2 = BR[x, y-1] + BR[x, y] + BR[x, y+1] # Fila 2
            Wdf3 = BR[x+1, y-1] + BR[x+1, y] + BR[x+1, y+1] # Fila 3
            Wd = Wdf1 + Wdf2 + Wdf3

            A_t[x, y] = Wn / Wd

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

# Filtro Contra Armonico Promedio
B = filt_contr_prom(A, 2)

plt.subplot(122) # posicionamiento de la nueva imagen
plt.title("Imagen Filtrada Contra Armonico Promedio") 
plt.imshow(B, cmap='gray', vmin = 0, vmax = 255, interpolation='none')
# muestra matriz como imagen

plt.show() # despliega la grafica