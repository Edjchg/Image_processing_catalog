import numpy as np
import scipy.ndimage as nd
import matplotlib.pyplot as plt
# Importacion de bibliotecas matematica, manejo imagenes, graficado y 
# operaciones morfologicas


def dilate_gray(A, B):
# Calcular Dilatacion: A + B
# Realiza la operación morfológica de dilatación en imágenes de 
# escala de grises.
#   
# Recibe: 
#   - A: imagen en escala de grises
#   - B: elemento estructurado o mascara 
# Retorna: 
#   - C: imagen en escala de grises dilatada

    (m, n) = A.shape # dimensiones de la imagen
    (j, k) = B.shape # dimensiones de la mascara

    B_Xr = j//2 # alcance de la mascara B en el eje X
    B_Yr = k//2 # alcance de la mascara B en el eje Y

    # Matriz de salida en zeros con el tipo uint8
    C = np.zeros((m,n), dtype=np.uint8)
    
    # Esquinas (4)
    # Esquina 1
    Aux = A[0 : B_Xr+1, 0 : B_Yr+1]
    C[0, 0] = np.max(Aux)
    # Esquina 2
    Aux = A[0 : B_Xr+1, (n-1) - B_Yr : n]
    C[0, n-1] = np.max(Aux)
    # Esquina 3
    Aux = A[(m-1) - B_Xr : m, 0 : B_Yr+1]
    C[m-1, 0] = np.max(Aux)
    # Esquina 4
    Aux = A[(m-1) - B_Xr : m, (n-1) - B_Yr : n]
    C[m-1, n-1] = np.max(Aux)

    # Bordes
    for y in range(B_Yr, n - B_Yr):
    # Borde superior
        Aux = A[0 : B_Xr+1, y - B_Yr : y + B_Yr+1]
        C[0, y] = np.max(Aux)
    # Borde inferior
        Aux = A[(m-1) - B_Xr : m, y - B_Yr : y + B_Yr+1]
        C[m-1, y] = np.max(Aux)
    for x in range(1, m-1):
    # Borde derecho
        Aux = A[x - B_Xr : x + B_Xr+1, (n-1) - B_Yr : n]
        C[x, n-1] = np.max(Aux)
    # Borde izquierdo
        Aux = A[x - B_Xr : x + B_Xr+1, 0 : B_Yr+1]
        C[x, 0] = np.max(Aux)

    # Pixeles de centro
    for x in range(B_Xr, m - B_Xr):
        for y in range(B_Yr, n - B_Yr):
            Aux = A[x - B_Xr : x + B_Xr+1, y - B_Yr : y + B_Yr+1]
            C[x, y] = np.max(Aux)

    return C


def erode_gray(A, B):
# Calcular Erosion: A -o- B
# Realiza la operación morfológica de erosion en imagenes de 
# escala de grises.
#   
# Recibe: 
#   - A: imagen en escala de grises
#   - B: elemento estructurado o mascara 
# Retorna: 
#   - C: imagen en escala de grises erosionada

    (m, n) = A.shape # dimensiones de la imagen
    (j, k) = B.shape # dimensiones de la mascara

    B_Xr = j//2 # alcance de la mascara B en el eje X
    B_Yr = k//2 # alcance de la mascara B en el eje Y

    # Matriz de salida en zeros con el tipo uint8
    C = np.zeros((m,n), dtype=np.uint8)
    
    # Esquinas (4)
    # Esquina 1
    Aux = A[0 : B_Xr+1, 0 : B_Yr+1]
    C[0, 0] = np.min(Aux)
    # Esquina 2
    Aux = A[0 : B_Xr+1, (n-1) - B_Yr : n]
    C[0, n-1] = np.min(Aux)
    # Esquina 3
    Aux = A[(m-1) - B_Xr : m, 0 : B_Yr+1]
    C[m-1, 0] = np.min(Aux)
    # Esquina 4
    Aux = A[(m-1) - B_Xr : m, (n-1) - B_Yr : n]
    C[m-1, n-1] = np.min(Aux)

    # Bordes
    for y in range(B_Yr, n - B_Yr):
    # Borde superior
        Aux = A[0 : B_Xr+1, y - B_Yr : y + B_Yr+1]
        C[0, y] = np.min(Aux)
    # Borde inferior
        Aux = A[(m-1) - B_Xr : m, y - B_Yr : y + B_Yr+1]
        C[m-1, y] = np.min(Aux)
    for x in range(1, m-1):
    # Borde derecho
        Aux = A[x - B_Xr : x + B_Xr+1, (n-1) - B_Yr : n]
        C[x, n-1] = np.min(Aux)
    # Borde izquierdo
        Aux = A[x - B_Xr : x + B_Xr+1, 0 : B_Yr+1]
        C[x, 0] = np.min(Aux)

    # Pixeles de centro
    for x in range(B_Xr,m-B_Xr):
        for y in range(B_Yr,n-B_Yr):
            Aux = A[x - B_Xr : x + B_Xr + 1, y - B_Yr : y + B_Yr + 1]
            C[x, y] = np.min(Aux)

    return C


A = plt.imread("imagen11.jpg") # lectura de imagen en escala a grises

# Creacion del elemento estructurado
B = np.zeros((3, 3), A.dtype)

plt.figure(1) # creacion de nueva figura para graficado
plt.subplot(131) # posicionamiento de imagen
plt.title("Imagen Original")
plt.imshow(A, cmap='gray', vmin = 0, vmax = 255, interpolation='none')
# muestra matriz como imagen

# Calculo de la apertura de una imagen en escala de grises
# Paso 1: Erosion
EA = erode_gray(A, B) # aplicacion de la erosion
# Paso 2: Dilatacion
DA = dilate_gray(EA, B) # aplicacion de la diltacion
# Paso 3: Aplicar la transformada de Top-Hat
AP = A - DA

# Calculo de la clausura de una imagen en escala de grises
# Paso 1: Dilatacion
DA = dilate_gray(A, B) # aplicacion de la diltacion
# Paso 2: Erosion
EA = erode_gray(DA, B) # aplicacion de la erosion
# Paso 3: Aplicar la transformada de Bottom-Hat
CL = EA - A

plt.subplot(132) # posicionamiento de la nueva imagen
plt.title("Imagen Apertura Top-Hat") 
plt.imshow(A + AP, cmap='gray', vmin = 0, vmax = 255, interpolation='none')

plt.subplot(133) # posicionamiento de la nueva imagen
plt.title("Imagen Clausura Bottom-Hat") 
plt.imshow(A + CL, cmap='gray', vmin = 0, vmax = 255, interpolation='none')

plt.show() # despliega y bloque la ventana