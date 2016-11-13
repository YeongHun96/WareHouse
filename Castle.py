from pico2d import *


class MyCastle:  # 우리 팀의 성

    def __init__(self):
        self.x, self.y = 1200, 300
        self.image = load_image("Resources/MyCastle.png")  # 성의 이미지 불러오기
        self.Health = 10000  # 성의 체력

    def draw(self):
        self.image.draw(1200, 300)  # 이미지를 좌표 (x,y)위치에 삽입

    def get_size(self):
        return self.x - 30, self.y - 54, self.x + 68, self.y + 30
        # 크기 30, 54, 68, 30

    def draw_bb(self):
        draw_rectangle(*self.get_size())


class EnemyCastle:  # 적 팀의 성

    NORMAL, DESTROYED = 0, 1

    def __init__(self):
        self.x, self.y = 50, 270
        self.image = load_image("Resources/EnemyCastle.png")  # 성의 이미지 불러오기
        self.Health = 10000  # 성의 체력

    def draw(self):
        if self.Health < 0:
            self.x, self.y = 1000, 700
        self.image.draw(self.x, self.y)

    def get_size(self):
        return self.x - 90, self.y - 100, self.x + 60, self.y + 100
        # 크기

    def draw_bb(self):
        draw_rectangle(*self.get_size())
