
function archivo_logaritmica
  % Funcion de prueba para trans_logaritmica.
  clc; clear; close all 
  pkg load image 

  A=imread('barbara.jpg'); %Carga de imagen
  %Colocacion en el grafico de la primer imagen
  subplot(1,2,1) 
  imshow(A) 
  title('Imagen Original')
  %Aplicacion de transformada
  B=trans_logaritmica(A); 
  %Colocacion de imagen de salida en el grafico
  subplot(1,2,2) 
  imshow(B) 
  title(['Imagen Modificada Transformada logaritmica'])
endfunction

function B = trans_logaritmica(A = imread('barbara.jpg'), c=20, s = 1, n_salida='logaritmica.jpg')
  % Transformada logaritmica de los valores 
  % de una imagen a escala de grises.
  % Se aplica la operacion 
  %       B(x, y) = c*log(1+A(x,y))
  % Entrada:
  %         A = Imagen en escala de grises (default = barbara.jpg)
  %         c = Factor de escala para cada pixels.(default = 20)
  % Salida:
  %         B = imagen modificada
  
  %Conversion de valores de la matriz a doble
  A=double(A);  
  [m,n]=size(A); 
  B=zeros(m,n);% Imagen de salida
  %Operacion a todos los elementos de la matriz
  B=c*log(1+A); 
  #Conversion a uint8 para mostar como imagen.
  B=uint8(B);
  if s
    imwrite(B, n_salida);
  endif
endfunction
