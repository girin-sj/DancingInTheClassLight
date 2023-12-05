import random
import numpy as np

# 25x28


class Eum:
    def __init__(self):
        self.spawnPos = np.array([0, 0])  # 스폰 위치

    def spawn_eum(self):
        # 랜덤한 좌표 생성
        x = random.randint(10, 210)
        y = random.randint(70, 210)

        self.spawnPos[0] = x
        self.spawnPos[1] = y

    # 음표 체크
    def overlap(self, char_position):
        return char_position[0] - 10 < self.spawnPos[0] + 25 < char_position[0] + 10 and char_position[1] - 10 < self.spawnPos[1] + 25 < char_position[1] + 10
