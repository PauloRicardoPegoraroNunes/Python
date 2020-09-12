import os

os.system('cvt 1264 768 60')
os.system('xrandr --newmode "1264x768_60.00"   78.75  1264 1328 1456 1648  768 771 781 798 -hsync +vsync')
os.system('xrandr --addmode VGA-1 1264x768_60.00')
os.system('xrandr --output VGA-1 --mode 1264x768_60.00')
