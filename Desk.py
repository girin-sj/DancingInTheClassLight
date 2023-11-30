import random
import numpy as np

# 25x28


class Desk:
    def __init__(self, position):
        self.spawnPos = np.array([position[0], position[1]])  # 스폰 위치
        self.spawned_positions = []  # 이미 스폰된 책상 위치를 저장할 리스트

    def __init__(self):
        self.deskList = []  # 책상 리스트

    def spawn_desk(self):
        # 책상의 범위 설정
        desk_width = 240
        desk_height = 196

        # 이미 스폰된 책상 위치를 저장할 리스트 초기화
        self.spawned_positions = []

        # 8개의 책상 스폰
        num_desk = 8
        for _ in range(num_desk):
            # 랜덤한 좌표 생성
            x = random.randint(0, desk_width)
            y = random.randint(0, desk_height)

            # 생성된 좌표가 이미 스폰된 위치인지 확인
            while (x, y) in self.spawned_positions:
                x = random.randint(0, desk_width)
                y = random.randint(0, desk_height)

            # 책상 위치 리스트에 추가
            self.spawned_positions.append((x, y))

        return self.spawned_positions
