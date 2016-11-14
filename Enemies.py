# Python Module : 파이썬의 정의와 문장을 담고 있는 파일
#                그 자체로도 실행 가능하며, 다른 모듈에서 import해서 사용할 수도 있음.
#                import되면 그 자체가 하나의 객체가 됨.
#                Module의 사용 : import 모듈이름
import random
from pico2d import *


class SkeleDog:
    pass


class MummyDog:
    pass


class SkeletonSoldier:  # 스켈레톤 병사 클래스

    image = None  # 클래스의 객체들이 공유하는 변수를 선언하고 None 값으로 초기화

    STOP, MOVE, HURT, ATTACK, ATTACK_EFFECT, DIE = 5, 4, 3, 2, 1, 0  # 상태 정의

    def __init__(self):  # 객체의 초기값 설정
        self.x, self.y = 80, 170 + random.randint(0, 15)  # 생성위치
        self.Health = 400  # 체력
        self.AttackPower = 2  # 공격력
        self.AttackRange = 110  # 공격사거리
        self.TimeBetweenAttacks = 2.23  # per seconds
        self.MovementSpeed = 4  # 이동속도
        self.AttackAnimation = 8  # frame
        self.RechargingTime = 8.33
        self.state = self.MOVE  # 초기상태
        self.frame = 0

        if SkeletonSoldier.image is None:  # 만약 변수의 값이 None 이면
            SkeletonSoldier.image = load_image("Resources/EnemyUnits/SkeletonSoldier.png")  # 한 번의 이미지 로딩을 통해 모든 객체들이 이미지 리소스를 공유

    def update(self):
        if self.state == self.MOVE:
            self.frame = (self.frame + 1) % 4  # N개의 이미지를 반복
            self.x += self.MovementSpeed  # 오른쪽으로 10/s 의 속도로 이동
        elif self.state == self.ATTACK:
            self.frame = (self.frame + 1) % 4  # N개의 이미지를 반복
        elif self.state == self.HURT:
            self.x -= 3
            self.frame = (self.frame + 1) % 1
        elif self.state == self.ATTACK:
            self.frame = (self.frame + 1) % 4
        elif self.state == self.DIE:
            self.frame = (self.frame + 1)

    def draw(self):
        self.image.clip_draw(self.frame * 110, self.state * 114, 110, 114, self.x, self.y)
        # Width = 110, Height = 114

    def get_size(self):
        return self.x - 23, self.y - 31, self.x + 23, self.y + 18

    def draw_bb(self):
        draw_rectangle(*self.get_size())

    def attack(self, e):
        self.state = self.ATTACK
        e.Health -= self.AttackPower
        print("공격중인 객체의 체력: ", e.Health)


class OfficerSkeleton:

    image = None  # 클래스의 객체들이 공유하는 변수를 선언하고 None 값으로 초기화

    STOP, MOVE, HURT, ATTACK, DIE = 5, 4, 3, 2, 1  # 상태 정의

    def __init__(self):  # 객체의 초기값 설정
        self.x, self.y = 80, 170 + random.randint(0, 15)  # 생성위치
        self.Health = 400  # 체력
        self.AttackPower = 2  # 공격력
        self.AttackRange = 110  # 공격사거리
        self.TimeBetweenAttacks = 2.23  # per seconds
        self.MovementSpeed = 4  # 이동속도
        self.AttackAnimation = 8  # frame
        self.RechargingTime = 8.33
        self.state = self.MOVE  # 초기상태
        self.frame = 0

        if OfficerSkeleton.image is None:  # 만약 변수의 값이 None 이면
            OfficerSkeleton.image = load_image("Resources/EnemyUnits/OfficerSkeleton.png")  # 한 번의 이미지 로딩을 통해 모든 객체들이 이미지 리소스를 공유

    def update(self):
        if self.state == self.MOVE:
            self.frame = (self.frame + 1) % 4  # N개의 이미지를 반복
            self.x += self.MovementSpeed  # 오른쪽으로 10/s 의 속도로 이동
        elif self.state == self.ATTACK:
            self.frame = (self.frame + 1) % 4  # N개의 이미지를 반복
        elif self.state == self.HURT:
            self.x -= 3
            self.frame = (self.frame + 1) % 1
        elif self.state == self.ATTACK:
            self.frame = (self.frame + 1) % 4
        elif self.state == self.DIE:
            self.frame = (self.frame + 1)

    def draw(self):
        self.image.clip_draw(self.frame * 106, self.state * 130, 106, 130, self.x, self.y)
        # Width = 106, Height = 130

    def get_size(self):
        return self.x - 30, self.y - 50, self.x + 30, self.y + 40

    def draw_bb(self):
        draw_rectangle(*self.get_size())

    def attack(self, e):
        self.state = self.ATTACK
        e.Health -= self.AttackPower
        print("공격중인 객체의 체력: ", e.Health)


