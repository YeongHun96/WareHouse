# Python Module : 파이썬의 정의와 문장을 담고 있는 파일
#                그 자체로도 실행 가능하며, 다른 모듈에서 import해서 사용할 수도 있음.
#                import되면 그 자체가 하나의 객체가 됨.
#                Module의 사용 : import 모듈이름
import random   # randint 를 사용하기 위해
from pico2d import*
import Scene_Stage1
import CatSkills


# Number 1
class BasicCat:
    # 프레임 시간에 따른 객체 이동 구현
    PIXEL_PER_METER = (10.0 / 0.3)  # 100픽셀이 10m라고 설정
    RUN_SPEED_KMPH = 5.0  # 시간당 20km
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0) / 60.0  # 분당 m
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)
    # 프레임 시간에 따른 액션 프레임의 조절
    TIME_PER_ACTION = 0.5
    ACTION_PER_TIME = 1 / TIME_PER_ACTION
    FRAMES_PER_MOVE = 3
    FRAMES_PER_ATTACK = 4

    image = None  # 클래스의 객체들이 공유하는 변수를 선언하고 None 값으로 초기화
    hit_sound = None
    die_sound = None

    ATTACK, MOVE, DIE = 1, 3, -1

    def __init__(self):
        self.x, self.y = 1200, 190 + random.randint(0, 10)  # 생성 위치
        # 능력치 #
        self.Health = 300  # 체력
        self.AttackPower = 10  # 공격력
        self.state = self.MOVE  # 캐릭터의 기본 상태
        self.frame = 0
        self.Frames_Move = 3
        self.Frames_Attack = 4

        if BasicCat.image is None:  # 만약 변수의 값이 None 이면
            BasicCat.image = load_image("Resources/CatUnits/Basic_Cat.png")  # 한 번의 이미지 로딩을 통해 모든 객체들이 이미지 리소스를 공유
        if BasicCat.hit_sound is None:
            BasicCat.hit_sound = load_wav('Resources/Musics/Hit3.wav')
            BasicCat.hit_sound.set_volume(30)
        if BasicCat.die_sound is None:
            BasicCat.die_sound = load_wav('Resources/Musics/Die2.wav')
            BasicCat.die_sound.set_volume(30)

    def update(self, frame_time):
        distance = self.RUN_SPEED_PPS * frame_time
        if self.Health < 0:
            BasicCat.die_sound.play(1)
            self.state = self.DIE
        if self.state == self.MOVE:
            self.Frames_Move += self.FRAMES_PER_MOVE * self.ACTION_PER_TIME * frame_time
            self.frame = int(self.Frames_Move + 1) % 3  # N개의 이미지를 반복 (이동 = 3 공격 = 4)
            self.x -= distance  # 왼쪽으로 10/s 의 속도로 이동
        elif self.state == self.ATTACK:
            self.Frames_Attack += self.FRAMES_PER_ATTACK * self.ACTION_PER_TIME * frame_time
            self.frame = int(self.Frames_Attack + 1) % 4  # N개의 이미지를 반복 (이동 = 3 공격 = 4)
            if self.frame > 2:
                BasicCat.hit_sound.play(1)
                self.state = self.MOVE
        elif self.state == self.DIE:
            Scene_Stage1.Cat_Units.remove(self)

    # 가로: 46, 세로: 63
    def draw(self):
        self.image.clip_draw(self.frame * 46, self.state * 63, 46, 63, self.x, self.y)

    def get_attack_range(self):
        return self.x - 23, self.y - 31, self.x + 23, self.y + 18

    def get_defense_size(self):
        return self.x - 23, self.y - 31, self.x + 23, self.y + 18

    def draw_bb(self):
        draw_rectangle(*self.get_attack_range())
        draw_rectangle(*self.get_defense_size())

    def attack(self, e):
        self.state = self.ATTACK
        e.Health -= self.AttackPower
        print("공격중인 객체의 체력: ", e.Health)


