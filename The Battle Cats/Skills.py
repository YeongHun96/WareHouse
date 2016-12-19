from pico2d import *
import Scene_Stage1


class LaserBeam:

    NORMAL, ATTACK = 0, 1

    def __init__(self, x, y):
        self.x, self.y = x, y
        self.AttackPower = 100
        self.image = load_image("Resources/LaserBeam2.png")
        self.frame = 0
        self.state = self.ATTACK

    def update(self):
        if self.state == self.ATTACK:
            self.frame = (self.frame + 1) % 7  # N개의 이미지를 반복

    def draw(self):
        self.image.clip_draw(self.frame * 800, 400, 800, 400, 1200, 300)

    def get_attack_range(self):
        return self.x - 50, self.y - 20, self.x + 50, self.y + 20

    def draw_bb(self):
        draw_rectangle(*self.get_attack_range())

    def attack(self, e):
        self.state = self.ATTACK
        e.Health -= self.AttackPower
        print("공격중인 객체의 체력: ", e.Health)
