# Python Module : 파이썬의 정의와 문장을 담고 있는 파일
#                그 자체로도 실행 가능하며, 다른 모듈에서 import해서 사용할 수도 있음.
#                import되면 그 자체가 하나의 객체가 됨.
#                Module의 사용 : import 모듈이름
import random   # randint 를 사용하기 위해
from pico2d import*
import Functions
import Castle

current_time = get_time()


# Number 1
class BasicCat:

    image = None  # 클래스의 객체들이 공유하는 변수를 선언하고 None 값으로 초기화

    ATTACK, WALK = 0, 3

    def __init__(self):
        self.x, self.y = 1200, 170 + random.randint(0, 15)  # 생성 위치
        # 능력치 #
        self.Health = 300  # 체력
        self.AttackPower = 8  # 공격력
        self.AttackRange = 140  # 공격사거리
        self.TimeBetweenAttacks = 1.23  # seconds 공격빈도
        self.MovementSpeed = 10  # 이동속도
        self.AttackAnimation = 8   # frame
        self.RechargingTime = 2.33   # seconds 유닛 쿨타임
        self.state = self.WALK  # 캐릭터의 기본 상태
        self.frame = 0

        if BasicCat.image is None:  # 만약 변수의 값이 None 이면
            BasicCat.image = load_image("Resources/CatUnits/Basic_Cat.png")  # 한 번의 이미지 로딩을 통해 모든 객체들이 이미지 리소스를 공유

    def update(self):
        if self.state == self.WALK:
            self.frame = (self.frame + 1) % 3  # N개의 이미지를 반복 (이동 = 3 공격 = 4)
            self.x -= self.MovementSpeed  # 왼쪽으로 10/s 의 속도로 이동
            delay(0.05)
        elif self.state == self.ATTACK:
            self.frame = (self.frame + 1) % 4  # N개의 이미지를 반복 (이동 = 3 공격 = 4)

    # 가로: 46, 세로: 63
    def draw(self):
        self.image.clip_draw(self.frame * 46, self.state * 63, 46, 63, self.x, self.y)

    def get_size(self):
        return self.x - 23, self.y - 31, self.x + 23, self.y + 18

    def draw_bb(self):
        draw_rectangle(*self.get_size())

    def attack(self, e):
        self.state = self.ATTACK
        e.Health -= self.AttackPower
        print("공격중인 객체의 체력: ", e.Health)

    def delete(self):
        del self

    def check_die(self):
        if self.Health < 0:
            return True


# Number 2
class TankCat:

    image = None  # 클래스의 객체들이 공유하는 변수를 선언하고 None 값으로 초기화
    WALK, ATTACK, HURT = 2, 1, 0

    def __init__(self):
        self.x, self.y = 1200, 190 + random.randint(0, 15)  # 생성 위치
        self.Health = 400
        self.AttackPower = 2
        self.AttackRange = 110
        self.TimeBetweenAttacks = 2.23  # per seconds
        self.MovementSpeed = 8
        self.AttackAnimation = 8  # frame
        self.RechargingTime = 8.33
        self.state = self.WALK
        self.frame = 0
        self.hurt_time = 0.0

        if TankCat.image is None:
            TankCat.image = load_image("Resources/CatUnits/Tank_Cat.png")

    def update(self):
        if self.state == self.WALK:
            self.frame = (self.frame + 1) % 3  # N개의 이미지를 반복
            self.x -= self.MovementSpeed  # 왼쪽으로 /s 의 속도로 이동
        elif self.state == self.ATTACK:
            self.frame = (self.frame + 1) % 4  # N개의 이미지를 반복
        elif self.state == self.HURT:
            self.frame = (self.frame + 1) % 1
            self.x += 3
            delay(0.1)
            self.hurt_time += 0.1
            if self.hurt_time > 1.0:
                self.hurt_time = 0.0
                self.state = self.WALK

    # 가로: 88, 세로: 121
    def draw(self):
        self.image.clip_draw(self.frame * 88, self.state * 121, 88, 121, self.x, self.y)

    def get_size(self):
        return self.x - 20, self.y - 50, self.x + 20, self.y + 30
    # 크기 20, 50, 20, 30
    # 사정거리 110

    def draw_bb(self):
        draw_rectangle(*self.get_size())

    def attack(self, e):
        self.state = self.ATTACK
        e.Health -= self.AttackPower
        print("공격중인 객체의 체력: ", e.Health)

    def check_die(self):
        if self.Health < 0:
            return True

    def check_Hurt(self):
        if self.Health < 200:
            return True

    def Hurt(self):
        self.state = self.HURT


class WallCat:
    pass


