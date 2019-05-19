import os
import time
from sys import exit, argv
from PIL import Image
import unicornhathd as unicorn

unicorn.brightness(0.25)
unicorn.rotation(180)
folder_path = '/home/pi/Desktop/PNG/selfpng/'
icon_extension = '.png'
width, height = unicorn.get_shape()
cycle_time = 0.25



def draw_animation(image):

    try:

        for o_x in range(int(image.size[0] / width)):
            for o_y in range(int(image.size[1] / height)):
                valid = False

                for x in range(width):
                    for y in range(height):
                        pixel = image.getpixel(((o_x * width) + y, (o_y * height) + x))
                        r, g, b = int(pixel[0]), int(pixel[1]), int(pixel[2])
                        if r or g or b:
                            valid = True
                        unicorn.set_pixel(x, y, r, g, b)

                if valid:
                    unicorn.show()
                    time.sleep(cycle_time)

    except KeyboardInterrupt:
        unicorn.off()


def loop(imge):

    img = Image.open(folder_path + imge + ".png")
    draw_animation(img)

    unicorn.off()



if '__name__' == '__main__':
        weather_icons()
