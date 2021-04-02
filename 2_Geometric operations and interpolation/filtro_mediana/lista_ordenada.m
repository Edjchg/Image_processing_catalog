function booleano = lista_ordenada(lista)
  largo_arreglo = length(lista);
  booleano = 1;
  for i = 1:largo_arreglo
    if(i+1 < largo_arreglo)
      if(lista(i) > lista(i+1))
        booleano = 0;
        break
      endif
    endif
  endfor
endfunction