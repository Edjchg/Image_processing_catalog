
import numpy as np #  Libreria matematica para operaciones con matrices.
import matplotlib.pyplot as plt # Manejo de graficos
from PIL import Image #Cargar y creacion de imagenes


def traslacion(delta_x = 50, delta_y = 50, 
        img = Image.open('barbara.jpg', 'r').convert('L'), 
        s = True, n_salida = 'img_salida.jpg'):
    #   Funcion traslacion permite mover una imagen 
    #   en escala de grises (0 .. .. .. 255).
    #   El proceso consiste de mover cada pixel de la imagen 
    #   de entrada a una nueva imagen con un offset en x y y.
    #       B[x+offset][y+offset] = A[x][y]
    #    Entrada:
    #           delta_x = Offset en el eje x(default 50)
    #           delta_y = Offset en el eje y(default 50)
    #           img = imagen de entrada(a color o BN) (default barbara.jpg)
    #           s = Guardar imagen (True/False) (default False)
    #           n_salida = Nombre imagen salida con extension
    #   Salida
    #           imagen original
    #           imagen trasladada
    A = np.array(img)  #Conversion de imagen a array
    m, n = img.size
    B = np.zeros((m, n), dtype=np.uint8) # imagen de salida
    
    for x in range(m-1):
        for y in range(n-1):         
            x_t = x + delta_x # Nueva poscion x del pixels
            y_t = y + delta_y # Nueva poscion y del pixels
            # Se el nuevo pixels solo si no 
            # se sale del tamano de la imagen
            if x_t < m and y_t < n: 
                B[x_t][y_t] = np.uint8(A[x, y])

    #Conversion del array de salida en un imagen en 
    # escala de grises.
    img_salida = Image.fromarray(B, 'L')
    if s:
        img_salida.save(n_salida)
    return img.convert('L'), img_salida.convert('L')
    

print("Traslacion de una imagen \n")
gf = plt.figure()

img_e, img_s = traslacion()  
gf.add_subplot(1, 2, 1)
plt.imshow(img_e, cmap ='gray')
plt.title("Imagen original")
gf.add_subplot(1, 2, 2)
plt.imshow(img_s, cmap ='gray')
plt.title("Imagen con traslacion")
plt.show()