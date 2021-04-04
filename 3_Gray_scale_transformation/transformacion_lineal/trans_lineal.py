
import numpy as np # Operaciones matematicas con matrices
import matplotlib.pyplot as plt # Graficacion de figuras
from PIL import Image # Cargar y creacion de imagenes


def trans_lineal(b=25, c=1, 
        img= Image.open('barbara.jpg', 'r').convert('L'), 
        s= True, n_salida = "trans_lineal.jpg"):
    #   Funcion para transformaciones lineales generales a 
    #   imagenes en escala de grises. Esta funcion trabaja
    #   modificando el valor de los pixeles de una imagen 
    #   para producir un cambio a la vista del ser humano o
    #   para procesamiento.
    #       B[x][y] = c*A[x][y] + b  
    #   Entradas:
    #           b = Offset lineal para los pixels (default = 25)
    #           c = Factor de escala de pixel (default = 1)
    #           img = Imagen a color o escala de grises(defualt = barbara.jpg)
    #           s = Guardar imagen (True/False)(default = True )
    #           n_salida = Nombre imagen de salida(default = trans_lineal.jpg)
    #   Salida:
    #           Imagen de entrada
    #           Imagen de salida
    A = np.array(img, dtype=np.double) #Conversion de imagen a array tipo double
    m, n = img.size
    B = np.zeros((m, n), dtype= np.double) # Imagen de salida
    
    for x in range(m-1):
        for y in range(n-1):       
            # Se modifica cada pixels segun la operacion descrita arriba 
            # con valores del pixels double.  
                B[x, y] = c*A[x, y] + b 
    
    #Conversion a tipo uint8 para convertir a imagen
    B = B.astype(np.uint8)
    #Creacion de imagen salida
    img_salida = Image.fromarray(B, 'L')
    #Guardo de imagen
    if s:
        img_salida.save(n_salida)
    return img.convert('L'), img_salida.convert('L')
    


print("Transformacion lineal de una imagen \n")
gf = plt.figure()
img_e, img_s = trans_lineal()  
gf.add_subplot(1, 2, 1)
plt.imshow(img_e, cmap ='gray')
plt.title("Imagen original")
gf.add_subplot(1, 2, 2)
plt.imshow(img_s, cmap ='gray')
plt.title("Imagen con transformada lineal")
plt.show()