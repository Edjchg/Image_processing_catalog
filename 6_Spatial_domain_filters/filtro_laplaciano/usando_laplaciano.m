clc;clear;close all
pkg load image

A=imread('Columnas.jpg');
subplot(1,2,1)
imshow(A)

B=filtro_laplaciano('Columnas.jpg');
subplot(1,2,2)
imshow(B)