
import imageio#Imagenes
import matplotlib.pyplot as plt#Graficos
import numpy as np#Libreria matematica

"""
Replica el cuadrante superior izquierdo de la matriz mk 
en todos los demas

Entrada:
    mk: Matriz de cualquier tamaño
Salida:
    mk: Matriz con los cuatro cuadrantes iguales 
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
Filtro ideal rechaza banda
Aplicado haciendo uso de la transformada de fourier 
disponible en numpy.
Entrada:
    nombre_imagen:Imagen a la que se aplicara el filtro
#Salida:
    A_t:Imagen filtrada
    F_B:Mascara aplicada
    F_C:Resultado en el dominio de la frecuencia del filtrado
"""
def f_idela_rb(nombre_imagen):
    A = imageio.imread(nombre_imagen)
    #Calculo de la tranformada inversa de fourier
    F_A = np.fft.fftshift(np.fft.fft2(A[:,:]))
    #Calculo de la mascara
    m = A.shape[0]
    n= A.shape[1]
    D1=np.zeros([m,n])
    for u in range(m):
        for v in range(n):
            #Calculo de distancias
            D1[u,v]=np.sqrt(u**2+v**2)
    D0=58    #Radio de corte
    W=10  #Ancha de banda de corte
    H=np.ones([m,n])
    #Intersion de matrices
    ind=np.logical_and(D0-W/2<D1, D0+W/2>=D1)
    H[ind]=0
    F_B=completar_mascara(H) #Completacion de la mascara
    F_B=np.fft.fftshift(F_B)
    
    #Aplicar el filtro haciendo uso de la convolucion en el
    # dominio de la frecuencia
    F_C=F_A*F_B

    #fftshift a la matriz resultante para obtener una 
    # imagen similar a la original
    F_C=np.fft.fftshift(F_C)
    #Reconstrunccion de la imagen aplicando tranfroda inversa
    A_t=np.fft.ifft2(F_C)
        
    return A_t, F_B, F_C


img = "periodico_ruido.png"
A = imageio.imread(img)
B, M, RC  = f_idela_rb(img)
plt.figure()
#Imagen original
plt.subplot(221),plt.title("Imagen original")
plt.imshow(A, cmap='gray')
#Mascara 2
plt.subplot(222),plt.title("Mascara filtro ideal rechaza banda")
plt.imshow(np.log(1 + np.abs(M)), cmap='gray')
#Resultado de la convolucion
#Se aplica un shift para observar mejor el resultado
plt.subplot(223),plt.title("Resultado de la convolucion")
plt.imshow(np.log(1 + np.abs(np.fft.fftshift(RC))), cmap='gray')
#Imagen con fft2 inversa
plt.subplot(224),plt.title("Imagen transformada inversa")
plt.imshow(np.uint8(np.abs(B)), cmap='gray')
plt.show()