# Number 2
class TankCat:
    # 프레임 시간에 따른 객체 이동 구현
    PIXEL_PER_METER = (10.0 / 0.3)  # 100픽셀이 10m라고 설정
    RUN_SPEED_KMPH = 5.0  # 시간당 20km
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0) / 60.0  # 분당 m
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)
    # 프레임 시간에 따른 액션 프레임의 조절
    TIME_PER_ACTION = 0.5
    ACTION_PER_TIME = 1 / TIME_PER_ACTION
    DIE_PER_TIME = 10
    FRAMES_PER_MOVE = 3
    FRAMES_PER_ATTACK = 4

    image = None  # 클래스의 객체들이 공유하는 변수를 선언하고 None 값으로 초기화

    hit_sound = None
    die_sound = None

    MOVE, ATTACK, DIE = 2, 1, 0

    def __init__(self):
        self.x, self.y = 1200, 210 + random.randint(0, 10)  # 생성 위치
        self.Health = 2000
        self.AttackPower = 2
        self.state = self.MOVE
        self.frame = 0
        self.Frame = 0
        self.Frames_Move = 0
        self.Frames_Attack = 0
        self.Frames_Die = 0

        if TankCat.image is None:
            TankCat.image = load_image("Resources/CatUnits/Tank_Cat.png")
        if TankCat.hit_sound is None:
            TankCat.hit_sound = load_wav('Resources/Musics/Hit3.wav')
            TankCat.hit_sound.set_volume(30)
        if TankCat.die_sound is None:
            TankCat.die_sound = load_wav('Resources/Musics/Die2.wav')
            TankCat.die_sound.set_volume(30)

    def update(self, frame_time):
        distance = self.RUN_SPEED_PPS * frame_time
        if self.Health < 0:
            self.state = self.DIE
        if self.state == self.MOVE:
            self.Frames_Move += self.FRAMES_PER_MOVE * self.ACTION_PER_TIME * frame_time
            self.frame = int(self.Frames_Move + 1) % 3  # N개의 이미지를 반복
            self.x -= distance  # 왼쪽으로 /s 의 속도로 이동
        elif self.state == self.ATTACK:
            self.Frames_Attack += self.FRAMES_PER_ATTACK * self.ACTION_PER_TIME * frame_time
            self.frame = int(self.Frames_Attack + 1) % 4  # N개의 이미지를 반복
            if self.frame > 2:
                TankCat.hit_sound.play(1)
                self.state = self.MOVE
        elif self.state == self.DIE:
            self.frame = 0
            self.Frames_Die += self.DIE_PER_TIME * frame_time
            self.Frame = int(self.Frames_Die + 1)
            self.x += 3
            if self.Frame > 1:
                TankCat.die_sound.play(1)
                Scene_Stage1.Cat_Units.remove(self)

    # 가로: 88, 세로: 121
    def draw(self):
        self.image.clip_draw(self.frame * 88, self.state * 121, 88, 121, self.x, self.y)

    def get_attack_range(self):
        return self.x - 5, self.y - 55, self.x + 35, self.y + 25

    def get_defense_size(self):
        return self.x - 5,  self.y - 55, self.x + 35, self.y + 25
    # 크기 20, 50, 20, 30
    # 사정거리 110

    def draw_bb(self):
        draw_rectangle(*self.get_attack_range())
        draw_rectangle(*self.get_defense_size())

    def attack(self, e):
        self.state = self.ATTACK
        e.Health -= self.AttackPower
        print("공격중인 객체의 체력: ", e.Health)

    def move(self):
        self.state = self.MOVE


class WallCat:
    pass


