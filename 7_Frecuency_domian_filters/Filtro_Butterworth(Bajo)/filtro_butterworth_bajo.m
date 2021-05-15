
%Aplicacion del filtro Butterworth paso-bajos
% a un imagen en escala de grises
clc; clear; close all;
pkg load image

%Carga de imagen a utiliar
A=imread('edificio_china.jpg');
subplot(2,2,1)
imshow(A)
title('Imagen Original')

%Conversiona de dato de la imagen a double
A=im2double(A);
%Aplicacion de la transformada al dominio de la frecuencia
F_A=fftshift(fft2(A));
% Calculo de la Mascara del filtro
[m,n]=size(A);
D0=100;%Frecuencia de corte 
orden=3;%Orden del filtro
F_B=zeros(m,n);%Mascara del filtro
for u=1:m
  for v=1:n
    %Calculo de la distancia
    D_uv=sqrt(u^2+v^2);
    %Calculo de la mascara del filtro segun la formula
    F_B(u,v)=1/(1+(D_uv/D0)**(2*orden));
  endfor
endfor 
%Se completa el circulo del filtro
F_B=completar_mascara(F_B);
F_B=fftshift(F_B);
subplot(2,2,2)
imshow(log(1+abs(F_B)), [])
title('Mascara del filtro Butterworth Paso Bajo')

%Aplciacion del filtro usando el teorema de convoolucion 
%en el domino de la frecuencia.
F_C=F_A.*F_B; 
subplot(2,2,3)
imshow(log(1+abs(F_C)), [])
title('Resultado de la convolucion')
%Aplicar  fftshift a la matriz resultante
% para obtener una imagen similar a la original
F_C=fftshift(F_C);
%Reconstruccion de la iamgen aplicando la tranformada inversa
A_t=ifft2(F_C);
A_t=im2uint8(real(A_t));
subplot(2,2,4)
imshow(A_t)
title('Imagen recontruida')