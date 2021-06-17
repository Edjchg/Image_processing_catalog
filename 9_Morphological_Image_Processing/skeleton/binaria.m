function Y=binaria(X)
  Y=zeros(size(X));
  ind_blanco=(X>=0.5);
  ind_negro=(X<0.5);
  Y(ind_blanco)=1;
  Y(ind_negro)=0;
endfunction