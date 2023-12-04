import numpy as np
import math


class Character:
    def __init__(self, width, height):
        # 초기화
        self.charPos = np.array([int(width/2), int(height/2)])  # 캐릭터 위치

    def check_character_position(self):
        # X 위치가 화면을 벗어나는지 체크
        if self.charPos[0] - 25 < 0:  # 화면 왼쪽을 벗어남
            self.charPos[0] = 25
        elif self.charPos[0] > 240:  # 화면 오른쪽을 벗어남
            self.charPos[0] = 240

        # Y 위치가 화면을 벗어나는지 체크
        if self.charPos[1] - 75 < 0:  # 화면 위쪽을 벗어남
            self.charPos[1] = 75
        elif self.charPos[1] > 235:  # 화면 아래쪽을 벗어남
            self.charPos[1] = 235

        return self.charPos

    # 움직임 함수
    def move(self, command=None):
        if command['move'] == False:
            self.state = None
        else:
            self.state = 'move'

            if command['up_pressed']:
                self.charPos[1] -= 5

            if command['down_pressed']:
                self.charPos[1] += 5

            if command['left_pressed']:
                self.charPos[0] -= 5

            if command['right_pressed']:
                self.charPos[0] += 5
