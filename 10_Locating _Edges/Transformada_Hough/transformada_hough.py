
import imageio#Imagenes
import matplotlib.pyplot as plt#Graficos
import numpy as np#Libreria matematica
from scipy import signal

"""
Transformada de Hough para la deteccion de lineas
rectas en una imagen.
Entrada:
    nombre_imagen:Imagen a procesar
#Salida:
    Grafico.
"""
def hough(nombre_imagen):
    A = imageio.imread(nombre_imagen)

    #nromalizado de la imagen de entrada
    A = A.astype(np.double)/255
    #Kernel para aplicar el filtro de sobel para 
    # resaltar bordes.
    Bx = [[-1, 0, 1],
          [-2, 0, 2],
          [-1, 0, 1]]
    By = [[-1, -2, -1],
          [0, 0, 0],
          [1, 2, 1]]

    #Resaltado de bordes horizontales.
    Cx = signal.convolve2d(A, Bx)
    #Resaltado de bordes verticales.
    Cy = signal.convolve2d(A, By)
    #Conversion a imagen binaria
    B = np.sqrt(np.square(Cx) + np.square(Cy))
    B[B<0.5]=0
    B[B>=0.5]=1

    #Creacion y conversion del array de angulos.
    h1=1
    angulos=np.arange(0,180,h1)
    angulos=np.radians(angulos)

    #Creacion del array de distancias desde el origen.
    m=A.shape[0]
    n=A.shape[1]
    d=np.sqrt(m**2+n**2)
    h2=1
    ps=np.arange(-d,d,h2)

    #Matriz acumulador
    m1=len(angulos)
    n1=len(ps)
    acumulador=np.zeros([m1,n1])
    for i in range(m):
        for j in range(n): 
            #Solo las entradas distintas de cero de procesan
            if B[i,j] != 0:
                for ang_ind in range(len(angulos)):
                    ang=angulos[ang_ind]
                    p=i*np.cos(ang)+j*np.sin(ang)
                    p_ind=np.where(np.abs(ps-p) == np.abs(ps-p).min())[0][0]
                    acumulador[ang_ind,p_ind]+=1
    
    num_lineas=25       
    plt.subplot(222),plt.title("Imagen binaria")
    #Iteraciones para dibujar las lineas
    for i in range(num_lineas):
        #Se extraen los maximos de la matriz acumulador 
        # hasta completar el numero de lineas
        maxA=acumulador.max()
        #Obtencion de los indices de los maximos.
        xp, yp=np.where(acumulador==maxA)

        #Por cada indice donde hay un valor maximo se dibuja una linea.
        for k in range(len(xp)):
            angMax=angulos[xp[k]]
            pMax=ps[yp[k]]

            #Si la linea tiene poca inclinacion se dibuja una 
            # linea recta
            if np.abs(np.sin(angMax))<10**(-5):
                x_v=pMax/np.cos(angMax)
                plt.plot((n,1), (x_v, x_v))
            else:
            #De los contrario de calculan dos puntos de la recta para 
            # dibujarla.
                pendiente=-np.cos(angMax)/np.sin(angMax)
                interseccion=pMax/np.sin(angMax)
                
                y1=pendiente*1+interseccion
                ym=pendiente*m+interseccion
                x1=(1-interseccion)/pendiente
                xn=(n-interseccion)/pendiente
            #Se dibujan lineas crecientes.
                if pendiente > 0:
                    if 0 < y1:
                        plt.plot((y1,n),(1,xn))
                    else:
                        plt.plot((1,ym),(x1,m))
            #Se dibujan lineas descrecientes
                else:
                    if y1>m:
                        plt.plot((ym,n),(m,xn))
                    else:
                        plt.plot((y1,1),(1,x1))
            #Se elimina el maixmo del la matriz acumulador 
            # para dar paso a otro maximo.
            acumulador[xp[k],yp[k]]=0

    
    #Imagen original
    plt.subplot(221),plt.title("Imagen original")
    plt.imshow(A, cmap='gray')
    #Imagen binaria
    plt.subplot(222),plt.title("Imagen binaria")
    plt.imshow(np.uint8(B*255), cmap='gray')

    plt.show()


img = "cuadro.jpg"
hough(img)

