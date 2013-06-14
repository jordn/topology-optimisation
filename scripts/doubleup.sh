#!/bin/sh

# for file in *.png; do
#   echo $file;
#   convert $file -alpha off -scale 25% `basename $file .png`.bmp;
#   potrace -o `basename $file .png`.dxf -b dxf `basename $file .png`.bmp;
#   rm `basename $file .png`.bmp;
# done

echo $1
IMAGE=$1
convert $IMAGE -trim temp_trim.png
convert temp_trim.png -flop temp_trim_right.png
montage temp_trim.png temp_trim_right.png -geometry +0+0 full_`basename $IMAGE .png`.png 
rm temp_trim.png temp_trim_right.png