class CommanderSkeleton:
    image = None  # 클래스의 객체들이 공유하는 변수를 선언하고 None 값으로 초기화

    STOP, MOVE, HURT, ATTACK, DIE = 4, 3, 2, 1, 0  # 상태 정의

    def __init__(self):  # 객체의 초기값 설정
        self.x, self.y = 80, 190 + random.randint(0, 15)  # 생성위치
        self.Health = 400  # 체력
        self.AttackPower = 2  # 공격력
        self.AttackRange = 110  # 공격사거리
        self.TimeBetweenAttacks = 2.23  # per seconds
        self.MovementSpeed = 4  # 이동속도
        self.AttackAnimation = 8  # frame
        self.RechargingTime = 8.33
        self.state = self.MOVE  # 초기상태
        self.frame = 0
        self.delay = 0.13

        if CommanderSkeleton.image is None:  # 만약 변수의 값이 None 이면
            CommanderSkeleton.image = load_image("Resources/EnemyUnits/CommanderSkeleton.png")  # 한 번의 이미지 로딩을 통해 모든 객체들이 이미지 리소스를 공유

    def update(self):
        if self.state == self.STOP:
            self.frame = (self.frame + 1) % 4  # N개의 이미지를 반복
        elif self.state == self.MOVE:
            self.frame = (self.frame + 1) % 4  # N개의 이미지를 반복
            self.x += self.MovementSpeed  # 오른쪽으로 10/s 의 속도로 이동
        elif self.state == self.HURT:
            self.x -= 3
            self.frame = (self.frame + 1) % 1
        elif self.state == self.ATTACK:
            self.frame = (self.frame + 1) % 8
        elif self.state == self.DIE:
            self.frame = (self.frame + 1) % 11

    def draw(self):
        self.image.clip_draw(self.frame * 151, self.state * 159, 151, 159, self.x, self.y)
        # Width = 151, Height = 159

    def get_size(self):
        return self.x - 23, self.y - 31, self.x + 23, self.y + 18

    def draw_bb(self):
        draw_rectangle(*self.get_size())

    def attack(self, e):
        self.state = self.ATTACK
        e.Health -= self.AttackPower
        print("공격중인 객체의 체력: ", e.Health)


class HeadlessKnight:  # 보스 몬스터 - 헤들리스나이트의 클래스

    image = None  # 클래스의 객체들이 공유하는 변수를 선언하고 None 값으로 초기화

    RUN_ATTACK, RUN_SLOW, RUN_SKILL, STAND_SKILL, DIE, STAND, RUN_FAST, MOVE, STAND_ATTACK = 0, 1, 2, 3, 4, 5, 6, 7, 8
    # 상태 정의

    def __init__(self):  # 객체의 초기값 설정
        self.x, self.y = 80, 300 + random.randint(0, 30)  # 생성위치
        self.Health = 99999  # 체력
        self.AttackPower = 100  # 공격력
        self.AttackRange = 110  # 공격범위
        self.TimeBetweenAttacks = 2.23  # per seconds
        self.MovementSpeed = 8  # 이동속도
        self.state = self.RUN_ATTACK
        self.frame = 0
        self.delay = 0

        if HeadlessKnight.image is None:
                HeadlessKnight.image = load_image("Resources/EnemyUnits/HeadlessKnight.png")

    def update(self):
        if self.state == self.RUN_ATTACK:
            self.frame = (self.frame + 1)
            self.x += self.MovementSpeed * 2
            if self.frame == 6:
                self.state = self.STAND_SKILL
        elif self.state == self.RUN_SLOW:
            self.frame = (self.frame + 1) % 6  # N개의 이미지를 반복 (이동 = 3 공격 = 4)
            self.x += self.MovementSpeed  # 왼쪽으로 10/s 의 속도로 이동
        elif self.state == self.RUN_SKILL:
            self.x += self.MovementSpeed
            self.frame = (self.frame + 1) % 6  # N개의 이미지를 반복 (이동 = 3 공격 = 4)
        elif self.state == self.STAND_SKILL:
            self.x += self.MovementSpeed * 2
            self.frame = (self.frame + 1) % 6
        elif self.state == self.DIE:
            self.frame = (self.frame + 1)
            self.delay = 0.1
        elif self.state == self.STAND:
            self.frame = (self.frame + 1) % 10
            self.x += self.MovementSpeed
        elif self.state == self.RUN_FAST:
            pass
        elif self.state == self.MOVE:
            pass
        elif self.state == self.STAND_ATTACK:
            pass
        # for enemy in enemies:
        #    if enemy.x - self.x <= self.Attack_Range:  # 적 팀 유닛을 만나면 - 적과 충돌
        #     self.state = self.ATTACK
        # 공격을 시작한다.

    def draw(self):
        self.image.clip_draw(self.frame * 336, self.state * 362, 336, 362, self.x, self.y)
        # 336,362

    def get_size(self):
        return self.x - 23, self.y - 31, self.x + 23, self.y + 18

    def draw_bb(self):
        draw_rectangle(*self.get_size())

    def attack(self, e):
        self.state = self.ATTACK
        e.Health -= self.AttackPower
        print("공격중인 객체의 체력: ", e.Health)


class HeadlessKnightSkill:
    image = None

    def __init__(self):
        self.x, self.y = 80, 230
        self.MovementSpeed = 20
        self.frame = 0

        if HeadlessKnightSkill.image is None:
            HeadlessKnightSkill.image = load_image("Resources/EnemyUnits/SkillEffects/Headless_Skill.png")
            # Width = 225, Height = 165 Frame = 6

    def update(self):
        self.frame = (self.frame + 1) % 6  # N개의 이미지를 반복 (이동 = 3 공격 = 4)
        self.x += self.MovementSpeed  # 왼쪽으로 10/s 의 속도로 이동

    def draw(self):
        self.image.clip_draw(self.frame*225, 0, 220, 160, self.x, self.y)
        # 0: 오른쪽 바라보며 공격  1: 왼쪽 바라보며 공격 2 : 오른쪽바라봄 3 : 왼쪽 바라봄
        # 마법진 302,129
        # 연기 188,90
        # 작은 연기 132, 65

    def get_size(self):
        return self.x - 23, self.y - 31, self.x + 23, self.y + 18

    def draw_bb(self):
        draw_rectangle(*self.get_size())

    def attack(self, e):
        self.state = self.ATTACK
        e.Health -= self.AttackPower
        print("공격중인 객체의 체력: ", e.Health)






