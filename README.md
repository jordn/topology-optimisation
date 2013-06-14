# Helper files for creating DXF files from ToPy 
ToPy: https://code.google.com/p/topy/

Installation 


##Instructions
Topy set-up

Download zip file.

python set.up install (puts topy in .virtualenv/[project]/python/site-packages)

pip install numpy matplotlib

ln -s the site packages to this git repo /topy

## To convert to a video
Install ImageMagick
convert vol_frac_0.*tight_100.png -alpha off mp4.mp4


##To convert .png files to a DXF for laser cutting
Install potrace http://potrace.sourceforge.net/ for raster  - > vector
(adds  "potrace.1" and "mkbitmap.1" to usr/local/bin)

potrace -o output.dxf -b dxf input.bmp

Use /scripts/convert_to_dxf.sh

## To convert a half bridge to a trimmed full bridge
Use /scripts/double_up.sh

#License 
ToPy GNU GPL Lisence. Author William Hunter.
https://code.google.com/p/topy/

My additional code under MIT Lisence.
