import random
from pico2d import *
import Scene_Stage1


class HeadlessKnightSkill:
    image = None

    def __init__(self, x, y):
        self.x, self.y = x, y
        self.MovementSpeed = 20
        self.AttackPower = 5000
        self.frame = 0

        if HeadlessKnightSkill.image is None:
            HeadlessKnightSkill.image = load_image("Resources/EnemyUnits/SkillEffects/Headless_Skill.png")
            # Width = 225, Height = 165 Frame = 6

    def update(self, frame_time):
        self.frame = (self.frame + 1) % 6  # N개의 이미지를 반복 (이동 = 3 공격 = 4)
        self.x += self.MovementSpeed  # 왼쪽으로 10/s 의 속도로 이동

    def draw(self):
        self.image.clip_draw(self.frame * 225, 0, 220, 160, self.x, self.y)
        # 0: 오른쪽 바라보며 공격  1: 왼쪽 바라보며 공격 2 : 오른쪽바라봄 3 : 왼쪽 바라봄

    def get_attack_range(self):
        return self.x - 100, self.y - 80, self.x + 100, self.y + 90

    def draw_bb(self):
        draw_rectangle(*self.get_attack_range())

    def attack(self, e):
        e.Health -= self.AttackPower
        print("공격중인 객체의 체력: ", e.Health)
