
%Aplicacacion del filtro ideal pasa-bajos 
%en el dominio de la frecuencia.
clc; clear; close all;
pkg load image

%Carga de imagen a utilizar
A=imread('edificio_china.jpg');
subplot(2,2,1)
imshow(A)
title('Imagen Original')

A=im2double(A); %Se cambia el tipo de data de la imagen a double 
%Tranformada al dominio de la frecuencia de la imagen
F_A=fftshift(fft2(A));
% Calculo de la Mascara del filtro
[m,n]=size(A);
D=zeros(m,n); %Matriz de distancias
for u=1:m
  for v=1:n
    D(u,v)=sqrt(u^2+v^2); %Calculo de distancias
  endfor
endfor 
   
D0=100;%Frecuencias de corte
F_B=D<=D0;%Calculo de la mascara
F_B=completar_mascara(F_B);%Completacion de la mascara del filtro
F_B=fftshift(F_B);
subplot(2,2,2)
imshow(log(1+abs(F_B)), [])
title('Mascara del filtro paso bajo ideal')
%Aplicacion el filtro utilizando el teorema de convolucion
% en el domino de la frecuencia
F_C=F_A.*F_B; %Teorema de convolucion
subplot(2,2,3)
imshow(log(1+abs(F_C)), [])
title('Resultado de la convolucion')
%Aplicacion  fftshift a la matriz resultante
%para obtener la imagen original
F_C=fftshift(F_C);
%Reconstruccion de la iamgen aplicando la tranformada inversa
A_t=ifft2(F_C);
%Se utiliza solo la parte real de la tranformada inversa
A_t=im2uint8(real(A_t));
subplot(2,2,4)
imshow(A_t)
title('Imagen recontruida')