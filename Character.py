import numpy as np
import math


class Character:
    def __init__(self, width, height):
        # 초기화
        self.charPos = np.array([int(width/2), int(height/2)])  # 캐릭터 위치

    # 움직임 함수
    def move(self, command=None):
        if command['move'] == False:
            self.state = None

        else:
            self.state = 'move'

            if command['up_pressed']:
                self.charPos[1] -= 10

            if command['down_pressed']:
                self.charPos[1] += 10

            if command['left_pressed']:
                self.charPos[0] -= 10

            if command['right_pressed']:
                self.charPos[0] += 10
