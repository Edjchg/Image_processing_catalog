
function archivo_logaritmica
  clc; clear; close all 
  pkg load image 

  A=imread('barbara.jpg'); 
  subplot(1,2,1) 
  imshow(A) 
  title('Imagen Original')
 
  B=trans_logaritmica(A); 
  subplot(1,2,2) 
  imshow(B) 
  title(['Imagen Modificada Transformada logaritmica'])
endfunction

function B = trans_logaritmica(A, c=20)
  A=double(A); 
  [m,n]=size(A); 
  B=zeros(m,n);

  B=c*log(1+A);
  
  B=uint8(B);
endfunction
