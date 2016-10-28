import random   # randint 를 사용하기 위해
from pico2d import*


class State:
    RIGHT_ATTACK = 0
    LEFT_Attack = 1
    LEFT_MOVE = 2
    RIGHT_MOVE = 3


class BasicCat:
    image = None  # 클래스의 객체들이 공유하는 변수를 선언하고 None 값으로 초기화

    def __init__(self):
        self.x, self.y = 970, 170 + random.randint(0, 30)  # 생성 위치
        # 능력치 #
        self.Health = 300  # 체력
        self.Attack_Power = 8  # 공격력
        self.Attack_Range = 140  # 공격사거리
        self.Time_between_attacks = 1.23  # seconds 공격빈도
        self.Movement_Speed = 10  # 이동속도
        self.Attack_Animation = 8   # frame
        self.Recharging_Time = 2.33   # seconds 공격 재장전 시간
        self.state = State.RIGHT_MOVE  # 캐릭터의 기본 상태
        self.frame = 0
        if BasicCat.image is None:  # 만약 변수의 값이 None 이면
            BasicCat.image = load_image("Resources/Cat.png")  # 한 번의 이미지 로딩을 통해 모든 객체들이 이미지 리소스를 공유

    def update(self):
        self.frame = (self.frame + 1) % 3  # N개의 이미지를 반복 (이동 = 3 공격 = 4)
        self.x -= self.Movement_Speed  # 왼쪽으로 10/s 의 속도로 이동

        if 1:  # 적 팀 유닛을 만나면
            pass
        # 공격을 시작한다.

    # 가로 46 세로 63
    def draw(self):
        self.image.clip_draw(self.frame * 46, 2 * 63, 46, 63, self.x, self.y)  # left,bottom,width,height,x,y
        # 0: 오른쪽 바라보며 공격  1: 왼쪽 바라보며 공격 2 : 오른쪽바라봄 3 : 왼쪽 바라봄


class TankCat:
    image = None  # 클래스의 객체들이 공유하는 변수를 선언하고 None 값으로 초기화

    def __init__(self):
        self.Health = 400
        self.AttackPower = 2
        self.AttackRange = 110
        self.TimeBetweenAttacks = 2.23  # per seconds
        self.MovementSpeed = 8
        self.AttackAnimation = 8  # frame
        self.RechargingTime = 8.33
        self.state = State.RIGHT_MOVE
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

        self.x, self.y = 50, 200 + random.randint(0, 30)
        if AxeCat.image is None:  # 만약 변수의 값이 None 이면
            AxeCat.image = load_image("Resources/Axe_Cat.png")  # 한 번의 이미지 로딩을 통해 모든 객체들이 이미지 리소스를 공유

    def update(self):
        self.delay += 1

        if self.delay > 1:
            self.delay = 0
            self.frame = (self.frame + 1) % 3  # Move = 3 Attack = 4
            self.x += self.Movement_Speed

    def draw(self):
        self.image.clip_draw(self.frame * 112, 0*125, 112, 125, self.x, self.y)
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
