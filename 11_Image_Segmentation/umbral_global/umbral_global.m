function B = umbral_global(A, T)
  A=im2double(A);
  [m n] = size(A);
  B=zeros(m,n);
  B(A>=T)=1;
  B(A<T)=0;
endfunction