function pixel = tomar_pixel(imagen, m, n, i_actual, j_actual)
  if(0 < i_actual && i_actual <= m) && (0 < j_actual && j_actual <= n)
    pixel = imagen(i_actual, j_actual, 1);
  else
    pixel = 0;
  endif
endfunction
