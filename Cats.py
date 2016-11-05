import random   # randint 를 사용하기 위해
from pico2d import*

ATTACK, LEFT_MOVE = 0, 3


class BasicCat:
    image = None  # 클래스의 객체들이 공유하는 변수를 선언하고 None 값으로 초기화

    def __init__(self):
        self.x, self.y = 1200, 170 + random.randint(0, 30)  # 생성 위치
        # 능력치 #
        self.Health = 300  # 체력
        self.Attack_Power = 8  # 공격력
        self.Attack_Range = 140  # 공격사거리
        self.Time_between_attacks = 1.23  # seconds 공격빈도
        self.Movement_Speed = 10  # 이동속도
        self.Attack_Animation = 8   # frame
        self.Recharging_Time = 2.33   # seconds 공격 재장전 시간
        self.state = LEFT_MOVE  # 캐릭터의 기본 상태
        self.frame = 0
        if BasicCat.image is None:  # 만약 변수의 값이 None 이면
            BasicCat.image = load_image("Resources/Cat.png")  # 한 번의 이미지 로딩을 통해 모든 객체들이 이미지 리소스를 공유

    def update(self):
        if self.state == LEFT_MOVE:
            self.frame = (self.frame + 1) % 3  # N개의 이미지를 반복 (이동 = 3 공격 = 4)
            self.x -= self.Movement_Speed  # 왼쪽으로 10/s 의 속도로 이동
        elif self.state == ATTACK:
            self.frame = (self.frame + 1) % 4  # N개의 이미지를 반복 (이동 = 3 공격 = 4)

        #for enemy in enemies:
        #    if enemy.x - self.x <= self.Attack_Range:  # 적 팀 유닛을 만나면 - 적과 충돌
        #     self.state = self.ATTACK
        # 공격을 시작한다.

    # 가로 46 세로 63
    def draw(self):
        self.image.clip_draw(self.frame * 46, self.state * 63, 46, 63, self.x, self.y)  # left,bottom,width,height,x,y
        # 0: 오른쪽 바라보며 공격  1: 왼쪽 바라보며 공격 2 : 오른쪽바라봄 3 : 왼쪽 바라봄


class TankCat:
    image = None  # 클래스의 객체들이 공유하는 변수를 선언하고 None 값으로 초기화

    ATTACK, LEFT_MOVE = 0, 2

    def __init__(self):
        self.Health = 400
        self.AttackPower = 2
        self.AttackRange = 110
        self.TimeBetweenAttacks = 2.23  # per seconds
        self.MovementSpeed = 8
        self.AttackAnimation = 8  # frame
        self.RechargingTime = 8.33
        self.state = self.LEFT_MOVE
        self.frame = 0
    pass


class AxeCat:
    image = None  # 클래스의 객체들이 공유하는 변수를 선언하고 None 값으로 초기화

    def __init__(self):
        self.Health = 200
        self.Attack_Power = 25
        self.Attack_Range = 150
        self.Time_Between_Attacks = 0.9
        self.Movement_Speed = 12
        self.Attack_Animation = 8
        self.Recharging_Time = 7.33
        self.frame = 0
        self.delay = 0
        self.state = LEFT_MOVE

        self.x, self.y = 1200, 200 + random.randint(0, 30)
        if AxeCat.image is None:  # 만약 변수의 값이 None 이면
            AxeCat.image = load_image("Resources/Axe_Cat.png")  # 한 번의 이미지 로딩을 통해 모든 객체들이 이미지 리소스를 공유

    def update(self):
        self.delay += 1

        if self.delay > 1:
            self.delay = 0
            self.frame = (self.frame + 1) % 3  # Move = 3 Attack = 4
            self.x -= self.Movement_Speed

    def draw(self):
        self.image.clip_draw(self.frame * 113, self.state * 125, 112, 125, self.x, self.y)
        # 0 : 오른쪽 바라보며 공격 125 : 왼쪽바라보며공격 250 : 오른쪽 이동 375 : 왼쪽 바라보기