# Number 3
class AxeCat:

    image = None  # 클래스의 객체들이 공유하는 변수를 선언하고 None 값으로 초기화

    WALK, ATTACK = 1, 0

    def __init__(self):
        self.x, self.y = 1200, 195 + random.randint(0, 15)  # 생성 위치
        self.Health = 200
        self.AttackPower = 25
        self.AttackRange = 150
        self.TimeBetweenAttacks = 0.9
        self.MovementSpeed = 12
        self.AttackAnimation = 8
        self.RechargingTime = 7.33
        self.frame = 0
        self.delay = 0
        self.state = self.WALK

        if AxeCat.image is None:  # 만약 변수의 값이 None 이면
            AxeCat.image = load_image("Resources/CatUnits/Axe_Cat.png")  # 한 번의 이미지 로딩을 통해 모든 객체들이 이미지 리소스를 공유

    def update(self):
        if self.state == self.WALK:
            self.frame = (self.frame + 1) % 3  # N개의 이미지를 반복
            self.x -= self.MovementSpeed  # 왼쪽으로 /s 의 속도로 이동
        elif self.state == self.ATTACK:
            self.frame = (self.frame + 1) % 4  # N개의 이미지를 반복

    # 가로: 109, 세로: 150
    def draw(self):
        self.image.clip_draw(self.frame * 109, self.state * 150, 109, 150, self.x, self.y)

    def get_size(self):
        return self.x - 54, self.y - 60, self.x + 45, self.y + 20
        # 크기 54, 60, 45, 20

    def draw_bb(self):
        draw_rectangle(*self.get_size())

    def attack(self, e):
        self.state = self.ATTACK
        e.Health -= self.AttackPower
        print("공격중인 객체의 체력: ", e.Health)

    def delete(self):
        del self

    def check_die(self):
        if self.Health < 0:
            return True


class BraveCat:
    pass


# Number 4
class GrossCat:
    image = None  # 클래스의 객체들이 공유하는 변수를 선언하고 None 값으로 초기화

    WALK, ATTACK, HURT = 2, 1, 0

    def __init__(self):
        self.x, self.y = 1200, 240 + random.randint(0, 15)  # 생성 위치
        self.Health = 400
        self.AttackPower = 100
        self.AttackRange = 350
        self.TimeBetweenAttacks = 4.23
        self.MovementSpeed = 10
        self.AttackAnimation = 8
        self.RechargingTime = 2.53
        self.frame = 0
        self.delay = 0
        self.state = self.WALK

        if GrossCat.image is None:  # 만약 변수의 값이 None 이면
            GrossCat.image = load_image("Resources/CatUnits/Gross_Cat.png")  # 한 번의 이미지 로딩을 통해 모든 객체들이 이미지 리소스를 공유

    def update(self):
        if self.state == self.WALK:
            self.frame = (self.frame + 1) % 5  # N개의 이미지를 반복
            self.x -= self.MovementSpeed  # 왼쪽으로 /s 의 속도로 이동
            delay(0.05)
        elif self.state == self.ATTACK:
            self.frame = (self.frame + 1) % 4  # N개의 이미지를 반복
        elif self.state == self.HURT:
            self.frame = (self.frame + 1) % 1

    # 가로: 240, 세로: 300
    def draw(self):
        self.image.clip_draw(self.frame * 240, self.state * 300, 240, 300, self.x, self.y)

    def get_size(self):
        return self.x - 40, self.y - 110, self.x + 40, self.y + 80
        # 크기 40, 110, 40, 80

    def draw_bb(self):
        draw_rectangle(*self.get_size())

    def attack(self, e):
        self.state = self.ATTACK
        e.Health -= self.AttackPower
        print("공격중인 객체의 체력: ", e.Health)

    def delete(self):
        del self

    def check_die(self):
        if self.Health < 0:
            return True


class SexyLegsCat:
    pass


