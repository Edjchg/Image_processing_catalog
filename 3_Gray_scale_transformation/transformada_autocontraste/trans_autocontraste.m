function archivo_autocontraste  clc; clear; close all %limpieza/preparacion inicial  pkg load image %cargado de biblioteca de lectura  A=imread('boat_new.jpg'); %lectura de imagen escala a grises 512*512  subplot(1,2,1) %posicionamiento de imagen en el grafico  imshow(A) %mostrar imagen original  title('Imagen Original') %titulo a mostrar de imagen original    B=trans_autocontraste(A); %llamado de la funcion de autocontraste    subplot(1,2,2) %posicionamiento de imagen transformada en el grafico  imshow(B) %mostrar imagen transformada  title(['Imagen Modificada Transformada Autocontraste'])endfunctionfunction B=trans_autocontraste(A)  %Transformada de autocontraste   % realiza ajustes de valores (contraste) nivelado con los maximos y minimos  % de la imagen, funciona para oscurecer imagenes con balance de blancos alto  % o viceversa  %Realiza la siguiente operacion:  % B = c*A + b  % donde c = 255/r_max-r_min ; b = 255*r_min/(r_max-r_min)  %Recibe: una matriz de imagen en valores de 8bits  %Retorna: una matriz resultante de imagen de valores de 8bits    A=double(A); %conversion de valores de uint8 a double  [m,n]=size(A); %extraccion de tamano de matriz  B=zeros(m,n); %creacion de la matriz resultante vacia  %Autocontraste  rmin=min(min(A)); %valor min de A(imagen original)  rmax=max(max(A)); %valor min de   alpha=255/(rmax-rmin); beta=rmin; %valores intermedios   B=alpha*(A-beta); %aplicacion de la formula    B=uint8(B); %conversion valores de double a uint 8bitsendfunction