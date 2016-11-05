import random
from pico2d import *


class SkeletonSoldier:
    image = None

    STOP, LEFT_MOVE, BE_ATTACKED, ATTACK, DIE = 5, 4, 3, 2, 0

    def __init__(self):
        self.x, self.y = 80, 170 + random.randint(0, 30)
        self.Health = 400
        self.AttackPower = 2
        self.AttackRange = 110
        self.TimeBetweenAttacks = 2.23  # per seconds
        self.MovementSpeed = 8
        self.AttackAnimation = 8  # frame
        self.RechargingTime = 8.33
        self.state = self.LEFT_MOVE
        self.frame = 0

        if SkeletonSoldier.image is None:
            SkeletonSoldier.image = load_image("Resources/SkeletonSoldier.png")

    def update(self):
        if self.state == self.LEFT_MOVE:
            self.frame = (self.frame + 1) % 3  # N개의 이미지를 반복 (이동 = 3 공격 = 4)
            self.x += self.MovementSpeed  # 왼쪽으로 10/s 의 속도로 이동
        elif self.state == self.ATTACK:
            self.frame = (self.frame + 1) % 4  # N개의 이미지를 반복 (이동 = 3 공격 = 4)
        elif self.state == self.BE_ATTACKED:
            self.x -= 3
            self.frame = (self.frame + 1) % 1
        elif self.state == self.ATTACK:
            self.frame = (self.frame + 1) % 4
        elif self.state == self.DIE:
            self.frame = (self.frame + 1) % 5

        #for enemy in enemies:
        #    if enemy.x - self.x <= self.Attack_Range:  # 적 팀 유닛을 만나면 - 적과 충돌
        #     self.state = self.ATTACK
        # 공격을 시작한다.

    # 가로 46 세로 63
    def draw(self):
        self.image.clip_draw(self.frame * 95, 581, 95, 109, self.x, self.y)  # left,bottom,width,height,x,y
        # 0: 오른쪽 바라보며 공격  1: 왼쪽 바라보며 공격 2 : 오른쪽바라봄 3 : 왼쪽 바라봄


class HeadlessKnight:
    image = None

    DIE, STAND, RUN, MOVE, ATTACK = 4, 5, 6, 7, 8

    def __init__(self):
        self.x, self.y = 80, 300 + random.randint(0, 30)
        self.Health = 400
        self.AttackPower = 2
        self.AttackRange = 110
        self.TimeBetweenAttacks = 2.23  # per seconds
        self.MovementSpeed = 8
        self.AttackAnimation = 8  # frame
        self.RechargingTime = 8.33
        self.state = self.MOVE
        self.frame = 0
        self.delay = 0

        if HeadlessKnight.image is None:
                HeadlessKnight.image = load_image("Resources/HeadlessKnight.png")

    def update(self):
        if self.state == self.MOVE:
            self.frame = (self.frame + 1) % 7  # N개의 이미지를 반복 (이동 = 3 공격 = 4)
            self.x += self.MovementSpeed  # 왼쪽으로 10/s 의 속도로 이동
            delay(0.05)
            if self.x > 300:
                self.state = self.RUN
        elif self.state == self.ATTACK:
            self.x += self.MovementSpeed
            self.frame = (self.frame + 1) % 7  # N개의 이미지를 반복 (이동 = 3 공격 = 4)
        elif self.state == self.RUN:
            self.x += self.MovementSpeed * 2
            self.frame = (self.frame + 1) % 6
        elif self.state == self.DIE:
            self.frame = self.frame + 1
            delay(0.08)
        elif self.state == self.STAND:
            self.frame = (self.frame + 1) % 4

        # for enemy in enemies:
        #    if enemy.x - self.x <= self.Attack_Range:  # 적 팀 유닛을 만나면 - 적과 충돌
        #     self.state = self.ATTACK
        # 공격을 시작한다.

    def draw(self):
        self.image.clip_draw(self.frame * 337, self.state * 367, 300, 300, self.x, self.y)
        # 0: 오른쪽 바라보며 공격  1: 왼쪽 바라보며 공격 2 : 오른쪽바라봄 3 : 왼쪽 바라봄



class RedCyclone:
    image = None

    def __init__(self):
        self.x, self.y = 80, 170 + random.randint(0, 30)  # 생성 위치
        # 능력치 #
        self.Health = 999999  # 체력
        self.Attack_Power = 92000  # 공격력
        self.Attack_Range = 90  # 공격사거리 (area attack)
        self.Time_between_attacks = 0  # seconds 공격빈도
        self.Movement_Speed = 6  # 이동속도
        self.Attack_Animation = 1  # frame
        self.state = self.MOVE  # 캐릭터의 기본 상태
        self.frame = 0

        if RedCyclone.image is None:  # 만약 변수의 값이 None 이면
            RedCyclone.image = load_image("Resources/Cat.png")  # 한 번의 이미지 로딩을 통해 모든 객체들이 공유
