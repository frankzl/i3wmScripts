#! /usr/bin/python
import os
import random
from PIL import Image, ImageFilter

im_path = '/home/frankz/Pictures/dm3gyoonrhz.jpg'
im_path = '/home/frankz/Pictures/225772.jpg'
#im_path = '/home/frankz/Pictures/SpiritedAway.jpg'
im_path = '/home/frankz/Pictures/futuristic-city-1600x670-id-27567.jpg'
im = Image.open(im_path)
tuple = im.size
width = tuple[0]
added = 10;
for index in range(0, tuple[0]):
    for index2 in range(0, tuple[1]):
        values = im.getpixel((index,index2))
        #gray = int(max(values[0],values[1],values[2])+min(values[0],values[1],values[2]));

        im.putpixel( (index,index2), ((values[0]+added)%256,(values[1]+added)%256,(values[2]+added)%256))

im.save('/home/frankz/Pictures/modified.jpg', 'JPEG')

os.system('feh --bg-scale ~/Pictures/modified.jpg')
exif_data = im._getexif()
exif_data
