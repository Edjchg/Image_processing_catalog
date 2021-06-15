function B = umbral_global(A, T)
  % Función que toma una imgen y un valor 
  % de frontera para segmentar la imagen en dos
  % tonalidades de gris.
  % Entradas: - A: una imagen.
  %           - T: valor de frontera.
  % Salidas: - imgen segmentada en dos tonalidades
  % de gris
  A=im2double(A);
  [m n] = size(A);
  B=zeros(m,n);
  B(A>=T)=1;
  B(A<T)=0;
endfunction