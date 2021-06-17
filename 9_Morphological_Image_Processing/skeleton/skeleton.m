function archivo_skeleton
  clc; clear; close all %limpieza/preparacion inicial
  pkg load image %cargado de biblioteca de lectura

  A=imread('imagen9.jpg'); %lectura de imagen escala a grises

  subplot(1,2,1)
  imshow(A)
  title('Imagen Original')
  A=binaria(im2double(A));

  %Elemento Estructurado
  B=ones(5);
  
  C=skeleton(A,B,1); %llamado de la funcion de esqueleto
  
  subplot(1,2,2)
  imshow(C)
  title('Finalizado')
endfunction


function S=skeleton(A,B,gui=0)
  %Esqueleto de una figura
  % 
  %Recibe: 
  % - A: una matriz de imagen binaria
  % - B: elemento estructurado
  % - iterMax: numero de iteraciones maximas para el algoritmo del esqueleto**
  % - gui: opcion para realizar el graficado interactivo
  %Retorna: 
  % - S: una matriz resultante de imagen binaria con el esqueleto

  k=0; %valor inicial de k
  KB=A; %se iguala como valor inicial de KB
  S=zeros(size(A)); %valor inicial de S como ceros
  A_KB=imerode(A,KB); %valor inicial de erosion
  
  %Se itera con un do until hasta que el valor de A erosion KB sea vacio
  while(size(find(A_KB),1)>0)
    A_KB=imerode(A,KB); %calculo de (A erosion KB)
    Sk=A_KB&~(imopen(A_KB,B)); %calculo de cada Sk
    S=S|Sk; %se hace la union de los valores en S con el Sk
    %Calculo de KB = ((A erosion B) erosion B ...) k veces
    %Se guarda el valor obtenido anteriormente por eficiencia
    KB=imerode(KB,B);
    k++
    
    %Para no durar mucho se tiene esta condicion de parada para terminar en
    % en la iteracion 10000
    if(k>50000)
      break;
    endif
  endwhile
endfunction