function archivo_filt_punt_med
  clc; clear; close all %limpieza/preparacion inicial
  pkg load image %cargado de biblioteca de lectura

  A=imread('edificio_china.jpg'); %lectura de imagen escala a grises

  %Crear un ruido del tipo sal y pimienta con la funcion de Octave imnoise
  B=imnoise(A,'salt & pepper');

  subplot(1,2,1) %posicionamiento de imagen en el grafico
  imshow(B)
  title('Imagen con Ruido Sal y Pimienta')
  
  A_t=filt_punt_med(B); %llamado de la funcion Filtro Punto Medio
  
  subplot(1,2,2)
  imshow(A_t)
  title('Imagen Filtrada Punto Medio')
endfunction

function A_t=filt_punt_med(B)
  %Filtro del punto medio
  % Elimina el ruido de sal y pimienta de una imagen en escala de 
  % grises aplicando el filtro del punto medio en ventanas de 3x3
  %
  %Recibe: 
  % - B: una matriz de imagen en valores de 8bits en escala de grises
  %Retorna: 
  % - A_t: una matriz resultante de imagen de valores de 8bits
  
  B=im2double(B); %conversion a double
  [m,n]=size(B); %extraccion de dimensiones
  A_t=zeros(m,n); %creacion de matriz de salida

  %Filtrado en esquinas (4)
  %Esquina 1
  %Pixel a modificar: B(1,1)
  %Pixeles: B(1,1), B(1,2), B(2,1), B(2,2)
  Wmax=max(max(B(1:2,1:2))); %max valor de la mascara
  Wmin=min(min(B(1:2,1:2))); %min valor de la mascara
  A_t(1,1)=(Wmax+Wmin)/2;

  %Esquina 2
  %Pixel a modificar: B(1,n)
  %Pixeles: B(1,n), B(1,n-1), B(2,n), B(2,n-1)
  Wmax=max(max(B(1:2,n-1:n))); %max valor de la mascara
  Wmin=min(min(B(1:2,n-1:n))); %min valor de la mascara
  A_t(1,n)=(Wmax+Wmin)/2;

  %Esquina 3
  %Pixel a modificar: B(m,1)
  %Pixeles: B(m,1), B(m,2), B(m-1,1), B(m-1,2)
  Wmax=max(max(B(m-1:m,1:2))); %max valor de la mascara
  Wmin=min(min(B(m-1:m,1:2))); %min valor de la mascara
  A_t(m,1)=(Wmax+Wmin)/2;

  %Esquina 4
  %Pixel a modificar: B(m,n)
  %Pixeles: B(m,n), B(m,n-1), B(m-1,n), B(m-1,n-1)
  Wmax=max(max(B(m-1:m,n-1:n))); %max valor de la mascara
  Wmin=min(min(B(m-1:m,n-1:n))); %min valor de la mascara
  A_t(m,n)=(Wmax+Wmin)/2;


  %Filtrado en bordes
  %Borde superior
  %Pixel a modificar: B(1,y)
  for y=2:n-1
    Wmax=max(max(B(1:2,y-1:y+1))); %max valor de la mascara
    Wmin=min(min(B(1:2,y-1:y+1))); %min valor de la mascara
    A_t(1,y)=(Wmax+Wmin)/2;
  %Borde inferior
  %Pixel a modificar: B(m,y)
    Wmax=max(max(B(m-1:m,y-1:y+1))); %max valor de la mascara
    Wmin=min(min(B(m-1:m,y-1:y+1))); %min valor de la mascara
    A_t(m,y)=(Wmax+Wmin)/2;
  endfor
  %Borde derecho
  %Pixel a modificar: B(x,n)
  for x=2:m-1
    Wmax=max(max(B(x-1:x+1,n-1:n))); %max valor de la mascara
    Wmin=min(min(B(x-1:x+1,n-1:n))); %min valor de la mascara
    A_t(x,n)=(Wmax+Wmin)/2;
  %Borde izquierdo
  %Pixel a modificar: B(x,1)
    Wmax=max(max(B(x-1:x+1,1:2))); %max valor de la mascara
    Wmin=min(min(B(x-1:x+1,1:2))); %min valor de la mascara
    A_t(x,1)=(Wmax+Wmin)/2;
  endfor

  %Filtrado de centros
  %Pixel a modificar: B(x,y)
  for x=2:m-1
    for y=2:n-1
      Wmax=max(max(B(x-1:x+1,y-1:y+1))); %max valor de la mascara
      Wmin=min(min(B(x-1:x+1,y-1:y+1))); %min valor de la mascara
      A_t(x,y)=(Wmax+Wmin)/2.0;
    endfor
  endfor

  A_t=im2uint8(A_t);
endfunction