# Number 3
class AxeCat:
    # 프레임 시간에 따른 객체 이동 구현
    PIXEL_PER_METER = (10.0 / 0.3)  # 100픽셀이 10m라고 설정
    RUN_SPEED_KMPH = 5.0  # 시간당 20km
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0) / 60.0  # 분당 m
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)
    # 프레임 시간에 따른 액션 프레임의 조절
    TIME_PER_ACTION = 0.5
    ACTION_PER_TIME = 1 / TIME_PER_ACTION
    FRAMES_PER_MOVE = 3
    FRAMES_PER_ATTACK = 4

    image = None  # 클래스의 객체들이 공유하는 변수를 선언하고 None 값으로 초기화
    hit_sound = None
    die_sound = None

    MOVE, ATTACK, HURT = 1, 0, -1

    def __init__(self):
        self.x, self.y = 1200, 215 + random.randint(0, 10)  # 생성 위치
        self.Health = 300
        self.AttackPower = 30
        self.frame = 0
        self.Frames_Move = 0
        self.Frames_Attack = 0
        self.Frames_Die = 0
        self.state = self.MOVE

        if AxeCat.image is None:  # 만약 변수의 값이 None 이면
            AxeCat.image = load_image("Resources/CatUnits/Axe_Cat.png")  # 한 번의 이미지 로딩을 통해 모든 객체들이 이미지 리소스를 공유
        if AxeCat.hit_sound is None:
            AxeCat.hit_sound = load_wav('Resources/Musics/Hit3.wav')
            AxeCat.hit_sound.set_volume(30)
        if self.die_sound is None:
            self.die_sound = load_wav('Resources/Musics/Die2.wav')
            self.die_sound.set_volume(30)

    def update(self, frame_time):
        distance = self.RUN_SPEED_PPS * frame_time
        if self.state == self.MOVE:
            self.Frames_Move += self.FRAMES_PER_MOVE * self.ACTION_PER_TIME * frame_time
            self.frame = int(self.Frames_Move + 1) % 3  # N개의 이미지를 반복
            self.x -= distance  # 왼쪽으로 /s 의 속도로 이동
        elif self.state == self.ATTACK:
            self.Frames_Attack += self.FRAMES_PER_ATTACK * self.ACTION_PER_TIME * frame_time
            self.frame = int(self.Frames_Attack + 1) % 4  # N개의 이미지를 반복
            if self.frame > 2:
                AxeCat.hit_sound.play(1)
                self.state = self.MOVE
        elif self.state == self.HURT:
            Scene_Stage1.Cat_Units.remove(self)

    # 가로: 109, 세로: 150
    def draw(self):
        self.image.clip_draw(self.frame * 109, self.state * 150, 109, 150, self.x, self.y)

    def get_attack_range(self):
        return self.x - 54, self.y - 60, self.x + 45, self.y + 20

    def get_defense_size(self):
        return self.x - 25, self.y - 60, self.x + 45, self.y + 20
        # 크기 54, 60, 45, 20

    def draw_bb(self):
        draw_rectangle(*self.get_attack_range())
        draw_rectangle(*self.get_defense_size())

    def attack(self, e):
        self.state = self.ATTACK
        e.Health -= self.AttackPower
        print("공격중인 객체의 체력: ", e.Health)

    def move(self):
        self.state = self.MOVE


class BraveCat:
    pass


# Number 4
class GrossCat:
    # 프레임 시간에 따른 객체 이동 구현
    PIXEL_PER_METER = (10.0 / 0.3)  # 100픽셀이 10m라고 설정
    RUN_SPEED_KMPH = 5.0  # 시간당 20km
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0) / 60.0  # 분당 m
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)
    # 프레임 시간에 따른 액션 프레임의 조절
    TIME_PER_ACTION = 1.0
    ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
    FRAMES_PER_MOVE = 5
    FRAMES_PER_ATTACK = 4

    image = None  # 클래스의 객체들이 공유하는 변수를 선언하고 None 값으로 초기화
    hit_sound = None
    die_sound = None

    MOVE, ATTACK, DIE = 2, 1, 0

    def __init__(self):
        self.x, self.y = 1100, 300 + random.randint(0, 15)  # 생성 위치
        self.Health = 400
        self.AttackPower = 100
        self.frame = 0
        self.delay = 0
        self.Frames_Move = 0
        self.Frames_Attack = 0
        self.Frames_Hurt = 0
        self.state = self.MOVE

        if GrossCat.image is None:  # 만약 변수의 값이 None 이면
            GrossCat.image = load_image("Resources/CatUnits/Gross_Cat.png")  # 한 번의 이미지 로딩을 통해 모든 객체들이 이미지 리소스를 공유
        if GrossCat.hit_sound is None:
            GrossCat.hit_sound = load_wav('Resources/Musics/Hit3.wav')
            GrossCat.hit_sound.set_volume(30)
        if self.die_sound is None:
            self.die_sound = load_wav('Resources/Musics/Die.wav')
            self.die_sound.set_volume(30)

    def update(self, frame_time):
        distance = self.RUN_SPEED_PPS * frame_time
        if self.Health < 0:
            self.state = self.DIE
        if self.state == self.MOVE:
            self.Frames_Move += self.FRAMES_PER_MOVE * self.ACTION_PER_TIME * frame_time
            self.frame = int(self.Frames_Move + 1) % 5  # N개의 이미지를 반복
            self.x -= distance  # 왼쪽으로 /s 의 속도로 이동
        elif self.state == self.ATTACK:
            self.Frames_Attack += self.FRAMES_PER_ATTACK * self.ACTION_PER_TIME * frame_time
            self.frame = int(self.Frames_Attack + 1) % 4  # N개의 이미지를 반복
            if self.frame > 2:
                GrossCat.hit_sound.play(1)
                self.state = self.MOVE
        elif self.state == self.DIE:
            self.frame = (self.Frames_Hurt + 1) % 2
            if self.frame > 0:
                Scene_Stage1.Cat_Units.remove(self)

    # 가로: 240, 세로: 300
    def draw(self):
        self.image.clip_draw(self.frame * 240, self.state * 300, 240, 300, self.x, self.y)

    def get_attack_range(self):
        return self.x - 30, self.y - 140, self.x + 120, self.y + 45

    def get_defense_size(self):
        return self.x + 30, self.y - 140, self.x + 120, self.y + 45
        # 크기 40, 110, 40, 80

    def draw_bb(self):
        draw_rectangle(*self.get_attack_range())
        draw_rectangle(*self.get_defense_size())

    def attack(self, e):
        self.state = self.ATTACK
        e.Health -= self.AttackPower
        print("공격중인 객체의 체력: ", e.Health)

    def walk(self):
        self.state = self.MOVE


