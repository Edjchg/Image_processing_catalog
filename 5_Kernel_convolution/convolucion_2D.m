function matriz_convolucion = convolucion_2D(A,B)
  [m, n] = size(A);
  [p, q] = size(B);
  columnas = m+p-1;
  filas = n+q-1;
  C = zeros(filas, columnas);
  
  for i=1:filas
    for j=1:columnas
      
      val_ini_s_1 = max(1, i-p+1);
      val_fin_s_1 = min(i, m);
      
      for r=val_ini_s_1:val_fin_s_1
        
        val_ini_s_2 = max(1, j-q+1);
        val_fin_s_2 = min(j, n);
        
        for s=val_ini_s_2:val_fin_s_2
          C(i,j) += A(r,s)*B(i-r+1, j-s+1);
          
        endfor
        
        
      endfor
      
    endfor
  endfor
  matriz_convolucion = C;
endfunction
