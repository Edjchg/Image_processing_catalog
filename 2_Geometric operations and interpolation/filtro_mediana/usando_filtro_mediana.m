clc;clear;close all;
pkg load image


[imagen_sucia, imagen_limpia] = filtro_mediana("barbara.jpg");

figure
subplot(1,2,1)
imshow(imagen_sucia);
title("Imagen sucia");
subplot(1,2,2);
imshow(imagen_limpia);
title("Imagen limpia");
