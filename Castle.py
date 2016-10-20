from pico2d import *


class OurCastle:

    def __init__(self):
        self.health = 10000
        self.image = load_image("resource/아군 기지.png")

    def draw(self):
        self.image.draw(50, 300)


class EnemyCastle:

    def __init__(self):
        self.health = 10000
        self.image = load_image("resource/적팀 기지.png")

    def draw(self):
        self.image.draw(976, 270)
