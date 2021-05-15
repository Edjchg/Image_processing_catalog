

%Funcion que completa el circulo 
%cuando se calculo la mascara de
% un filtro en el dominio de la frecuencia.
function B=completar_mascara(A)
  [m,n]=size(A);
  B=zeros(m,n);
  for i=1:round(m/2) %Se copia el cuadrante superior izquierdo 
    for j=1:round(n/2)% en los demas cuadrantes.
      B(i,j)=A(i,j); %Cuadrante superior izquierdo
      B(m-i+1,n-j+1)=A(i,j);%Cuadrante inferior derecho 
      B(m-i+1,j)=A(i,j);%Cuadrante superior derecho
      B(i,n-j+1)=A(i,j);%Cuadrante inferior izquierdo
    endfor
  endfor
endfunction
