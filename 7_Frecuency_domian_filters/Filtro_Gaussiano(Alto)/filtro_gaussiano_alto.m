
%Aplicacion del filtro Gaussiano paso altos en una 
%imagen en escala de grises
clc; clear; close all;
pkg load image
%Carga de la imagen a utilizar
A=imread('chest.jpg');
subplot(2,2,1)
imshow(A)
title('Imagen Original')
%Conversion de los tipos de datos de la imagen a double
A=im2double(A);
%Transformacion al dominio de la frecuencia usando la 
% la tranformada discreta de fourier.
F_A=fftshift(fft2(A));
% Calculo de la Mascara del filtro
[m,n]=size(A);
o=1;%Frecuencia de corte para el filtro
F_B=zeros(m,n);%Mascara del filtro
for u=1:m
  for v=1:n
    %Calculo de la distancia 
    D_uv=sqrt(u^2+v^2);
    %Calculo del filtro utilizando la formula
    F_B(u,v)=1-e^(-(D_uv**2/(2*o**2)));
  endfor
endfor 
%Se completa el circulo del filtro 
F_B=completar_mascara(F_B);
F_B=fftshift(F_B);% Se aplica shift para que quede igual de la imagen
subplot(2,2,2)
imshow(log(1+abs(F_B)), [])
title('Mascara del filtro Gaussinao Paso Alto')

%Aplciacion del filtro utilizando el teorema de convolucion
% en el dominio de la frecuencia
F_C=F_A.*F_B;
subplot(2,2,3)
imshow(log(1+abs(F_C)), [])
title('Resultado de la convolucion')
%Aplicar  fftshift a la matriz resultante para obtener
% una imagen similar a la original
F_C=fftshift(F_C);
%Reconstruccion de la imagen aplicando la tranformada inversa
A_t=ifft2(F_C);
%Se utilizan solo los valores reales de la tranformada inversa
A_t=im2uint8(real(A_t));
subplot(2,2,4)
imshow(A_t)
title('Imagen recontruida')