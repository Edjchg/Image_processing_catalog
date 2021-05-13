function archivo_filt_prom_arm
  clc; clear; close all %limpieza/preparacion inicial
  pkg load image %cargado de biblioteca de lectura

  A=imread('edificio_china.jpg'); %lectura de imagen escala a grises

  %Crear un ruido del tipo gaussiano con la funcion de Octave imnoise
  B=imnoise(A,'gaussian');

  subplot(1,2,1) %posicionamiento de imagen en el grafico
  imshow(B)
  title('Imagen con Ruido Gaussiano')
  
  A_t=filt_prom_arm(B); %llamado de la funcion Filtro Promedio Armonico
  
  subplot(1,2,2)
  imshow(A_t)
  title('Imagen Filtrada Promedio Armonico')
endfunction

function A_t=filt_prom_arm(B)
  %Filtro promedio armonico
  % Elimina el ruido aditivo de una imagen en escala de grises aplicando
  % el filtro promedio armonico en ventanas de 3x3
  % Es comunmente aplicado a ruidos de tipo gaussiano
  %
  %Recibe: 
  % - B: una matriz de imagen en valores de 8bits en escala de grises
  %Retorna: 
  % - A_t: una matriz resultante de imagen de valores de 8bits
  
  B=double(B); %conversion a double
  [m,n]=size(B); %extraccion de dimensiones
  A_t=zeros(m,n); %creacion de matriz de salida

  %Por conveniencia se calculo en inverso de todos los valores en la
  % matriz
  Binv=B.^-1; %inverso por elemento, potencia -1
  mask=isinf(Binv); %mascara booleana con los valores infinitos
  Binv(mask)=0.0; %con mascara se hacen los valores infinitos

  %Filtrado en esquinas (4)
  %Esquina 1
  %Pixel a modificar: B(1,1)
  %Pixeles: B(1,1), B(1,2), B(2,1), B(2,2)
  W=Binv(1,1)+Binv(1,2)+Binv(2,1)+Binv(2,2);
  A_t(1,1)=4/W;

  %Esquina 2
  %Pixel a modificar: B(1,n)
  %Pixeles: B(1,n), B(1,n-1), B(2,n), B(2,n-1)
  W=Binv(1,n)+Binv(1,n-1)+Binv(2,n)+Binv(2,n-1);
  A_t(1,n)=4/W;

  %Esquina 3
  %Pixel a modificar: B(m,1)
  %Pixeles: B(m,1), B(m,2), B(m-1,1), B(m-1,2)
  W=Binv(m,1)+Binv(m,2)+Binv(m-1,1)+Binv(m-1,2);
  A_t(m,1)=4/W;

  %Esquina 4
  %Pixel a modificar: B(m,n)
  %Pixeles: B(m,n), B(m,n-1), B(m-1,n), B(m-1,n-1)
  W=Binv(m,n)+Binv(m,n-1)+Binv(m-1,n)+Binv(m-1,n-1);
  A_t(m,n)=4/W;


  %Filtrado en bordes
  %Borde superior
  %Pixel a modificar: B(1,y)
  for y=2:n-1
    Wnf1=Binv(1,y-1)+Binv(1,y)+Binv(1,y+1); %Fila 1
    Wnf2=Binv(2,y-1)+Binv(2,y)+Binv(2,y+1); %Fila 2
    A_t(1,y)=6/(Wnf1+Wnf2);
  %Borde inferior
  %Pixel a modificar: B(m,y)
    Wnf1=Binv(m-1,y-1)+Binv(m-1,y)+Binv(m-1,y+1); %Fila 1
    Wnf2=Binv(m,y-1)+Binv(m,y)+Binv(m,y+1); %Fila 2
    A_t(m,y)=6/(Wnf1+Wnf2);
  endfor
  %Borde derecho
  %Pixel a modificar: B(x,n)
  for x=2:m-1
    Wnc1=Binv(x-1,n-1)+Binv(x,n-1)+Binv(x+1,n-1); %Col 1
    Wnc2=Binv(x-1,n)+Binv(x,n)+Binv(x+1,n); %Col 2
    A_t(x,n)=6/(Wnc1+Wnc2);
  %Borde izquierdo
  %Pixel a modificar: B(x,1)
    Wnc1=Binv(x-1,1)+Binv(x,1)+Binv(x+1,1); %Col 1
    Wnc2=Binv(x-1,2)+Binv(x,2)+Binv(x+1,2); %Col 2
    A_t(x,1)=6/(Wnc1+Wnc2);
  endfor

  %Filtrado de centros
  %Pixel a modificar: B(x,y)
  for x=2:m-1
    for y=2:n-1
      Wf1=Binv(x-1,y-1)+Binv(x-1,y)+Binv(x-1,y+1); %Fila 1
      Wf2=Binv(x,y-1)+Binv(x,y)+Binv(x,y+1); %Fila 2
      Wf3=Binv(x+1,y-1)+Binv(x+1,y)+Binv(x+1,y+1); %Fila 3
      A_t(x,y)=9/(Wf1+Wf2+Wf3);
    endfor
  endfor

  A_t=uint8(A_t);
endfunction
