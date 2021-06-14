clc;clear; close all;
pkg load image

A=imread("imagen1.jpg");
subplot(1,2,1)
imshow(A)
title("Imagen original")

T=0.5;
B=umbral_global(A,T);
subplot(1,2,2)
imshow(B)
title("Imagen con umbral simple o global")