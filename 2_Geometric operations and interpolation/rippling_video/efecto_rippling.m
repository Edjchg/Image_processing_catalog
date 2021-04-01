function efecto_rippling(imagen)
  pkg load image
  pkg load video
  A = imread(imagen);
  A = imresize(A, [128 128]);
  [m,n,r] = size(A);
  theta = pi/4;
  x_c = floor(m/2); y_c=floor(n/2);
  B = uint8(zeros(m,n,r));
  frames = 50;
  Y = uint8(zeros(m,n,r,frames));
  L_x = 75; L_y = 75;
  A_x = 5; A_y = 5;
  for i=1:10
    Y(:,:,1,i) = A(:,:,1);
    Y(:,:,2,i) = A(:,:,2);
    Y(:,:,3,i) = A(:,:,3);
  endfor 
  while A_y < 200
    i += 1
    for x=1:m
      for y=1:n
        
        %Eje x
        a_0 = cos(theta); a_1=sin(theta); a_2=x_c-a_0*x_c-a_1*y_c;
        x_t= round(x + A_x*sin(2*pi*y/L_x));
        %Eje y
        b_0=-sin(theta); b_1=cos(theta);b_2=y_c-b_0*x_c-b_1*y_c;
        y_t = round(y + A_y*sin(2*pi*x/L_y));
        if and(x_t>0, y_t>0)
          if and(x_t<=m, y_t<=n)
            B(x_t+1,y_t+1,:)=A(x,y,:);
          endif
        endif
      endfor
    endfor
    Y(:,:,1,i) = B(1:128,1:128,1);
    Y(:,:,2,i) = B(1:128,1:128,2);
    Y(:,:,3,i) = B(1:128,1:128,2);
    A_x += 5;
    A_y += 5;
  endwhile
  video = VideoWriter('video_salida_rippling.mp4');
  for i=1:40;
    writeVideo(video, Y(:,:,:,i));
  endfor
  close(video)
  
endfunction