class SexyLegsCat:
    pass


# Number 5
class CowCat:
    # 프레임 시간에 따른 객체 이동 구현
    PIXEL_PER_METER = (10.0/0.3)  # 100픽셀이 10m라고 설정
    RUN_SPEED_KMPH = 20.0  # 시간당 40km
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0) / 60.0  # 분당 m
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)
    # 프레임 시간에 따른 액션 프레임의 조절
    TIME_PER_ACTION = 0.3
    ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
    FRAMES_PER_MOVE = 4
    FRAMES_PER_ATTACK = 4

    image = None  # 클래스의 객체들이 공유하는 변수를 선언하고 None 값으로 초기화
    hit_sound = None
    die_sound = None
    MOVE, ATTACK, HURT = 2, 1, 0

    def __init__(self):
        self.x, self.y = 1200, 225 + random.randint(0, 10)  # 생성 위치
        self.Health = 500  # 체력
        self.AttackPower = 30  # 공격력
        self.frame = 0
        self.Frames_Move = 0
        self.Frames_Attack = 0
        self.Frames_Die = 0
        self.state = self.MOVE  # 기본 상태

        if CowCat.image is None:  # 만약 변수의 값이 None 이면
            CowCat.image = load_image("Resources/CatUnits/Cow_Cat.png")  # 한 번의 이미지 로딩을 통해 모든 객체들이 이미지 리소스를 공유
        if CowCat.hit_sound is None:
            CowCat.hit_sound = load_wav('Resources/Musics/Hit3.wav')
            CowCat.hit_sound.set_volume(30)
        if self.die_sound is None:
            self.die_sound = load_wav('Resources/Musics/Die.wav')
            self.die_sound.set_volume(30)
    def update(self, frame_time):
        distance = self.RUN_SPEED_PPS * frame_time
        if self.x < 0:
            Scene_Stage1.Cat_Units.remove(self)
            print("Object Removed!")
        if self.state == self.MOVE:  # 이동 상태라면
            self.Frames_Move += self.FRAMES_PER_MOVE * frame_time * self.ACTION_PER_TIME
            self.frame = int(self.Frames_Move) % 4  # N개의 이미지를 반복
            self.x -= distance
        elif self.state == self.ATTACK:  # 공격 상태라면
            self.Frames_Attack += self.FRAMES_PER_ATTACK * self.ACTION_PER_TIME * frame_time
            self.frame = int(self.Frames_Attack) % 4  # N개의 이미지를 반복
            if self.frame > 2:
                CowCat.hit_sound.play(1)
                self.state = self.MOVE
        elif self.state == self.HURT:
            self.frame = int(self.Frames_Hurt) % 2
            distance += 3
            if self.frame > 0:
                Scene_Stage1.Cat_Units.remove(self)

    def draw(self):
        self.image.clip_draw(self.frame * 150, self.state * 200, 150, 200, self.x, self.y)
        # 가로: 150, 세로: 200

    def get_attack_range(self):
        return self.x - 50, self.y - 70, self.x + 50,  self.y + 30
        # 크기 50, 70, 50, 30

    def get_defense_size(self):
        return self.x - 50, self.y - 70, self.x + 50, self.y + 30
        # 크기 50, 70, 50, 30

    def draw_bb(self):
        draw_rectangle(*self.get_attack_range())
        draw_rectangle(*self.get_defense_size())

    def attack(self, e):
        self.state = self.ATTACK
        e.Health -= self.AttackPower
        print("공격중인 객체의 체력: ", e.Health)


