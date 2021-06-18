
import imageio#Imagenes
import matplotlib.pyplot as plt#Graficos
import numpy as np#Libreria matematica

"""
Replica el cuadrante superior izquierdo de la matriz mk 
en todos los demas

Entrada:
    mk: Matriz de cualquier tamaño
Salida:
    mk: Matriz con las cuatro cuadrantes iguales 
"""
def completar_mascara(mk):
    m=mk.shape[0]
    n=mk.shape[1]
    #Recorrido del cuadrante superior izquierdo
    #para ser replicado en los demas cuadrantes
    for i in range(int(m/2)):
        for j in range(int(n/2)):
            mk[m-i-1,n-j-1]=mk[i,j]
            mk[m-i-1,j]=mk[i,j]
            mk[i,n-j-1]=mk[i,j]
    return mk

"""
Filtro Gaussiano paso rechaza banda
Aplicado haciendo uso de la transformada de fourier 
disponible en numpy.
Entrada:
    nombre_imagen:Imagen a la que se aplicara el filtro
#Salida:
    A_t:Imagen filtrada
    F_B:Mascara aplicada
    F_C:Resultado en el dominio de la frecuencia del filtrado
"""
def f_gaussinao_rb(nombre_imagen):
    A = imageio.imread(nombre_imagen)
    #Calculo de la tranformada inversa de fourier
    F_A = np.fft.fftshift(np.fft.fft2(A[:,:]))
    #Calculo de la mascara
    m = A.shape[0]
    n= A.shape[1]
    D1=np.zeros([m,n])
    D0=58 #Frecuencia de corte
    W=10 #Ancha de la banda
    orden=1 #Orden del filtro
    F_B=np.zeros([m,n])
    for u in range(m):
        for v in range(n):
            #Calculo de la distancia
            D_uv=np.sqrt(u**2+v**2)
            #Calculo de la mascara del filtro
            F_B[u,v]=1-np.exp(-(1/2)*((D_uv**2-D0**2)/(D_uv*W))**2)
    #Completacion de la mascara del filtro
    F_B=completar_mascara(F_B)
    F_B=np.fft.fftshift(F_B)
    
    #Aplicacion del filtro por medio del teorema de convolucion
    # en la dominio de la frecuencia
    F_C=F_A*F_B

    #fftshift a la matriz resultante
    F_C=np.fft.fftshift(F_C)
    #Reconstrunccion de la imagen aplicando tranfroda inversa
    A_t=np.fft.ifft2(F_C)
        
    return A_t, F_B, F_C


img = "periodico_ruido.png"
A = imageio.imread(img)
B, M, RC  = f_gaussinao_rb(img)
plt.figure()
#Imagen original
plt.subplot(221),plt.title("Imagen original")
plt.imshow(A, cmap='gray')
#Mascara 2
plt.subplot(222),plt.title("Mascara filtro Gaussiano rechaza banda")
plt.imshow(np.log(1 + np.abs(M)), cmap='gray')
#Resultado de la convolucion
#Se aplica un shift para mostrar mejor el resultado
plt.subplot(223),plt.title("Resultado de la convolucion")
plt.imshow(np.log(1 + np.abs(np.fft.fftshift(RC))), cmap='gray')
#Imagen con fft2 inversa
plt.subplot(224),plt.title("Imagen transformada inversa")
plt.imshow(np.uint8(np.abs(B)), cmap='gray')
plt.show()