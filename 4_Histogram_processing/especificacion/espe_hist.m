function archivo_ecua_hist
  clc; clear; close all %limpieza/preparacion inicial
  pkg load image %cargado de biblioteca de lectura

  sou=imread('boat.jpg'); %lectura de la imagen fuente escala a grises
  subplot(3,2,1) %posicionamiento de imagen en el grafico
  imshow(sou) %mostrar imagen fuente
  title('Imagen Original') %titulo a mostrar de imagen original

  ref=imread('sydney.jpg'); %lectura de la imagen referencia escala a grises
  subplot(3,2,3) %posicionamiento de imagen en el grafico
  imshow(ref) %mostrar imagen referencia
  title('Imagen de Referencia') %titulo a mostrar de imagen de referencia

  [B,H1,H2]=espe_hist(sou,ref); %llamado de la funcion de ecualizacion
  
  subplot(3,2,2) %posicionamiento del histograma de la imagen original
  bar(0:255,H1) %mostrar histograma
  xlim([0 255]) %limita el eje x de la graficacion
  title(['Histograma Imagen Original'])

  subplot(3,2,4) %posicionamiento del histograma de la imagen de referencia
  bar(0:255,H2) %mostrar histograma
  xlim([0 255]) %limita el eje x de la graficacion
  title(['Histograma Imagen de Referencia'])

  subplot(3,2,5) %posicionamiento de imagen de salida
  imshow(B) %mostrar imagen transformada
  title(['Imagen Resultante'])

  subplot(3,2,6) %posicionamiento del histograma de la imagen de salida
  bar(0:255,imhist(B)) %mostrar histograma
  xlim([0 255]) %limita el eje x de la graficacion
  title(['Histograma Imagen Resultante'])

endfunction

function [B,H1,H2]=espe_hist(sou,ref)
  %Especificacion del histograma
  % Esta tecnica busca transformar el histograma de una imagen para que 
  % se parezca al histograma de otra. En esta se utiliza las 
  % funciones de distribucion acumulativa.
  % 
  %
  %Recibe: 
  % - sou: una imagen fuente en valores de 8bits 
  % - ref: una imagen de referencia para el histograma
  %Retorna: 
  % - B: una matriz resultante de imagen de valores de 8bits
  % - H1: el histograma de la imagen original
  % - H2: histograma de la imagen ecualizada

  %Se crea un vector de almacenamiento de tipo uint8 para indices
  M = zeros(256,1,'uint8'); 

  %Se ejecutan los histograms con la funcion de Octave
  H1 = imhist(sou); 
  H2 = imhist(ref);

  %Se computan las funciones de distribucion acumulativa para 
  % ambas imagenes, de entrada y de referencia
  cdf1 = cumsum(H1) / numel(sou); 
  cdf2 = cumsum(H2) / numel(ref);
  % cumsum : realiza una suma acumulativa de los elementos en una 
  %     dimension m, por defecto la primera no singleton
  % numel : retorna el numero de elementos de un objeto

  %Se realiza el mapep por valor de pixel
  % idx representa el valor en escala de grises a mapear
  % entre los dos histogramas, se busca coincidir la primera con
  % la segunda. Se almacenan los indices mapeados
  for idx = 0 : 255
    [~,ind] = min(abs(cdf1(idx+1) - cdf2));
    M(idx+1) = ind-1;
  end

  %Ahora se aplica el mapeo a la primera imagen
  %La distribucion de la imagen debera verse como la distribucion
  % de la segunda
  B = M(double(sou)+1);
endfunction