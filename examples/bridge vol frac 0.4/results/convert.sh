#!/bin/sh

for file in *.png; do
  echo $file;
  convert $file -alpha off -scale 25% `basename $file .png`.bmp;
  potrace -o `basename $file .png`.dxf -b dxf `basename $file .png`.bmp;
  rm `basename $file .png`.bmp;
done