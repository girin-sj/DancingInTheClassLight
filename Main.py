from PIL import Image, ImageDraw, ImageFont
import random
import numpy as np
import math
from colorsys import hsv_to_rgb
from Joystick import Joystick


def main():
    joystick = Joystick()
    my_image = Image.new("RGB", (joystick.width, joystick.height))
    my_draw = ImageDraw.Draw(my_image)
    joystick.disp.image(my_image)

    img_main = Image.open(
        '/home/kau-esw/DancingInTheClassLight/Asset/background.png', mode='r').convert('RGBA')  # 메인 화면

    def Start():  # 시작 화면
        while True:
            my_image.paste(im=img_main, box=(0, 0), mask=img_main)
            joystick.disp.image(my_image)

    Start()  # 메인 화면 시작


if __name__ == '__main__':
    main()