class GrossCat:
    image = None  # 클래스의 객체들이 공유하는 변수를 선언하고 None 값으로 초기화

    def __init__(self):
        self.Health = 400
        self.Attack_Power = 100
        self.Attack_Range = 350
        self.Time_Between_Attacks = 4.23
        self.Movement_Speed = 10
        self.Attack_Animation = 8
        self.Recharging_Time = 2.53
        self.frame = 0
        self.delay = 0


    pass


class CowCat:
    image = None  # 클래스의 객체들이 공유하는 변수를 선언하고 None 값으로 초기화

    def __init__(self):
        self.Health = 500
        self.Attack_Power = 13
        self.Attack_Range = 140
        self.Time_Between_Attacks = 0.33
        self.Movement_Speed = 30
        self.Attack_Animation = 6
        self.Recharging_Time = 2.33
        self.frame = 0
        self.delay = 0
    pass


class BirdCat:
    image = None  # 클래스의 객체들이 공유하는 변수를 선언하고 None 값으로 초기화

    LEFT_MOVE, ATTACK = 400, 231

    def __init__(self):
        self.Health = 300
        self.Attack_Power = 140
        self.Attack_Range = 170
        self.Time_Between_Attacks = 1.63
        self.Movement_Speed = 10
        self.Attack_Animation = 10
        self.Recharging_Time = 2.33
        self.frame = 0
        self.delay = 0
        self.state = LEFT_MOVE

        self.x, self.y = 1200, 500 + random.randint(0, 30)
        if self.image is None:  # 만약 변수의 값이 None 이면
            self.image = load_image("Resources/UFO_Cat.png")  # 한 번의 이미지 로딩을 통해 모든 객체들이 이미지 리소스를 공유

    def update(self):
        if self.state == LEFT_MOVE:
            self.frame = (self.frame + 1) % 4  # N개의 이미지를 반복 (이동 = 3 공격 = 4)
            self.x -= self.Movement_Speed  # 왼쪽으로 10/s 의 속도로 이동
            self.y += random.randint(-10, 10)
        elif self.state == ATTACK:
            self.frame = (self.frame + 1) % 7  # N개의 이미지를 반복 (이동 = 3 공격 = 4)

    def draw(self):
        self.image.clip_draw(self.frame * 132, self.state, 132, 80, self.x, self.y)
        # 0 : 오른쪽 바라보며 공격 125 : 왼쪽바라보며공격 250 : 오른쪽 이동 375 : 왼쪽 바라보기
    pass


class FishCat:
    image = None  # 클래스의 객체들이 공유하는 변수를 선언하고 None 값으로 초기화

    def __init__(self):
        self.Health = 700
        self.Attack_Power = 180
        self.Attack_Range = 150
        self.Time_Between_Attacks = 1.76
        self.Movement_Speed = 10
        self.Attack_Animation = 10
        self.Recharging_Time = 4.53
        self.frame = 0
        self.delay = 0
    pass


class LizardCat:
    image = None  # 클래스의 객체들이 공유하는 변수를 선언하고 None 값으로 초기화

    def __init__(self):
        self.Health = 800
        self.Attack_Power = 350
        self.Attack_Range = 400
        self.Time_Between_Attacks = 4.30
        self.Movement_Speed = 10
        self.Attack_Animation = 10
        self.Recharging_Time = 316
        self.frame = 0
        self.delay = 0
    pass


class TitanCat:
    image = None  # 클래스의 객체들이 공유하는 변수를 선언하고 None 값으로 초기화

    def __init__(self):
        self.Health = 1000
        self.Attack_Power = 280
        self.Attack_Range = 150
        self.Time_Between_Attacks = 2.23
        self.Movement_Speed = 8
        self.Attack_Animation = 18
        self.Recharging_Time = 27.33
        self.frame = 0
        self.delay = 0
    pass
