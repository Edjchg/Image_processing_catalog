
clc; clear; close all;
pkg load image


function Ar=jpeg_decomp(x,n)
  pkg load signal
  %Paso 1: Convertir vector c en matriz 8x8
  Cr=vect2mat_diag(x);
  %Paso 2: Mutiplicar puntualemente Cr y Q
  Q=cuantificacion(n);
  M=Cr.*Q;
  %Paso 3: Calcular la inversa de DCT-2D a M
  P=idct2(M);
  %Paso 4: Redondear P y sumar 128 a cada entrada
  Ar=round(P)+128;
endfunction
 
function x=jpeg_comp(A,n)
  pkg load signal 
  %Parte 1: Restart 128 a cada entrada
  M=A-128;
  %Paso 2: Calcular la DCT-2D
  D=dct2(M);
  %Paso 3: Obtener la matriz cuantiicada
  %Matriz de Cuantificada
  Q=cuantificacion(n);
  %Matriz cuantificada
  C=round(D./Q);
  %Paso 4: Codificar la martriz C en un vector x.
  x=mat2vect_diag(C);
endfunction


#Lectura de imagen a usar
A=imread("flores.bmp");
subplot(121)
imshow(A)
title("Imagen Original")

#Conversiona double para realiar operaciones
A=double(A);
[m,n]=size(A);
#Creacion de variable tipo cell
#para guardar arrays de diferente tamano 
x=cell(m/8, m/8);
#Se hacen for para ir de 8 en 8
for i=1:8:m
  for j=1:8:n
    #Se toman secciones de 8x8 de la matriz
    T=A(i:i+7,j:j+7);
    #Se aplica el metodo de compresion
    # y se guarda en la poscion en la celda
    x(round(i/8)+1,round(j/8)+1)=jpeg_comp(T,50);
  endfor
endfor

#Reconstruccion de la matriz comprimida.
C=zeros(m,n);
for i=1:8:m
  for j=1:8:n
    #Se toman cada posicion de la celda y se aplica
    # la descompresion
    B=jpeg_decomp(cell2mat(x(round(i/8)+1,round(j/8)+1)),50);
    #La matriz 8x8 resultante se coloca en la 
    #imagen de salida en la parte correspondiente.
    C(i:i+7,j:j+7)=B;
  endfor
endfor

D=uint8(C);
subplot(122)
imshow(D)
title("Imagen Descomprimida")