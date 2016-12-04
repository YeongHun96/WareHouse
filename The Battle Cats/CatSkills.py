import random   # randint 를 사용하기 위해
from pico2d import*
import Scene_Stage1


class LizardCatSkill:
    image = None

    def __init__(self, x, y):
        self.x, self.y = x, y
        self.MovementSpeed = 20
        self.AttackPower = 5000
        self.frame = 0

        if LizardCatSkill.image is None:
            LizardCatSkill.image = load_image("Resources/CatUnits/SkillEffects/Lizard_Cat_Skill.png")
            # Width = 225, Height = 165 Frame = 6

    def update(self):
        self.frame = (self.frame + 1) % 6  # N개의 이미지를 반복 (이동 = 3 공격 = 4)
        self.x -= self.MovementSpeed
        if self.frame > 4:
            Scene_Stage1.Cat_Skills.remove(self)

    def draw(self):
        self.image.clip_draw(self.frame * 130, 0, 130, 53, self.x, self.y)
        # 0: 오른쪽 바라보며 공격  1: 왼쪽 바라보며 공격 2 : 오른쪽바라봄 3 : 왼쪽 바라봄

    def get_attack_range(self):
        return self.x - 50, self.y - 20, self.x + 50, self.y + 20

    def draw_bb(self):
        draw_rectangle(*self.get_attack_range())

    def attack(self, e):
        e.Health -= self.AttackPower
        print("공격중인 객체의 체력: ", e.Health)


class UFOCatSkill:
    image = None

    def __init__(self, x, y):
        self.x, self.y = x, y
        self.MovementSpeed = 10
        self.AttackPower = 100
        self.frame = 0

        if UFOCatSkill.image is None:
            UFOCatSkill.image = load_image("Resources/CatUnits/SkillEffects/UFO_Cat_Skill.png")
            # Width = 225, Height = 165 Frame = 6

    def update(self):
        self.frame = (self.frame + 1) % 9  # N개의 이미지를 반복 (이동 = 3 공격 = 4)
        self.x -= self.MovementSpeed * 2
        if self.frame > 7:
            Scene_Stage1.Cat_Skills.remove(self)

    # 69, 224
    def draw(self):
        self.image.clip_draw(self.frame * 69, 0, 69, 224, self.x, self.y)
        # 0: 오른쪽 바라보며 공격  1: 왼쪽 바라보며 공격 2 : 오른쪽바라봄 3 : 왼쪽 바라봄

    def get_attack_range(self):
        return self.x - 40, self.y - 100, self.x + 40, self.y + 100

    def draw_bb(self):
        draw_rectangle(*self.get_attack_range())

    def attack(self, e):
        e.Health -= self.AttackPower
        print("공격중인 객체의 체력: ", e.Health)

