from PIL import Image, ImageDraw
from Joystick import Joystick
from Eum import Eum
from Character import Character
import time
import random


def main():
    joystick = Joystick()
    my_character = Character(joystick.width, joystick.height)
    my_image = Image.new("RGB", (joystick.width, joystick.height))
    my_draw = ImageDraw.Draw(my_image)
    joystick.disp.image(my_image)
    my_eum = Eum()

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

    img_professor = Image.open(
        '/home/kau-esw/DancingInTheClassLight/Asset/professor.png', mode='r').convert('RGBA')  # 칠판 보시는 교수님
    img_professor_turn = Image.open(
        '/home/kau-esw/DancingInTheClassLight/Asset/professor_before_turn.png', mode='r').convert('RGBA')  # 뒤돌아보시려는 교수님
    img_professor_look = Image.open(
        '/home/kau-esw/DancingInTheClassLight/Asset/professor_look.png', mode='r').convert('RGBA')  # 뒤돌아보시는 교수님

    img_bar = Image.open(
        '/home/kau-esw/DancingInTheClassLight/Asset/bar.png', mode='r').convert('RGBA')  # 흥 게이지 바
    img_eum = Image.open(
        '/home/kau-esw/DancingInTheClassLight/Asset/eumppyo.png', mode='r').convert('RGBA')  # 음표

    img_background_set = Image.open(
        '/home/kau-esw/DancingInTheClassLight/Asset/background_set.png', mode='r').convert('RGBA')  # 메인 화면
    img_start = Image.open(
        '/home/kau-esw/DancingInTheClassLight/Asset/start.png', mode='r').convert('RGBA')  # 시작 화면
    img_fail = Image.open(
        '/home/kau-esw/DancingInTheClassLight/Asset/fail.png', mode='r').convert('RGBA')  # 게임오버 화면
    img_fail2 = Image.open(
        '/home/kau-esw/DancingInTheClassLight/Asset/fail2.png', mode='r').convert('RGBA')  # 게임오버 교수님 화면

    def Start():  # 시작 화면

        while True:
            my_image.paste(im=img_start, box=(0, 0), mask=img_start)
            joystick.disp.image(my_image)
            if not joystick.button_A.value:
                break

    def Fail():  # 실패 화면
        my_image.paste(im=img_fail2, box=(0, 0), mask=img_fail2)  # 교수님 화면 Draw
        joystick.disp.image(my_image)
        time.sleep(4)
        while True:
            my_image.paste(im=img_fail, box=(0, 0),
                           mask=img_fail)  # 실패 화면 Draw
            joystick.disp.image(my_image)
            # 게임 진행하면서 수정된 값들 초기화
            my_character.danceGage = 185
            my_character.charPos[0] = 120
            my_character.charPos[1] = 120
            my_character.gameover = False
            my_character.IsDancing = False
            my_character.IsStudying = False
            my_character.IsTurning = False
            my_character.turnFrame = 0
            my_character.IsEumTime = False
            my_character.professorTime = 0
            my_character.firstSpon = 0
            if not joystick.button_A.value:
                break

    def Clear():  # 클리어 화면
        while True:
            my_image.paste(im=img_start, box=(0, 0), mask=img_start)
            joystick.disp.image(my_image)

    Start()  # 메인 화면 시작

    tmp = 0
    my_character.turnFrame = 0
    my_character.professorTime = 0
    count = 0
    my_character.firstSpon = 0
    random_number = random.randint(50, 70)

    while True:  # 게임 시작

        command = {'move': False, 'up_pressed': False, 'down_pressed': False,
                   'left_pressed': False, 'right_pressed': False}  # 딕셔너리
        animation_dancing = [img_dancing1,
                             img_dancing2, img_dancing3, img_dancing4]
        animation_walking = [img_walking1, img_walking2]
        animation_turning = [img_professor_turn, img_professor_look]
        my_image.paste(im=img_background_set, box=(0, 0),
                       mask=img_background_set)  # 배경 Draw

        my_image.paste(im=img_professor, box=(145, 27), mask=img_professor)
        my_character.IsTurning = False

        # 캐릭터 walking animation
        if (tmp % 6 == 3 or tmp % 6 == 4 or tmp % 6 == 5) and command['move'] == False and my_character.IsDancing == False and my_character.IsStudying == False:
            my_image.paste(im=animation_walking[0], box=tuple(
                my_character.charPos-25), mask=animation_walking[0])
        elif (tmp % 6 == 0 or tmp % 6 == 1 or tmp % 6 == 2) and command['move'] == False and my_character.IsDancing == False and my_character.IsStudying == False:
            my_image.paste(im=animation_walking[1], box=tuple(
                my_character.charPos-25), mask=animation_walking[1])
        elif my_character.IsDancing == False and my_character.IsStudying == False:
            my_image.paste(im=img_walking1, box=tuple(
                my_character.charPos-25), mask=img_walking1)  # 캐릭터 처음 그림

        # 캐릭터 dancing animation
        if (tmp % 8 == 0 or tmp % 8 == 1) and my_character.IsDancing == True and my_character. IsStudying == False:
            my_image.paste(im=animation_dancing[0], box=tuple(
                my_character.charPos-25), mask=animation_dancing[0])
        elif (tmp % 8 == 2 or tmp % 8 == 3) and my_character.IsDancing == True and my_character.IsStudying == False:
            my_image.paste(im=animation_dancing[1], box=tuple(
                my_character.charPos-25), mask=animation_dancing[1])
        elif (tmp % 8 == 4 or tmp % 8 == 5) and my_character.IsDancing == True and my_character.IsStudying == False:
            my_image.paste(im=animation_dancing[2], box=tuple(
                my_character.charPos-25), mask=animation_dancing[2])
        elif (tmp % 8 == 6 or tmp % 8 == 7) and my_character.IsDancing == True and my_character.IsStudying == False:
            my_image.paste(im=animation_dancing[3], box=tuple(
                my_character.charPos-25), mask=animation_dancing[3])

        # 캐릭터 studying
        if my_character.IsStudying == True and my_character.IsDancing == False:
            my_image.paste(im=img_studying, box=tuple(
                my_character.charPos-25), mask=img_studying)

        # 음표 스폰
        if my_character.IsEumTime and my_character.firstSpon == 0:
            my_eum.spawn_eum()
            my_character.firstSpon = 1

        if my_character.IsEumTime:
            my_image.paste(im=img_eum, box=tuple(
                my_eum.spawnPos), mask=img_eum)

        # 음표 먹었는지 체크
        collision = my_eum.overlap(my_character.charPos)
        if my_character.IsEumTime and collision:
            my_character.IsEumTime = False
            collision = False
            my_character.firstSpon = 0

        print(my_character.charPos, my_eum.spawnPos, collision)
        # 교수님 돌리기
        if my_character.professorTime > random_number and count < 10:
            my_character.IsTurning = True
            count += 1
        elif my_character.professorTime > random_number and count >= 10:
            count = 0
            my_character.professorTime = 0
            random_number = random.randint(45, 80)
        else:
            my_character.professorTime += 1

        # 교수님 그리기
        if my_character.IsTurning == True:  # turning
            my_image.paste(im=animation_turning[0], box=(
                145, 27), mask=animation_turning[0])
            if my_character.turnFrame == 6:  # turned
                my_image.paste(im=animation_turning[1], box=(
                    107, 17), mask=animation_turning[1])
                joystick.disp.image(my_image)
                my_character.turnFrame = 0
                my_character.professorTime = 0
                my_character.IsTurning = False
                time.sleep(2)
                # 뒤돌아 봤는데 공부하는 척 안 하면 게임오버 처리
                if my_character.IsStudying == False:
                    my_character.gameover = True
            else:
                my_character.turnFrame += 1
        elif my_character.IsTurning == False:
            my_image.paste(im=img_professor, box=(
                145, 27), mask=img_professor)  # 교수님 처음 그림
            count = 0

         # 조이스틱 눌림 감지
        if not joystick.button_U.value and my_character.IsStudying == False and my_character.IsDancing == False:  # up pressed
            command['up_pressed'] = True
            command['move'] = True
            my_character.check_character_position()

        if not joystick.button_D.value and my_character.IsStudying == False and my_character.IsDancing == False:  # down pressed
            command['down_pressed'] = True
            command['move'] = True
            my_character.check_character_position()

        if not joystick.button_L.value and my_character.IsStudying == False and my_character.IsDancing == False:  # left pressed
            command['left_pressed'] = True
            command['move'] = True
            my_character.check_character_position()

        if not joystick.button_R.value and my_character.IsStudying == False and my_character.IsDancing == False:  # right pressed
            command['right_pressed'] = True
            command['move'] = True
            my_character.check_character_position()

        my_character.move(command)  # 캐릭터 무브 함수에 커맨드를 넣어줌

        # A pressed = Study
        if not joystick.button_A.value and joystick.button_B.value == True:
            my_character.IsStudying = True
        else:
            my_character.IsStudying = False

        # B pressed = Dance
        if joystick.button_A.value == True and not joystick.button_B.value:
            my_character.IsDancing = True
            if my_character.IsEumTime == False:
                my_character.reduceDanceGage()

        else:
            my_character.IsDancing = False

        # 흥 바 Draw
        my_draw.rectangle([(25, 5), (210, 10)], fill=(244, 161, 227))
        my_draw.rectangle(
            [(25, 5), (my_character.danceGage + 25, 10)], fill=(255, 255, 255))
        my_image.paste(im=img_bar, box=(25, 5), mask=img_bar)

        # 게임오버
        if my_character.gameover:
            Fail()

        # 게임클리어
        if my_character.danceGage < 0:
            Clear()

        tmp += 1
        joystick.disp.image(my_image)


if __name__ == '__main__':
    main()
