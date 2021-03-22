function [B,C] = rango_reducido(A, r)
  [U,S,V]=svd(A);
  %Rango reducido
  U_r=U(:,1:r);
  V_r=V(:,1:r);
  S_r=S(1:r,1:r);
  B=U_r*S_r;
  C=V_r';
  %AR=B*C
endfunction
