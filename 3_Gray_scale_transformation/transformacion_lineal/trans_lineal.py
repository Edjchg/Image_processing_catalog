
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image


def trans_lineal(b=25, c=1, img= Image.open('barbara.jpg', 'r').convert('L')):
    A = np.array(img, dtype=np.double)
    m, n = img.size
    B = np.zeros((m, n), dtype= np.double)
    
    for x in range(m-1):
        for y in range(n-1):         
                B[x, y] = c*A[x, y] + b
    
    B = B.astype(np.uint8)
    img_salida = Image.fromarray(B, 'L')
    img_salida.save('img_salida.jpg')
    return img.convert('L'), img_salida.convert('L')
    


print("Transformacion lineal de una imagen \n")

gf = plt.figure()

img_e, img_s = trans_lineal()  
gf.add_subplot(1, 2, 1)
plt.imshow(img_e, cmap ='gray')
plt.title("Imagen original")
gf.add_subplot(1, 2, 2)
plt.imshow(img_s, cmap ='gray')
plt.title("Imagen con transformada")
plt.show()