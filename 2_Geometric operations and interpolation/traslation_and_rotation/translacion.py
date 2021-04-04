
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image


def traslacion(delta_x = 50, delta_y = 50, img = Image.open('barbara.jpg', 'r').convert('L')):
    A = np.array(img)
    m, n = img.size
    B = np.zeros((m, n), dtype=np.uint8)
    
    for x in range(m-1):
        for y in range(n-1):         
            x_t = x + delta_x
            y_t = y + delta_y
            if x_t < m and y_t < n:
                B[x_t][y_t] = np.uint8(A[x, y])
    
    img_salida = Image.fromarray(B, 'L')
    img_salida.save('img_salida.jpg')
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