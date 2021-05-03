function resultado = filtro_promedio(imagen_str, factor_k)
  A=imread(imagen_str);
  B=(1/factor_k^2)*ones(factor_k,factor_k);
  A=im2double(A);
  resultado=conv2(A,B,'same');
  resultado=im2uint8(resultado);
endfunction
