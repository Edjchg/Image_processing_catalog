clc;clear;close all
pkg load image

A=imread('child.jpg');
subplot(1,2,1)
imshow(A)

C=filtro_promedio('child.jpg', 50);
subplot(1,2,2)
imshow(C)