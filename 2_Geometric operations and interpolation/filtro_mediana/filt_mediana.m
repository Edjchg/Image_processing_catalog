function I=filt_mediana(A)
  %Ventana de 3x3
  %Sacando las dimensiones de la imagen.
  [m,n,ch] = size(A);
  %Creando una matriz de ceros del mismo tamano que la imagen.
  I = zeros(m,n,ch);
  %Tomando todos los canales de la imagen
  for channel=1:ch
    A_ch=A(:,:,channel);

    %Pixels en las esquinas
    med_ind=round(4/2);
    %Consiguiendo las ventanas de las esquinas (4x4)
    kernel1=A_ch(1:2,1:2);
    kernel2=A_ch(m-1:m,1:2);
    kernel3=A_ch(1:2,n-1:n);
    kernel4=A_ch(m-1:m,n-1:n);
    %Vectorizar y ordenar las ventanas
    kernel1=sort(kernel1(:));
    kernel2=sort(kernel2(:));
    kernel3=sort(kernel3(:));
    kernel4=sort(kernel4(:));
    %Guardar el pixel
    I(1,1,channel)=kernel1(med_ind);
    I(m,1,channel)=kernel2(med_ind);
    I(1,n,channel)=kernel3(med_ind);
    I(m,n,channel)=kernel4(med_ind);

    for i=2:m-1
      %Pixeles en los bordes (costados)
      med_ind=round(6/2);
      %Consiguiendo las ventanas de los bordes (3x2 o 2x3)
      kernel1=A_ch(i-1:i+1,1:2);
      kernel2=A_ch(i-1:i+1,n-1:n);
      %Vectorizar y ordenar las ventanas
      kernel1=sort(kernel1(:));
      kernel2=sort(kernel2(:));
      %Guardar el pixel
      I(i,1,channel)=kernel1(med_ind);
      I(i,n,channel)=kernel2(med_ind);
      for j=2:n-1
        if i==2
          %Pixeles en los bordes (sup-inf)
          med_ind=round(6/2);
          %Consiguiendo las ventanas de los bordes (3x2 o 2x3)
          kernel1=A_ch(1:2,j-1:j+1);
          kernel2=A_ch(m-1:m,j-1:j+1);
          %Vectorizar y ordenar las ventanas
          kernel1=sort(kernel1(:));
          kernel2=sort(kernel2(:));
          %Guardar el pixel
          I(1,j,channel)=kernel1(med_ind);
          I(m,j,channel)=kernel2(med_ind);
        endif

        %Pixeles del centro
        %Calculando el elemento medio de la lista.
        med_ind=round(9/2);
        %Consiguiendo la ventana
        kernel=A_ch(i-1:i+1,j-1:j+1);
        %Vectorizar y ordenar la ventana
        kernel=sort(kernel(:));
        %Guardar el pixel
        I(i,j,channel)=kernel(med_ind);
      endfor
    endfor
  endfor

  I=uint8(I);
endfunction