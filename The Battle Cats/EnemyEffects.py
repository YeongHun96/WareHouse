import random
from pico2d import *
import Scene_Stage1


class HeadlessKnightCircle:
    image = None

    def __init__(self):
        self.x, self.y = None, None
        self.frame = 0
        if HeadlessKnightCircle.image is None:
            HeadlessKnightCircle.image = load_image('Resources/EnemyUnits/SkillEffects/Headless_Skill2.png')

    def draw(self, x, y):
        self.image.clip_draw(0, 497, 303, 130, x, y)

    def update(self):
        self.frame = (self.frame + 1) % 1