function archivo_ecua_hist
  clc; clear; close all %limpieza/preparacion inicial
  pkg load image %cargado de biblioteca de lectura

  A=imread('sydney.jpg'); %lectura de imagen escala a grises
  subplot(2,2,1) %posicionamiento de imagen en el grafico
  imshow(A) %mostrar imagen original
  title('Imagen Original') %titulo a mostrar de imagen original
  
  [B,H1,H2]=ecua_hist(A); %llamado de la funcion de ecualizacion
  
  subplot(2,2,2) %posicionamiento del histograma de la imagen original
  bar(0:255,H1) %mostrar histograma
  xlim([0 255]) %limita el eje x de la graficacion
  title(['Histograma Imagen Original'])

  subplot(2,2,3) %posicionamiento de imagen ecualizada
  imshow(B) %mostrar imagen transformada
  title(['Imagen Modificada Ecualizada'])

  subplot(2,2,4) %posicionamiento del histograma de la imagen ecualizada
  bar(0:255,H2) %mostrar histograma
  xlim([0 255]) %limita el eje x de la graficacion
  title(['Histograma Imagen Ecualizada'])
endfunction

function [B,H1,H2]=ecua_hist(A)
  %Ecualizacion del histograma 
  % Esta tecnica cambia la distribucion de niveles de grises de una imagen de 
  % tal manera que se obtiene un histograma uniforme, en el que el porcentaje 
  % de pixeles de cada nivel de gris es el mismo.
  %
  % Utiliza la distribucion acumulativa
  %
  %Recibe: una matriz de imagen en valores de 8bits
  %Retorna: 
  % - B: una matriz resultante de imagen de valores de 8bits
  % - H1: el histograma de la imagen original
  % - H2: histograma de la imagen ecualizada
  
  %Forma 2 de calcular el histograma
  H1=zeros(256,1); %h2=[h2(0) h2(1) ... h2(255)]\ vector inicial
  for i=0:255 
    H1(i+1)=sum(sum(A==i)); %suma la frecuencia de cada valor
  end
  
  %Calcular la funcion de distribucion acumulativa
  [m,n]=size(A); %obtencion de las dimensiones
  acv=zeros(256,1); %vector inicial
  for i=0:255
    acv(i+1)=sum(H1(1:i+1))/(m*n); %se obtiene la distribucion acumulativa
  end

  %Metodo de Ecualizacion
  B=zeros(m,n); %matrix inicial de salida
  A=double(A); %conversion de la matriz de entrada a doubles
  for x=1:m
    for y=1:n
      B(x,y)=round(acv(A(x,y)+1)*255); 
      %obtencion de la posicion del valor en la distribucion acumulativa
    endfor
  endfor

  B=uint8(B);

    %Forma 2 de calcular el histograma
  H2=zeros(256,1); %h2=[h2(0) h2(1) ... h2(255)]\ vector inicial
  for i=0:255 
    H2(i+1)=sum(sum(B==i)); %suma la frecuencia de cada valor
  end
endfunction