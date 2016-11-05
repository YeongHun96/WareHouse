from pico2d import *


class MyCastle:  # 우리 팀의 성

    def __init__(self):
        self.image = load_image("Resources/MyCastle.png")  # 성의 이미지 불러오기
        self.Health = 10000  # 성의 체력

    def draw(self):
        self.image.draw(1200, 300)  # 이미지를 좌표 (x,y)위치에 삽입


class EnemyCastle:  # 적 팀의 성

    def __init__(self):
        self.image = load_image("Resources/EnemyCastle.png")  # 성의 이미지 불러오기
        self.Health = 10000  # 성의 체력

    def draw(self):
        self.image.draw(50, 270)  # 이미지를 좌표 (x,y)위치에 삽입
