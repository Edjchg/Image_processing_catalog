clc; clear;
pkg load image
%A = [1 0 1; 4 3 1; -1 0 2; 3 0 -1];
%B = [1 -1 2 3; -4 0 1 5; 3 2 -1 0];
A = imread('boat.jpg');
A = im2double(A);
B =[1 2 1; 0 0 0;-1 -2 -1];

tic
C = convolucion_2D(A,B);
t1=toc

tic
C2 = conv2(A,B);
t2 = toc


subplot(1,2,1)
C = im2uint8(C);
imshow(C)
title("Convolución manual")

subplot(1,2,2)
C2 = im2uint8(C2);
imshow(C2)
title("Convolución Octave")

