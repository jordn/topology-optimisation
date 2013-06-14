#!/bin/sh

for file in $*; do
  echo $file;
  convert $file -alpha off -scale 25% -rotate 90 `basename $file .png`.bmp;
  potrace -o `basename $file .png`.dxf -b dxf `basename $file .png`.bmp;
  rm `basename $file .png`.bmp;
done