class GiraffeCat:
    pass


# Number 6
class BirdCat:
    # 프레임 시간에 따른 객체 이동 구현
    PIXEL_PER_METER = (10.0 / 0.3)  # 100픽셀이 10m라고 설정
    RUN_SPEED_KMPH = 20.0  # 시간당 40km
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0) / 60.0  # 분당 m
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)
    # 프레임 시간에 따른 액션 프레임의 조절
    TIME_PER_ACTION = 0.3
    ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
    FRAMES_PER_MOVE = 4
    FRAMES_PER_ATTACK = 4

    image = None  # 클래스의 객체들이 공유하는 변수를 선언하고 None 값으로 초기화
    hit_sound = None

    FLY, ATTACK, HURT = 2, 1, 0

    def __init__(self):
        self.x, self.y = 1200, 400
        self.Health = 300
        self.AttackPower = 400
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

    def update(self, frame_time):
        distance = self.RUN_SPEED_PPS * frame_time
        if self.state == self.FLY:
            self.frame = (self.frame + 1) % 4  # N개의 이미지를 반복 (이동 = 3 공격 = 4)
            self.x -= distance  # 왼쪽으로 10/s 의 속도로 이동
            self.y += random.randint(-2, 2)
        elif self.state == self.ATTACK:
            self.frame = (self.frame + 1) % 6  # N개의 이미지를 반복
            if self.frame > 4:
                self.state = self.FLY
        elif self.state == self.HURT:
            self.frame = (self.frame + 1) % 2
            if self.frame > 0:
                Scene_Stage1.Cat_Units.remove(self)

    # 가로: 180, 세로: 120
    def draw(self):
        self.image.clip_draw(self.frame * 180, self.state * 120, 180, 120, self.x, self.y)

    def get_attack_range(self):
        return self.x - 300, self.y - 50, self.x + 70, self.y + 30
        # 크기 70, 50, 70, 30

    def get_defense_size(self):
        return self.x - 23, self.y - 50, self.x + 70,  self.y + 30
        # 크기 70, 50, 70, 30

    def draw_bb(self):
        draw_rectangle(*self.get_attack_range())
        draw_rectangle(*self.get_defense_size())

    def attack(self, e):
        self.state = self.ATTACK
        e.Health -= self.AttackPower
        print("공격중인 객체의 체력: ", e.Health)

    def move(self):
        self.state = self.FLY