# Number 5
class CowCat:

    image = None  # 클래스의 객체들이 공유하는 변수를 선언하고 None 값으로 초기화

    WALK, ATTACK, HURT = 2, 1, 0

    PIXEL_PER_METER = (10.0 / 0.3)
    RUN_SPEED_KMPH = 20.0
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

    def __init__(self):
        self.x, self.y = 1200, 205 + random.randint(0, 15)  # 생성 위치55
        self.Health = 500
        self.AttackPower = 13
        self.AttackRange = 140
        self.TimeBetweenAttacks = 0.33
        self.MovementSpeed = 30
        self.AttackAnimation = 6
        self.RechargingTime = 2.33
        self.frame = 0
        self.delay = 0
        self.state = self.WALK
        if CowCat.image is None:  # 만약 변수의 값이 None 이면
            CowCat.image = load_image("Resources/CatUnits/Cow_Cat.png")  # 한 번의 이미지 로딩을 통해 모든 객체들이 이미지 리소스를 공유

    def update(self):
        #distance = self.RUN_SPEED_PPS * frame_time
        #self.total_frames += 1.0
        #self.total_frames += 1.0
        #self.frame = (self.frame + 1) % 8
        #self.x += (self.dir * distance)


        if self.state == self.WALK:
            self.frame = (self.frame + 1) % 4  # N개의 이미지를 반복
            self.x -= self.MovementSpeed  # 왼쪽으로 /s 의 속도로 이동
        elif self.state == self.ATTACK:
            self.frame = (self.frame + 1) % 4  # N개의 이미지를 반복
            if self.frame == 3:
                self.state = self.WALK
        elif self.state == self.HURT:
            self.frame = (self.frame + 1) % 1
    # 가로: 150, 세로: 200
    def draw(self):
        self.image.clip_draw(self.frame * 150, self.state * 200, 150, 200, self.x, self.y)

    def get_size(self):
        return self.x - 50, self.y - 70, self.x + 50, self.y + 30
        # 크기 50, 70, 50, 30

    def draw_bb(self):
        draw_rectangle(*self.get_size())

    def attack(self, e):
         self.state = self.ATTACK
         e.Health -= self.AttackPower
         print("공격중인 객체의 체력: ", e.Health)

    def normal(self):
        self.state = self.WALK

    def check_die(self):
        if self.Health < 0:
            return True


class GiraffeCat:
    pass


# Number 6
class BirdCat:
    image = None  # 클래스의 객체들이 공유하는 변수를 선언하고 None 값으로 초기화

    FLY, ATTACK, HURT = 2, 1, 0

    def __init__(self):
        self.x, self.y = 1200, 400
        self.Health = 300
        self.AttackPower = 140
        self.AttackRange = 170
        self.TimeBetweenAttacks = 1.63
        self.MovementSpeed = 10
        self.AttackAnimation = 10
        self.RechargingTime = 2.33
        self.frame = 0
        self.delay = 0
        self.state = self.FLY

        if BirdCat.image is None:  # 만약 변수의 값이 None 이면
            BirdCat.image = load_image("Resources/CatUnits/Bird_Cat.png")  # 한 번의 이미지 로딩을 통해 모든 객체들이 이미지 리소스를 공유

    def update(self):
        if self.state == self.FLY:
            self.frame = (self.frame + 1) % 4  # N개의 이미지를 반복 (이동 = 3 공격 = 4)
            self.x -= self.MovementSpeed  # 왼쪽으로 10/s 의 속도로 이동
            self.y += random.randint(-10, 10)
        elif self.state == self.ATTACK:
            self.frame = (self.frame + 1) % 6  # N개의 이미지를 반복
        elif self.state == self.HURT:
            self.frame = (self.frame + 1) % 1

    # 가로: 180, 세로: 120
    def draw(self):
        self.image.clip_draw(self.frame * 180, self.state * 120, 180, 120, self.x, self.y)

    def get_size(self):
        return self.x - 70, self.y - 50, self.x + 70, self.y + 30
        # 크기 70, 50, 70, 30

    def draw_bb(self):
        draw_rectangle(*self.get_size())

    def attack(self, e):
        self.state = self.ATTACK
        e.Health -= self.AttackPower
        print("공격중인 객체의 체력: ", e.Health)

    def delete(self):
        del self

    def check_die(self):
        if self.Health < 0:
            return True


class UFOCat:
    pass


# Number 7
class FishCat:

    image = None  # 클래스의 객체들이 공유하는 변수를 선언하고 None 값으로 초기화

    WALK, ATTACK, HURT = 2, 1, 0

    def __init__(self):
        self.x, self.y = 1200, 205 + random.randint(0, 15)  # 생성 위치
        self.Health = 700
        self.AttackPower = 180
        self.AttackRange = 150
        self.TimeBetweenAttacks = 1.76
        self.MovementSpeed = 10
        self.AttackAnimation = 10
        self.RechargingTime = 4.53
        self.frame = 0
        self.delay = 0
        self.state = self.WALK
        if FishCat.image is None:
            FishCat.image = load_image("Resources/CatUnits/Fish_Cat.png")

    def update(self):
        if self.state == self.WALK:
            self.frame = (self.frame + 1) % 8  # N개의 이미지를 반복
            self.x -= self.MovementSpeed  # 왼쪽으로 /s 의 속도로 이동
        elif self.state == self.ATTACK:
            self.frame = (self.frame + 1) % 4  # N개의 이미지를 반복
        elif self.state == self.HURT:
            self.frame = (self.frame + 1) % 1

    # 가로: 133, 세로: 149
    def draw(self):
        self.image.clip_draw(self.frame * 133, self.state * 149, 133, 149, self.x, self.y)

    def get_size(self):
        return self.x - 68, self.y - 65, self.x + 64, self.y + 40
        # 크기 68, 65, 64, 40

    def draw_bb(self):
        draw_rectangle(*self.get_size())

    def attack(self, e):
        self.state = self.ATTACK
        e.Health -= self.AttackPower
        print("공격중인 객체의 체력: ", e.Health)

    def delete(self):
        del self

    def check_die(self):
        if self.Health < 0:
            return True


