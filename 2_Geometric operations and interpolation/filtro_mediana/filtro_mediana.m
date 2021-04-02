
%function [imagen_sucia, imagen_limpia]  = filtro_mediana(imagen_str)
function [imagen_sucia, imagen_limpia]  = filtro_mediana(imagen_str)
  %Con una ventana de 3x3:
  %Leyendo la imagen.
  imagen_sucia = imread(imagen_str);
  %Tomando un canal de la imagen.
  imagen_sucia = imagen_sucia(:,:,1);
  %Sacando las dimensiones de la imagen.
  [m,n] = size(imagen_sucia);
  %Creando una matriz de ceros del mismo tamaño que la imagen.
  imagen_limpia = uint8(zeros(m,n,1));
  %Calculando el elemento medio de la lista.
  elemento_medio = round(9/2);
  %Creando la lista de ceros que será la ventana puesta en una lista.
  kernel_a_lista = uint8(zeros(1,9));
  for i = 1: m
    for j = 1: n
      kernel_a_lista(1) = tomar_pixel(imagen_sucia, m, n, i-1, j-1);
      kernel_a_lista(2) = tomar_pixel(imagen_sucia, m, n, i, j-1);
      kernel_a_lista(3) = tomar_pixel(imagen_sucia, m, n, i+1, j-1);
      kernel_a_lista(4) = tomar_pixel(imagen_sucia, m, n, i-1, j);
      kernel_a_lista(5) = tomar_pixel(imagen_sucia, m, n, i, j);
      kernel_a_lista(6) = tomar_pixel(imagen_sucia, m, n, i+1, j);
      kernel_a_lista(7) = tomar_pixel(imagen_sucia, m, n, i-1, j+1);
      kernel_a_lista(8) = tomar_pixel(imagen_sucia, m, n, i, j+1);
      kernel_a_lista(9) = tomar_pixel(imagen_sucia, m, n, i+1, j+1);
      kernel_a_lista = ordenar_asc(kernel_a_lista);
      imagen_limpia(i,j, 1) = kernel_a_lista(elemento_medio);
    endfor
  endfor
endfunction