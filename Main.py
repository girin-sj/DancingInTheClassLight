from PIL import Image, ImageDraw, ImageFont
import random
import numpy as np
import math
from colorsys import hsv_to_rgb
from Joystick import Joystick
from Desk import Desk
from Character import Character


def main():
    joystick = Joystick()
    my_character = Character(joystick.width, joystick.height)
    my_desk = Desk()
    my_image = Image.new("RGB", (joystick.width, joystick.height))
    my_draw = ImageDraw.Draw(my_image)
    joystick.disp.image(my_image)
    IsDancing = False
    IsStudying = False

    img_dancing1 = Image.open(
        '/home/kau-esw/DancingInTheClassLight/Asset/student_dancing1.png', mode='r').convert('RGBA')  # 춤추는 모션1
    img_dancing2 = Image.open(
        '/home/kau-esw/DancingInTheClassLight/Asset/student_dancing2.png', mode='r').convert('RGBA')  # 춤추는 모션2
    img_dancing3 = Image.open(
        '/home/kau-esw/DancingInTheClassLight/Asset/student_dancing3.png', mode='r').convert('RGBA')  # 춤추는 모션3
    img_dancing4 = Image.open(
        '/home/kau-esw/DancingInTheClassLight/Asset/student_dancing4.png', mode='r').convert('RGBA')  # 춤추는 모션4

    img_walking1 = Image.open(
        '/home/kau-esw/DancingInTheClassLight/Asset/student_walking1.png', mode='r').convert('RGBA')  # 걷는 모션1
    img_walking2 = Image.open(
        '/home/kau-esw/DancingInTheClassLight/Asset/student_walking2.png', mode='r').convert('RGBA')  # 걷는 모션2
    img_studying = Image.open(
        '/home/kau-esw/DancingInTheClassLight/Asset/student_studying.png', mode='r').convert('RGBA')  # 공부하는 척 모션

    img_background_set = Image.open(
        '/home/kau-esw/DancingInTheClassLight/Asset/background_set.png', mode='r').convert('RGBA')  # 메인 화면
    img_start = Image.open(
        '/home/kau-esw/DancingInTheClassLight/Asset/start.png', mode='r').convert('RGBA')  # 시작 화면
    img_fail = Image.open(
        '/home/kau-esw/DancingInTheClassLight/Asset/fail.png', mode='r').convert('RGBA')  # 게임오버 화면

    def Start():  # 시작 화면

        while True:
            my_image.paste(im=img_start, box=(0, 0), mask=img_start)
            joystick.disp.image(my_image)
            if not joystick.button_A.value:
                break

    Start()  # 메인 화면 시작

    tmp = 0
    while True:  # 게임 시작
        command = {'move': False, 'up_pressed': False, 'down_pressed': False,
                   'left_pressed': False, 'right_pressed': False}  # 딕셔너리
        animation_dancing = [img_dancing1,
                             img_dancing2, img_dancing3, img_dancing4]
        animation_walking = [img_walking1, img_walking2]

        my_image.paste(im=img_background_set, box=(0, 0),
                       mask=img_background_set)  # 배경 Draw

        # 캐릭터 walking animation
        if (tmp % 6 == 3 or tmp % 6 == 4 or tmp % 6 == 5) and command['move'] == False and IsDancing == False and IsStudying == False:
            my_image.paste(im=animation_walking[0], box=tuple(
                my_character.charPos-25), mask=animation_walking[0])
        elif (tmp % 6 == 0 or tmp % 6 == 1 or tmp % 6 == 2) and command['move'] == False and IsDancing == False and IsStudying == False:
            my_image.paste(im=animation_walking[1], box=tuple(
                my_character.charPos-25), mask=animation_walking[1])
        elif IsDancing == False and IsStudying == False:
            my_image.paste(im=img_walking1, box=tuple(
                my_character.charPos-25), mask=img_walking1)  # 캐릭터 처음 그림

        # 캐릭터 dancing animation
        if (tmp % 8 == 0 or tmp % 8 == 1) and IsDancing == True and IsStudying == False:
            my_image.paste(im=animation_dancing[0], box=tuple(
                my_character.charPos-25), mask=animation_dancing[0])
        elif (tmp % 8 == 2 or tmp % 8 == 3) and IsDancing == True and IsStudying == False:
            my_image.paste(im=animation_dancing[1], box=tuple(
                my_character.charPos-25), mask=animation_dancing[1])
        elif (tmp % 8 == 4 or tmp % 8 == 5) and IsDancing == True and IsStudying == False:
            my_image.paste(im=animation_dancing[2], box=tuple(
                my_character.charPos-25), mask=animation_dancing[2])
        elif (tmp % 8 == 6 or tmp % 8 == 7) and IsDancing == True and IsStudying == False:
            my_image.paste(im=animation_dancing[3], box=tuple(
                my_character.charPos-25), mask=animation_dancing[3])

        # 캐릭터 studying
        if IsStudying == True and IsDancing == False:
            my_image.paste(im=img_studying, box=tuple(
                my_character.charPos-25), mask=img_studying)

        # 조이스틱 눌림 감지
        if not joystick.button_U.value:  # up pressed
            command['up_pressed'] = True
            command['move'] = True
            my_character.check_character_position()

        if not joystick.button_D.value:  # down pressed
            command['down_pressed'] = True
            command['move'] = True
            my_character.check_character_position()

        if not joystick.button_L.value:  # left pressed
            command['left_pressed'] = True
            command['move'] = True
            my_character.check_character_position()

        if not joystick.button_R.value:  # right pressed
            command['right_pressed'] = True
            command['move'] = True
            my_character.check_character_position()

        my_character.move(command)  # 캐릭터 무브 함수에 커맨드를 넣어줌

        # A pressed = Study
        if not joystick.button_A.value and joystick.button_B.value == True:
            IsStudying = True
        else:
            IsStudying = False

        # B pressed = Dance
        if joystick.button_A.value == True and not joystick.button_B.value:
            IsDancing = True
        else:
            IsDancing = False

        joystick.disp.image(my_image)
        tmp += 1


if __name__ == '__main__':
    main()
