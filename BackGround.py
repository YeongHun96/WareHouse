from pico2d import *


class BackGround:

    def __init__(self):
        self.image = load_image('resource/background.png')

    def draw(self):
        self.image.draw(513, 341)