# Number 8
class LizardCat:

    image = None  # 클래스의 객체들이 공유하는 변수를 선언하고 None 값으로 초기화

    WALK, ATTACK, HURT = 2, 1, 0

    def __init__(self):
        self.x, self.y = 1200, 205 + random.randint(0, 15)  # 생성 위치
        self.Health = 800
        self.AttackPower = 350
        self.AttackRange = 400
        self.TimeBetweenAttacks = 4.30
        self.MovementSpeed = 10
        self.AttackAnimation = 10
        self.RechargingTime = 316
        self.frame = 0
        self.delay = 0
        self.state = self.WALK
        if LizardCat.image is None:
            LizardCat.image = load_image("Resources/CatUnits/Lizard_Cat.png")

    def update(self):
        if self.state == self.WALK:
            self.frame = (self.frame + 1) % 4  # N개의 이미지를 반복
            self.x -= self.MovementSpeed  # 왼쪽으로 /s 의 속도로 이동
        elif self.state == self.ATTACK:
            self.frame = (self.frame + 1) % 6  # N개의 이미지를 반복
        elif self.state == self.HURT:
            self.frame = (self.frame + 1) % 1

    # 가로: 136, 세로: 109
    def draw(self):
        self.image.clip_draw(self.frame * 136, self.state * 109, 136, 109, self.x, self.y)

    def get_size(self):
        return self.x - 30, self.y - 54, self.x + 68, self.y + 30
        # 크기 30, 54, 68, 30

    def draw_bb(self):
        draw_rectangle(*self.get_size())

    def attack(self, e):
        self.state = self.ATTACK
        e.Health -= self.AttackPower
        print("공격중인 객체의 체력: ", e.Health)

    def delete(self):
        del self

    def check_die(self):
        if self.Health < 0:
            return True


class DragonCat:
    pass


# Number 9
class TitanCat:
    image = None  # 클래스의 객체들이 공유하는 변수를 선언하고 None 값으로 초기화

    WALK, ATTACK, HURT, STOP = 3, 2, 1, 0

    def __init__(self):
        self.x, self.y = 1200, 220 + random.randint(0, 15)  # 생성 위치
        self.Health = 1000
        self.AttackPower = 280
        self.AttackRange = 150
        self.TimeBetweenAttacks = 2.23
        self.MovementSpeed = 8
        self.AttackAnimation = 18
        self.RechargingTime = 27.33
        self.frame = 0
        self.delay = 0
        self.state = self.WALK
        if TitanCat.image is None:
            TitanCat.image = load_image("Resources/CatUnits/Titan_Cat.png")

    def update(self):
        if self.state == self.WALK:
            self.frame = (self.frame + 1) % 6  # N개의 이미지를 반복
            self.x -= self.MovementSpeed  # 왼쪽으로 /s 의 속도로 이동
        elif self.state == self.ATTACK:
            self.frame = (self.frame + 1) % 7  # N개의 이미지를 반복
        elif self.state == self.HURT:
            self.frame = (self.frame + 1) % 1
        elif self.state == self.STOP:
            self.frame = (self.frame + 1) % 1

    # 가로: 200, 세로: 215
    def draw(self):
        self.image.clip_draw(self.frame * 200, self.state * 215, 200, 215, self.x, self.y)

    def get_size(self):
        return self.x - 60, self.y - 107, self.x + 40, self.y + 107
        # 크기 60, 107, 40, 107

    def draw_bb(self):
        draw_rectangle(*self.get_size())

    def attack(self, e):
        self.state = self.ATTACK
        e.Health -= self.AttackPower
        print("공격중인 객체의 체력: ", e.Health)

    def delete(self):
        del self

    def check_die(self):
        if self.Health < 0:
            return True


class MythicalTitanCat:
    pass


class JamieraCat:
    pass