class UFOCat:
    # 프레임 시간에 따른 객체 이동 구현
    PIXEL_PER_METER = (10.0 / 0.3)  # 100픽셀이 10m라고 설정
    RUN_SPEED_KMPH = 20.0  # 시간당 40km
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0) / 60.0  # 분당 m
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)
    # 프레임 시간에 따른 액션 프레임의 조절
    TIME_PER_ACTION = 0.5
    ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
    FRAMES_PER_MOVE = 1
    FRAMES_PER_ATTACK = 7

    image = None  # 클래스의 객체들이 공유하는 변수를 선언하고 None 값으로 초기화
    hit_sound = None
    die_sound = None
    FLY, ATTACK, HURT = 1, 0, 1

    def __init__(self):
        self.x, self.y = 1200, 350
        self.Health = 300
        self.AttackPower = 400
        self.AttackRange = 170
        self.TimeBetweenAttacks = 1.63
        self.MovementSpeed = 10
        self.AttackAnimation = 10
        self.RechargingTime = 2.33
        self.frame = 0
        self.Frames_Move = 0
        self.Frames_Attack = 0
        self.delay = 0
        self.state = self.FLY

        if UFOCat.image is None:  # 만약 변수의 값이 None 이면
            UFOCat.image = load_image("Resources/CatUnits/UFO_Cat.png")  # 한 번의 이미지 로딩을 통해 모든 객체들이 이미지 리소스를 공유
        if UFOCat.hit_sound is None:
            UFOCat.hit_sound = load_wav('Resources/Musics/Hit3.wav')
            UFOCat.hit_sound.set_volume(30)
        if self.die_sound is None:
            self.die_sound = load_wav('Resources/Musics/Die.wav')
            self.die_sound.set_volume(30)
    def update(self, frame_time):
        distance = self.RUN_SPEED_PPS * frame_time
        if self.state == self.FLY:
            self.Frames_Move += self.FRAMES_PER_MOVE * self.ACTION_PER_TIME * frame_time
            self.frame = int(self.Frames_Move + 1) % 1  # N개의 이미지를 반복
            self.x -= distance  # 왼쪽으로 10/s 의 속도로 이동
            self.y += random.randint(-2, 2)
        elif self.state == self.ATTACK:
            self.Frames_Attack += self.FRAMES_PER_ATTACK * self.ACTION_PER_TIME * frame_time
            self.frame = int(self.Frames_Attack + 1) % 7  # N개의 이미지를 반복
            if self.frame > 3:
                Scene_Stage1.Cat_Skills.append(CatSkills.UFOCatSkill(self.x - 200, self.y - 115))
            if self.frame > 5:
                UFOCat.hit_sound.play(1)
                self.state = self.FLY
        elif self.state == self.HURT:
            self.frame = (self.frame + 1) % 2
            if self.frame > 0:
                Scene_Stage1.Cat_Units.remove(self)

    # 가로: 108, 세로: 124
    def draw(self):
        self.image.clip_draw(self.frame * 108, self.state * 124, 108, 124, self.x, self.y)

    def get_attack_range(self):
        return self.x - 300, self.y - 220, self.x - 180, self.y - 10

    def get_defense_size(self):
        return 0, 0, 0, 0  #self.x - 50, self.y - 60, self.x + 50, self.y + 20
        # 크기 70, 50, 70, 30

    def draw_bb(self):
        draw_rectangle(*self.get_attack_range())
        draw_rectangle(*self.get_defense_size())

    def attack(self, e):
        self.state = self.ATTACK

    def move(self):
        self.state = self.FLY


# Number 7
class FishCat:
    # 프레임 시간에 따른 객체 이동 구현
    PIXEL_PER_METER = (10.0 / 0.3)  # 100픽셀이 10m라고 설정
    RUN_SPEED_KMPH = 5.0  # 시간당 40km
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0) / 60.0  # 분당 m
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)
    # 프레임 시간에 따른 액션 프레임의 조절
    TIME_PER_ACTION = 0.5
    ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
    FRAMES_PER_MOVE = 8
    FRAMES_PER_ATTACK = 4

    image = None  # 클래스의 객체들이 공유하는 변수를 선언하고 None 값으로 초기화
    hit_sound = None
    die_sound = None
    MOVE, ATTACK, HURT = 2, 1, 0

    def __init__(self):
        self.x, self.y = 1200, 225 + random.randint(0, 10)  # 생성 위치
        self.Health = 1500
        self.AttackPower = 300
        self.AttackRange = 150
        self.TimeBetweenAttacks = 1.76
        self.MovementSpeed = 10
        self.AttackAnimation = 10
        self.RechargingTime = 4.53
        self.frame = 0
        self.Frames_Move = 0
        self.Frames_Attack = 0
        self.delay = 0
        self.state = self.MOVE

        if FishCat.image is None:
            FishCat.image = load_image("Resources/CatUnits/Fish_Cat.png")
        if FishCat.hit_sound is None:
            FishCat.hit_sound = load_wav('Resources/Musics/Hit3.wav')
            FishCat.hit_sound.set_volume(30)
        if self.die_sound is None:
            self.die_sound = load_wav('Resources/Musics/Die.wav')
            self.die_sound.set_volume(30)
    def update(self, frame_time):
        distance = self.RUN_SPEED_PPS * frame_time
        if self.state == self.MOVE:
            self.Frames_Move += self.FRAMES_PER_MOVE * self.ACTION_PER_TIME * frame_time
            self.frame = int(self.Frames_Move + 1) % 8  # N개의 이미지를 반복
            self.x -= distance  # 왼쪽으로 /s 의 속도로 이동
        elif self.state == self.ATTACK:
            self.Frames_Attack += self.FRAMES_PER_MOVE * self.ACTION_PER_TIME * frame_time
            self.frame = int(self.Frames_Attack + 1) % 4  # N개의 이미지를 반복
            if self.frame > 2:
                FishCat.hit_sound.play(1)
                self.state = self.MOVE
        elif self.state == self.HURT:
            self.frame = (self.frame + 1) % 2
            if self.frame > 0:
                Scene_Stage1.Cat_Units.remove(self)

    # 가로: 133, 세로: 149
    def draw(self):
        self.image.clip_draw(self.frame * 134, self.state * 149, 133, 149, self.x, self.y)

    def get_attack_range(self):
        return self.x - 68, self.y - 65, self.x + 64, self.y + 40

    def get_defense_size(self):
        return self.x - 68, self.y - 65, self.x + 64, self.y + 40
        # 크기 68, 65, 64, 40

    def draw_bb(self):
        draw_rectangle(*self.get_attack_range())
        draw_rectangle(*self.get_defense_size())

    def attack(self, e):
        self.state = self.ATTACK
        e.Health -= self.AttackPower
        print("공격중인 객체의 체력: ", e.Health)

    def move(self):
        self.state = self.MOVE


