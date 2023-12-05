import numpy as np
import math


class Character:
    def __init__(self, width, height):
        # 초기화
        self.charPos = np.array([int(width/2), int(height/2)])  # 캐릭터 위치
        self.IsEumTime = False
        self.danceGage = 185  # 흥 게이지
        self.gameover = False
        self.IsDancing = False
        self.IsStudying = False
        self.IsTurning = False
        self.turnFrame = 0
        self.professorTime = 0
        self.firstSpon = 0

    def reduceDanceGage(self):
        whenToEumSpon = np.array([160, 110, 60, 30])
        self.danceGage -= 0.8
        for time in whenToEumSpon:
            if (time - 1 < self.danceGage < time):
                self.IsEumTime = True

        return self.danceGage, self.IsEumTime

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

        # 교수님 주변인지 체크
        if 130 < self.charPos[0] < 210 and 74 < self.charPos[1] < 90:
            self.gameover = True
            return self.gameover
        # print(self.charPos[0], self.charPos[1])

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
