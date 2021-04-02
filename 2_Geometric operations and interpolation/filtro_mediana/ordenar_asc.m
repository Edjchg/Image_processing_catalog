function lista = ordenar_asc(lista_desordenada)
  largo_arreglo = length(lista_desordenada);
  while (lista_ordenada(lista_desordenada) != 1)
    for i = 1:largo_arreglo
      if(i+1 < largo_arreglo)
        if(lista_desordenada(i) > lista_desordenada(i+1))
          lower = lista_desordenada(i+1);
          higher = lista_desordenada(i);
          lista_desordenada(i+1) = higher;
          lista_desordenada(i) = lower;
        endif
      endif
    endfor
  endwhile
  lista = lista_desordenada;
endfunction