# Number 8
class LizardCat:
    # 프레임 시간에 따른 객체 이동 구현
    PIXEL_PER_METER = (10.0 / 0.3)  # 100픽셀이 10m라고 설정
    RUN_SPEED_KMPH = 5.0  # 시간당 40km
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0) / 60.0  # 분당 m
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)
    # 프레임 시간에 따른 액션 프레임의 조절
    TIME_PER_ACTION = 0.5
    ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
    FRAMES_PER_MOVE = 4
    FRAMES_PER_ATTACK = 6

    image = None  # 클래스의 객체들이 공유하는 변수를 선언하고 None 값으로 초기화
    hit_sound = None
    die_sound = None
    MOVE, ATTACK, HURT = 2, 1, 0

    def __init__(self):
        self.x, self.y = 1200, 225 + random.randint(0, 10)  # 생성 위치
        self.Health = 800
        self.AttackPower = 700
        self.AttackRange = 400
        self.TimeBetweenAttacks = 4.30
        self.MovementSpeed = 10
        self.AttackAnimation = 10
        self.RechargingTime = 316
        self.frame = 0
        self.delay = 0
        self.Frames_Move = 0
        self.Frames_Attack = 0
        self.state = self.MOVE

        if LizardCat.image is None:
            LizardCat.image = load_image("Resources/CatUnits/Lizard_Cat.png")
        if LizardCat.hit_sound is None:
            LizardCat.hit_sound = load_wav('Resources/Musics/Hit3.wav')
            LizardCat.hit_sound.set_volume(30)
        if self.die_sound is None:
            self.die_sound = load_wav('Resources/Musics/Die.wav')
            self.die_sound.set_volume(30)
    def update(self, frame_time):
        distance = self.RUN_SPEED_PPS * frame_time
        if self.state == self.MOVE:
            self.Frames_Move += self.FRAMES_PER_MOVE * self.ACTION_PER_TIME * frame_time
            self.frame = int(self.Frames_Move + 1) % 4  # N개의 이미지를 반복
            self.x -= distance  # 왼쪽으로 /s 의 속도로 이동
        elif self.state == self.ATTACK:
            self.Frames_Attack += self.FRAMES_PER_ATTACK * self.ACTION_PER_TIME * frame_time
            self.frame = int(self.Frames_Attack + 1) % 6  # N개의 이미지를 반복
            if self.frame > 4:
                LizardCat.hit_sound.play(1)
                Scene_Stage1.Cat_Skills.append(CatSkills.LizardCatSkill(self.x - 60, self.y - 10))
                self.state = self.MOVE
        elif self.state == self.HURT:
            self.frame = (self.frame + 1) % 2
            if self.frame > 0:
                Scene_Stage1.Cat_Units.remove(self)

    # 가로: 136, 세로: 109
    def draw(self):
        self.image.clip_draw(self.frame * 136, self.state * 109, 136, 109, self.x, self.y)

    def get_attack_range(self):
        return self.x - 70, self.y - 54, self.x + 68, self.y + 30

    def get_defense_size(self):
        return self.x - 30, self.y - 54, self.x + 68, self.y + 30
        # 크기 30, 54, 68, 30

    def draw_bb(self):
        draw_rectangle(*self.get_attack_range())
        draw_rectangle(*self.get_defense_size())

    def attack(self, e):
        self.state = self.ATTACK

    def move(self):
        self.state = self.MOVE


class DragonCat:
    pass


# Number 9
class TitanCat:
    # 프레임 시간에 따른 객체 이동 구현
    PIXEL_PER_METER = (10.0 / 0.3)  # 100픽셀이 10m라고 설정
    RUN_SPEED_KMPH = 5.0  # 시간당 40km
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0) / 60.0  # 분당 m
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)
    # 프레임 시간에 따른 액션 프레임의 조절
    TIME_PER_ACTION = 0.7
    ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
    FRAMES_PER_MOVE = 6
    FRAMES_PER_ATTACK = 7
    FRAMES_PER_HURT = 1

    image = None  # 클래스의 객체들이 공유하는 변수를 선언하고 None 값으로 초기화
    hit_sound = None
    die_sound = None
    MOVE, ATTACK, HURT, STOP = 3, 2, 1, 0

    def __init__(self):
        self.x, self.y = 1200, 260 + random.randint(0, 10)  # 생성 위치
        self.Health = 3000
        self.AttackPower = 700
        self.AttackRange = 150
        self.TimeBetweenAttacks = 2.23
        self.MovementSpeed = 8
        self.AttackAnimation = 18
        self.RechargingTime = 27.33
        self.frame = 0
        self.delay = 0
        self.Frames_Move = 0
        self.Frames_Attack = 0
        self.state = self.MOVE

        if TitanCat.image is None:
            TitanCat.image = load_image("Resources/CatUnits/Titan_Cat.png")
        if TitanCat.hit_sound is None:
            TitanCat.hit_sound = load_wav('Resources/Musics/Hit3.wav')
            TitanCat.hit_sound.set_volume(30)
        if self.die_sound is None:
            self.die_sound = load_wav('Resources/Musics/Die.wav')
            self.die_sound.set_volume(30)

    def update(self, frame_time):
        distance = self.RUN_SPEED_PPS * frame_time
        if self.state == self.MOVE:
            self.Frames_Move += self.FRAMES_PER_MOVE * self.ACTION_PER_TIME * frame_time
            self.frame = int(self.Frames_Move + 1) % 6  # N개의 이미지를 반복
            self.x -= distance  # 왼쪽으로 /s 의 속도로 이동
        elif self.state == self.ATTACK:
            self.Frames_Attack += self.FRAMES_PER_ATTACK * self.ACTION_PER_TIME * frame_time
            self.frame = int(self.Frames_Attack + 1) % 7  # N개의 이미지를 반복
            if self.frame > 5:
                TitanCat.hit_sound.play(1)
                self.state = self.MOVE
        elif self.state == self.HURT:
            #self.Frames_Hurt += self.FRAMES_PER_HURT * self.ACTION_PER_TIME * frame_time
            self.frame = (self.frame + 1) % 2
            if self.frame > 0:
                Scene_Stage1.Cat_Units.remove(self)
        elif self.state == self.STOP:
            self.frame = (self.frame + 1) % 1

    # 가로: 200, 세로: 215
    def draw(self):
        self.image.clip_draw(self.frame * 200, self.state * 215, 200, 215, self.x, self.y)

    def get_attack_range(self):
        return self.x - 65, self.y - 107, self.x + 40, self.y + 107

    def get_defense_size(self):
        return self.x - 55, self.y - 107, self.x + 40, self.y + 107
        # 크기 60, 107, 40, 107

    def draw_bb(self):
        draw_rectangle(*self.get_attack_range())
        draw_rectangle(*self.get_defense_size())

    def attack(self, e):
        self.state = self.ATTACK
        e.Health -= self.AttackPower
        print("공격중인 객체의 체력: ", e.Health)

    def move(self):
        self.state = self.MOVE


class MythicalTitanCat:
    pass


class JamieraCat:
    pass
