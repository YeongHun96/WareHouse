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
    RUN_SPEED_KMPH = 5.0  # 시간당 5km
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0) / 60.0
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)
    # 프레임 시간에 따른 액션 프레임의 조절
    TIME_PER_ACTION = 0.5
    TIME_FOR_DIE = 10
    ACTION_PER_TIME = 1 / TIME_PER_ACTION
    FRAMES_PER_MOVE = 3
    FRAMES_PER_ATTACK = 4

    image = None  # 클래스의 객체들이 공유하는 변수를 선언하고 None 값으로 초기화
    sound_hit = None
    sound_die = None

    ATTACK, MOVE, DIE = 1, 3, -1

    def __init__(self):
        self.x, self.y = 1200, 190 + random.randint(0, 10)  # 생성 위치
        self.Health = 300  # 체력
        self.AttackPower = 100  # 공격력
        self.state = self.MOVE  # 캐릭터의 기본 상태
        self.frame = 0
        self.Frame_For_Die = 0
        self.Frames_Move = 3
        self.Frames_Attack = 4
        self.Frames_Die = 0

        if BasicCat.image is None:  # 만약 변수의 값이 None 이면
            BasicCat.image = load_image("Resources/CatUnits/Basic_Cat.png")  # 한 번의 이미지 로딩을 통해 모든 객체들이 이미지 리소스를 공유
        if BasicCat.sound_hit is None:
            BasicCat.sound_hit = load_wav('Resources/Musics/Hit3.wav')
            BasicCat.sound_hit.set_volume(30)
        if BasicCat.sound_die is None:
            BasicCat.sound_die = load_wav('Resources/Musics/Die2.wav')
            BasicCat.sound_die.set_volume(30)

    def update(self, frame_time):
        distance = self.RUN_SPEED_PPS * frame_time
        if self.Health < 0:
            self.state = self.DIE
        if self.x < 0:
            Scene_Stage1.Cat_Units.remove(self)
            print("Object Removed!")
        if self.state == self.MOVE:
            self.Frames_Move += self.FRAMES_PER_MOVE * self.ACTION_PER_TIME * frame_time
            self.frame = int(self.Frames_Move + 1) % 3  # N개의 이미지를 반복 (이동 = 3 공격 = 4)
            self.x -= distance  # 왼쪽으로 10/s 의 속도로 이동
        elif self.state == self.ATTACK:
            self.Frames_Attack += self.FRAMES_PER_ATTACK * self.ACTION_PER_TIME * frame_time
            self.frame = int(self.Frames_Attack + 1) % 4  # N개의 이미지를 반복 (이동 = 3 공격 = 4)
            if self.frame > 2:
                BasicCat.sound_hit.play(1)
                self.state = self.MOVE
        elif self.state == self.DIE:
            self.Frames_Die += self.TIME_FOR_DIE * frame_time
            self.Frame_For_Die = int(self.Frames_Die + 1)
            self.x += 3
            if self.Frame_For_Die > 1:
                BasicCat.sound_die.play(1)
                Scene_Stage1.Cat_Units.remove(self)

    # 가로: 46, 세로: 63
    def draw(self):
        self.image.clip_draw(self.frame * 46, self.state * 63, 46, 63, self.x, self.y)

    # 충돌 체크 - 공격 범위
    def get_attack_range(self):
        return self.x - 23, self.y - 31, self.x + 23, self.y + 18

    # 충돌 체크 - 피격 범위
    def get_defense_size(self):
        return self.x - 23, self.y - 31, self.x + 23, self.y + 18

    # 충돌 범위(공격, 피격) 출력
    def draw_bb(self):
        draw_rectangle(*self.get_attack_range())
        draw_rectangle(*self.get_defense_size())

    # 충돌 발생 시 공격
    def attack(self, enemy):
        self.state = self.ATTACK
        enemy.Health -= self.AttackPower
        print("공격중인 객체의 체력: ", enemy.Health)


# Number 2
class TankCat:
    # 프레임 시간에 따른 객체 이동 구현
    PIXEL_PER_METER = (10.0 / 0.3)  # 10픽셀이 0.3m라고 설정
    RUN_SPEED_KMPH = 5.0  # 시간당 5km
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0) / 60.0
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)
    # 프레임 시간에 따른 액션 프레임의 조절
    TIME_PER_ACTION = 0.5
    ACTION_PER_TIME = 1 / TIME_PER_ACTION
    TIME_FOR_DIE = 10
    FRAMES_PER_MOVE = 3
    FRAMES_PER_ATTACK = 4

    image = None  # 클래스의 객체들이 공유하는 변수를 선언하고 None 값으로 초기화
    sound_hit = None
    sound_die = None

    MOVE, ATTACK, DIE = 2, 1, 0

    def __init__(self):
        self.x, self.y = 1200, 210 + random.randint(0, 10)  # 생성 위치
        self.Health = 5000
        self.AttackPower = 2
        self.state = self.MOVE
        self.frame = 0
        self.Frame_Die = 0
        self.Frames_Move = 0
        self.Frames_Attack = 0
        self.Frames_Die = 0

        if TankCat.image is None:
            TankCat.image = load_image("Resources/CatUnits/Tank_Cat.png")
        if TankCat.sound_hit is None:
            TankCat.sound_hit = load_wav('Resources/Musics/Hit3.wav')
            TankCat.sound_hit.set_volume(30)
        if TankCat.sound_die is None:
            TankCat.sound_die = load_wav('Resources/Musics/Die2.wav')
            TankCat.sound_die.set_volume(30)

    def update(self, frame_time):
        distance = self.RUN_SPEED_PPS * frame_time
        if self.Health < 0:
            self.state = self.DIE
        if self.x < 0:
            Scene_Stage1.Cat_Units.remove(self)
            print("Object Removed!")
        if self.state == self.MOVE:
            self.Frames_Move += self.FRAMES_PER_MOVE * self.ACTION_PER_TIME * frame_time
            self.frame = int(self.Frames_Move + 1) % 3  # N개의 이미지를 반복
            self.x -= distance  # 왼쪽으로 /s 의 속도로 이동
        elif self.state == self.ATTACK:
            self.Frames_Attack += self.FRAMES_PER_ATTACK * self.ACTION_PER_TIME * frame_time
            self.frame = int(self.Frames_Attack + 1) % 4  # N개의 이미지를 반복
            if self.frame > 2:
                TankCat.sound_hit.play(1)
                self.state = self.MOVE
        elif self.state == self.DIE:
            self.frame = 0
            self.Frames_Die += self.TIME_FOR_DIE * frame_time
            self.Frame_Die = int(self.Frames_Die + 1)
            self.x += 3
            if self.Frame_Die > 1:
                TankCat.sound_die.play(1)
                Scene_Stage1.Cat_Units.remove(self)

    # 가로: 88, 세로: 121
    def draw(self):
        self.image.clip_draw(self.frame * 88, self.state * 121, 88, 121, self.x, self.y)

    def get_attack_range(self):
        return self.x - 5, self.y - 55, self.x + 35, self.y + 25

    def get_defense_size(self):
        return self.x - 5,  self.y - 55, self.x + 35, self.y + 25

    def draw_bb(self):
        draw_rectangle(*self.get_attack_range())
        draw_rectangle(*self.get_defense_size())

    def attack(self, enemy):
        self.state = self.ATTACK
        enemy.Health -= self.AttackPower
        print("공격중인 객체의 체력: ", enemy.Health)


class WallCat:
    pass


# Number 3
class AxeCat:
    # 프레임 시간에 따른 객체 이동 구현
    PIXEL_PER_METER = (10.0 / 0.3)  # 10픽셀이 0.3m라고 설정
    RUN_SPEED_KMPH = 5.0  # 시간당 5km
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0) / 60.0
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)
    # 프레임 시간에 따른 액션 프레임의 조절
    TIME_PER_ACTION = 0.5
    TIME_FOR_DIE = 10
    ACTION_PER_TIME = 1 / TIME_PER_ACTION
    FRAMES_PER_MOVE = 3
    FRAMES_PER_ATTACK = 4

    image = None  # 클래스의 객체들이 공유하는 변수를 선언하고 None 값으로 초기화
    sound_hit = None
    sound_die = None

    MOVE, ATTACK, DIE = 1, 0, -1

    def __init__(self):
        self.x, self.y = 1200, 215 + random.randint(0, 10)  # 생성 위치
        self.Health = 800
        self.AttackPower = 300
        self.frame = 0
        self.Frame_Die = 0
        self.Frames_Move = 0
        self.Frames_Attack = 0
        self.Frames_Die = 0
        self.state = self.MOVE

        if AxeCat.image is None:  # 만약 변수의 값이 None 이면
            AxeCat.image = load_image("Resources/CatUnits/Axe_Cat.png")  # 한 번의 이미지 로딩을 통해 모든 객체들이 이미지 리소스를 공유
        if AxeCat.sound_hit is None:
            AxeCat.sound_hit = load_wav('Resources/Musics/Hit3.wav')
            AxeCat.sound_hit.set_volume(30)
        if AxeCat.sound_die is None:
            AxeCat.sound_die = load_wav('Resources/Musics/Die2.wav')
            AxeCat.sound_die.set_volume(30)

    def update(self, frame_time):
        distance = self.RUN_SPEED_PPS * frame_time
        if self.Health < 0:
            self.state = self.DIE
        if self.x < 0:
            Scene_Stage1.Cat_Units.remove(self)
            print("Object Removed!")
        if self.state == self.MOVE:
            self.Frames_Move += self.FRAMES_PER_MOVE * self.ACTION_PER_TIME * frame_time
            self.frame = int(self.Frames_Move + 1) % 3  # N개의 이미지를 반복
            self.x -= distance  # 왼쪽으로 /s 의 속도로 이동
        elif self.state == self.ATTACK:
            self.Frames_Attack += self.FRAMES_PER_ATTACK * self.ACTION_PER_TIME * frame_time
            self.frame = int(self.Frames_Attack + 1) % 4  # N개의 이미지를 반복
            if self.frame > 2:
                AxeCat.sound_hit.play(1)
                self.state = self.MOVE
        elif self.state == self.DIE:
            self.Frames_Die += self.TIME_FOR_DIE * frame_time
            self.Frame_Die = int(self.Frames_Die + 1)
            self.x += 3
            if self.Frame_Die > 1:
                AxeCat.sound_die.play(1)
                Scene_Stage1.Cat_Units.remove(self)

    # 가로: 109, 세로: 150
    def draw(self):
        self.image.clip_draw(self.frame * 109, self.state * 150, 109, 150, self.x, self.y)

    def get_attack_range(self):
        return self.x - 54, self.y - 60, self.x + 45, self.y + 20

    def get_defense_size(self):
        return self.x - 25, self.y - 60, self.x + 45, self.y + 20

    def draw_bb(self):
        draw_rectangle(*self.get_attack_range())
        draw_rectangle(*self.get_defense_size())

    def attack(self, enemy):
        self.state = self.ATTACK
        enemy.Health -= self.AttackPower
        print("공격중인 객체의 체력: ", enemy.Health)


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
    TIME_FOR_DIE = 10
    ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
    FRAMES_PER_MOVE = 5
    FRAMES_PER_ATTACK = 4

    image = None  # 클래스의 객체들이 공유하는 변수를 선언하고 None 값으로 초기화
    sound_hit = None
    sound_die = None

    MOVE, ATTACK, DIE = 2, 1, 0

    def __init__(self):
        self.x, self.y = 1100, 300 + random.randint(0, 15)  # 생성 위치
        self.Health = 800
        self.AttackPower = 2000
        self.frame = 0
        self.Frame_Die = 0
        self.Frames_Move = 0
        self.Frames_Attack = 0
        self.Frames_Die = 0
        self.state = self.MOVE

        if GrossCat.image is None:  # 만약 변수의 값이 None 이면
            GrossCat.image = load_image("Resources/CatUnits/Gross_Cat.png")  # 한 번의 이미지 로딩을 통해 모든 객체들이 이미지 리소스를 공유
        if GrossCat.sound_hit is None:
            GrossCat.sound_hit = load_wav('Resources/Musics/Hit3.wav')
            GrossCat.sound_hit.set_volume(30)
        if GrossCat.sound_die is None:
            GrossCat.sound_die = load_wav('Resources/Musics/Die2.wav')
            GrossCat.sound_die.set_volume(30)

    def update(self, frame_time):
        distance = self.RUN_SPEED_PPS * frame_time
        if self.Health < 0:
            self.state = self.DIE
        if self.x < 0:
            Scene_Stage1.Cat_Units.remove(self)
            print("Object Removed!")
        if self.state == self.MOVE:
            self.Frames_Move += self.FRAMES_PER_MOVE * self.ACTION_PER_TIME * frame_time
            self.frame = int(self.Frames_Move + 1) % 5  # N개의 이미지를 반복
            self.x -= distance  # 왼쪽으로 /s 의 속도로 이동
        elif self.state == self.ATTACK:
            self.Frames_Attack += self.FRAMES_PER_ATTACK * self.ACTION_PER_TIME * frame_time
            self.frame = int(self.Frames_Attack + 1) % 4  # N개의 이미지를 반복
            if self.frame > 2:
                GrossCat.sound_hit.play(1)
                self.state = self.MOVE
        elif self.state == self.DIE:
            self.frame = 0
            self.Frames_Die += self.TIME_FOR_DIE * frame_time
            self.Frame_Die = int(self.Frames_Die + 1)
            self.x += 3
            if self.Frame_Die > 1:
                GrossCat.sound_die.play(1)
                Scene_Stage1.Cat_Units.remove(self)

    # 가로: 240, 세로: 300
    def draw(self):
        self.image.clip_draw(self.frame * 240, self.state * 300, 240, 300, self.x, self.y)

    def get_attack_range(self):
        return self.x - 30, self.y - 140, self.x + 120, self.y + 45

    def get_defense_size(self):
        return self.x + 30, self.y - 140, self.x + 120, self.y + 45

    def draw_bb(self):
        draw_rectangle(*self.get_attack_range())
        draw_rectangle(*self.get_defense_size())

    def attack(self, enemy):
        self.state = self.ATTACK
        enemy.Health -= self.AttackPower
        print("공격중인 객체의 체력: ", enemy.Health)


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
    TIME_FOR_DIE = 10
    ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
    FRAMES_PER_MOVE = 4
    FRAMES_PER_ATTACK = 4

    image = None  # 클래스의 객체들이 공유하는 변수를 선언하고 None 값으로 초기화
    sound_hit = None
    sound_die = None

    MOVE, ATTACK, DIE = 2, 1, 0

    def __init__(self):
        self.x, self.y = 1200, 225 + random.randint(0, 10)  # 생성 위치
        self.Health = 3000  # 체력
        self.AttackPower = 200  # 공격력
        self.frame = 0
        self.Frame_Die = 0
        self.Frames_Move = 0
        self.Frames_Attack = 0
        self.Frames_Die = 0
        self.state = self.MOVE  # 기본 상태

        if CowCat.image is None:  # 만약 변수의 값이 None 이면
            CowCat.image = load_image("Resources/CatUnits/Cow_Cat.png")  # 한 번의 이미지 로딩을 통해 모든 객체들이 이미지 리소스를 공유
        if CowCat.sound_hit is None:
            CowCat.sound_hit = load_wav('Resources/Musics/Hit3.wav')
            CowCat.sound_hit.set_volume(30)
        if CowCat.sound_die is None:
            CowCat.sound_die = load_wav('Resources/Musics/Die2.wav')
            CowCat.sound_die.set_volume(30)

    def update(self, frame_time):
        distance = self.RUN_SPEED_PPS * frame_time
        if self.Health < 0:
            self.state = self.DIE
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
            if self.frame < 2:
                CowCat.sound_hit.play(1)
                self.state = self.MOVE
        elif self.state == self.DIE:
            self.frame = 0
            self.Frames_Die += self.TIME_FOR_DIE * frame_time
            self.Frame_Die = int(self.Frames_Die + 1)
            self.x += 3
            if self.Frame_Die > 1:
                CowCat.sound_die.play(1)
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

    def attack(self, enemy):
        self.state = self.ATTACK
        enemy.Health -= self.AttackPower
        print("공격중인 객체의 체력: ", enemy.Health)


class GiraffeCat:
    pass


# Number 6
class BirdCat:
    pass


class UFOCat:
    # 프레임 시간에 따른 객체 이동 구현
    PIXEL_PER_METER = (10.0 / 0.3)  # 10픽셀이 0.3m라고 설정
    RUN_SPEED_KMPH = 20.0  # 시간당 20km
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0) / 60.0  # 분당 m
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)
    # 프레임 시간에 따른 액션 프레임의 조절
    TIME_PER_ACTION = 0.5
    TIME_FOR_DIE = 10
    ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
    FRAMES_PER_MOVE = 1
    FRAMES_PER_ATTACK = 7

    image = None  # 클래스의 객체들이 공유하는 변수를 선언하고 None 값으로 초기화
    sound_hit = None
    sound_die = None

    MOVE, ATTACK, DIE = 1, 0, 1

    def __init__(self):
        self.x, self.y = 1200, 350
        self.Health = 300
        self.frame = 0
        self.Frame_Die = 0
        self.Frames_Move = 0
        self.Frames_Attack = 0
        self.Frames_Die = 0
        self.state = self.MOVE

        if UFOCat.image is None:  # 만약 변수의 값이 None 이면
            UFOCat.image = load_image("Resources/CatUnits/UFO_Cat.png")  # 한 번의 이미지 로딩을 통해 모든 객체들이 이미지 리소스를 공유
        if UFOCat.sound_hit is None:
            UFOCat.sound_hit = load_wav('Resources/Musics/Hit3.wav')
            UFOCat.sound_hit.set_volume(30)
        if UFOCat.sound_die is None:
            UFOCat.sound_die = load_wav('Resources/Musics/Die2.wav')
            UFOCat.sound_die.set_volume(30)

    def update(self, frame_time):
        distance = self.RUN_SPEED_PPS * frame_time
        for Enemy in Scene_Stage1.Enemy_Units:
            if Enemy.x > self.x:
                #UFOCat.sound_die.play(1)
                Scene_Stage1.Cat_Units.remove(self)
        if self.Health < 0:
            self.state = self.DIE
        if self.x < 0:
            print("Object Removed!")
            Scene_Stage1.Cat_Units.remove(self)
        if self.state == self.MOVE:
            self.Frames_Move += self.FRAMES_PER_MOVE * self.ACTION_PER_TIME * frame_time
            self.frame = int(self.Frames_Move + 1) % 1  # N개의 이미지를 반복
            self.x -= distance
            self.y += random.randint(-1, 1)
        elif self.state == self.ATTACK:
            self.Frames_Attack += self.FRAMES_PER_ATTACK * self.ACTION_PER_TIME * frame_time
            self.frame = int(self.Frames_Attack + 1) % 7  # N개의 이미지를 반복
            if self.frame > 3:
                Scene_Stage1.Cat_Skills.append(CatSkills.UFOCatSkill(self.x - 200, self.y - 115))
            if self.frame < 5:
                UFOCat.sound_hit.play(1)
                self.state = self.MOVE
        elif self.state == self.DIE:
            self.frame = 0
            self.Frames_Die += 2 * frame_time
            self.Frame_Die = int(self.Frames_Die + 1)
            if self.Frame_Die > 1:
                Scene_Stage1.Cat_Units.remove(self)

    # 가로: 108, 세로: 124
    def draw(self):
        self.image.clip_draw(self.frame * 108, self.state * 124, 108, 124, self.x, self.y)

    def get_attack_range(self):
        return self.x - 300, self.y - 220, self.x - 180, self.y - 10

    def get_defense_size(self):
        return self.x + 70, self.y + 50, self.x - 70, self.y - 200
        # 크기 70, 50, 70, 30

    def draw_bb(self):
        draw_rectangle(*self.get_attack_range())
        draw_rectangle(*self.get_defense_size())

    def attack(self, enemy):
        self.state = self.ATTACK
        # CatSkill 클래스의 UFOCatSkill 객체에서 역할 수행


# Number 7
class FishCat:
    # 프레임 시간에 따른 객체 이동 구현
    PIXEL_PER_METER = (10.0 / 0.3)  # 10픽셀이 0.3m라고 설정
    RUN_SPEED_KMPH = 5.0  # 시간당 5km
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0) / 60.0  # 분당 m
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)
    # 프레임 시간에 따른 액션 프레임의 조절
    TIME_PER_ACTION = 0.5
    TIME_FOR_DIE = 10
    ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
    FRAMES_PER_MOVE = 8
    FRAMES_PER_ATTACK = 4

    image = None  # 클래스의 객체들이 공유하는 변수를 선언하고 None 값으로 초기화
    sound_hit = None
    sound_die = None

    MOVE, ATTACK, DIE = 2, 1, 0

    def __init__(self):
        self.x, self.y = 1200, 225 + random.randint(0, 10)  # 생성 위치
        self.Health = 4000
        self.AttackPower = 1000
        self.frame = 0
        self.Frame_Die = 0
        self.Frames_Move = 0
        self.Frames_Attack = 0
        self.Frames_Die =0
        self.state = self.MOVE

        if FishCat.image is None:
            FishCat.image = load_image("Resources/CatUnits/Fish_Cat.png")
        if FishCat.sound_hit is None:
            FishCat.sound_hit = load_wav('Resources/Musics/Hit3.wav')
            FishCat.sound_hit.set_volume(30)
        if FishCat.sound_die is None:
            FishCat.sound_die = load_wav('Resources/Musics/Die2.wav')
            FishCat.sound_die.set_volume(30)

    def update(self, frame_time):
        distance = self.RUN_SPEED_PPS * frame_time
        if self.Health < 0:
            self.state = self.DIE
        if self.x < 0:
            Scene_Stage1.Cat_Units.remove(self)
            print("Object Removed!")
        if self.state == self.MOVE:
            self.Frames_Move += self.FRAMES_PER_MOVE * self.ACTION_PER_TIME * frame_time
            self.frame = int(self.Frames_Move + 1) % 8  # N개의 이미지를 반복
            self.x -= distance  # 왼쪽으로 /s 의 속도로 이동
        elif self.state == self.ATTACK:
            self.Frames_Attack += self.FRAMES_PER_MOVE * self.ACTION_PER_TIME * frame_time
            self.frame = int(self.Frames_Attack + 1) % 4  # N개의 이미지를 반복
            if self.frame > 2:
                FishCat.sound_hit.play(1)
                self.state = self.MOVE
        elif self.state == self.DIE:
            self.frame = 0
            self.Frames_Die += self.TIME_FOR_DIE * frame_time
            self.Frame_Die = int(self.Frames_Die + 1)
            self.x += 3
            if self.Frame_Die > 1:
                FishCat.sound_die.play(1)
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

    def attack(self, enemy):
        self.state = self.ATTACK
        enemy.Health -= self.AttackPower
        print("공격중인 객체의 체력: ", enemy.Health)


# Number 8
class LizardCat:
    # 프레임 시간에 따른 객체 이동 구현
    PIXEL_PER_METER = (10.0 / 0.3)  # 10픽셀이 0.3m라고 설정
    RUN_SPEED_KMPH = 5.0  # 시간당 5km
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0) / 60.0  # 분당 m
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)
    # 프레임 시간에 따른 액션 프레임의 조절
    TIME_PER_ACTION = 0.5
    TIME_FOR_DIE = 10
    ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
    FRAMES_PER_MOVE = 4
    FRAMES_PER_ATTACK = 6

    image = None  # 클래스의 객체들이 공유하는 변수를 선언하고 None 값으로 초기화
    sound_hit = None
    sound_die = None

    MOVE, ATTACK, DIE = 2, 1, 0

    def __init__(self):
        self.x, self.y = 1200, 225 + random.randint(0, 10)  # 생성 위치
        self.Health = 1000
        self.frame = 0
        self.Frame_Die = 0
        self.Frames_Move = 0
        self.Frames_Attack = 0
        self.Frames_Die = 0
        self.state = self.MOVE

        if LizardCat.image is None:
            LizardCat.image = load_image("Resources/CatUnits/Lizard_Cat.png")
        if LizardCat.sound_hit is None:
            LizardCat.sound_hit = load_wav('Resources/Musics/Hit3.wav')
            LizardCat.sound_hit.set_volume(30)
        if LizardCat.sound_die is None:
            LizardCat.sound_die = load_wav('Resources/Musics/Die2.wav')
            LizardCat.sound_die.set_volume(30)

    def update(self, frame_time):
        distance = self.RUN_SPEED_PPS * frame_time
        if self.Health < 0:
            self.state = self.DIE
        if self.x < 0:
            Scene_Stage1.Cat_Units.remove(self)
            print("Object Removed!")
        if self.state == self.MOVE:
            self.Frames_Move += self.FRAMES_PER_MOVE * self.ACTION_PER_TIME * frame_time
            self.frame = int(self.Frames_Move + 1) % 4  # N개의 이미지를 반복
            self.x -= distance  # 왼쪽으로 /s 의 속도로 이동
        elif self.state == self.ATTACK:
            self.Frames_Attack += self.FRAMES_PER_ATTACK * self.ACTION_PER_TIME * frame_time
            self.frame = int(self.Frames_Attack + 1) % 6  # N개의 이미지를 반복
            if self.frame > 4:
                LizardCat.sound_hit.play(1)
                Scene_Stage1.Cat_Skills.append(CatSkills.LizardCatSkill(self.x - 60, self.y - 20))
                self.state = self.MOVE
        elif self.state == self.DIE:
            self.frame = 0
            self.Frames_Die += self.TIME_FOR_DIE * frame_time
            self.Frame_Die = int(self.Frames_Die + 1)
            self.x += 3
            if self.Frame_Die > 1:
                LizardCat.sound_die.play(1)
                Scene_Stage1.Cat_Units.remove(self)

    # 가로: 136, 세로: 109
    def draw(self):
        self.image.clip_draw(self.frame * 136, self.state * 109, 136, 109, self.x, self.y)

    def get_attack_range(self):
        return self.x - 100, self.y - 54, self.x + 68, self.y + 30

    def get_defense_size(self):
        return self.x - 30, self.y - 54, self.x + 68, self.y + 30
        # 크기 30, 54, 68, 30

    def draw_bb(self):
        draw_rectangle(*self.get_attack_range())
        draw_rectangle(*self.get_defense_size())

    def attack(self, enemy):
        self.state = self.ATTACK


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
    TIME_FOR_DIE = 10
    ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
    FRAMES_PER_MOVE = 6
    FRAMES_PER_ATTACK = 7
    FRAMES_PER_DIE = 1

    image = None  # 클래스의 객체들이 공유하는 변수를 선언하고 None 값으로 초기화
    sound_hit = None
    sound_die = None

    MOVE, ATTACK, DIE, STOP = 3, 2, 1, 0

    def __init__(self):
        self.x, self.y = 1200, 260 + random.randint(0, 10)  # 생성 위치
        self.Health = 10000
        self.AttackPower = 1000
        self.frame = 0
        self.Frame_Die = 0
        self.Frames_Move = 0
        self.Frames_Attack = 0
        self.Frames_Die = 0
        self.state = self.MOVE

        if TitanCat.image is None:
            TitanCat.image = load_image("Resources/CatUnits/Titan_Cat.png")
        if TitanCat.sound_hit is None:
            TitanCat.sound_hit = load_wav('Resources/Musics/Hit3.wav')
            TitanCat.sound_hit.set_volume(30)
        if TitanCat.sound_die is None:
            TitanCat.sound_die = load_wav('Resources/Musics/Die2.wav')
            TitanCat.sound_die.set_volume(30)

    def update(self, frame_time):
        distance = self.RUN_SPEED_PPS * frame_time
        if self.Health < 0:
            self.state = self.DIE
        if self.x < 0:
            Scene_Stage1.Cat_Units.remove(self)
            print("Object Removed!")
        if self.state == self.MOVE:
            self.Frames_Move += self.FRAMES_PER_MOVE * self.ACTION_PER_TIME * frame_time
            self.frame = int(self.Frames_Move + 1) % 6  # N개의 이미지를 반복
            self.x -= distance  # 왼쪽으로 /s 의 속도로 이동
        elif self.state == self.ATTACK:
            self.Frames_Attack += self.FRAMES_PER_ATTACK * self.ACTION_PER_TIME * frame_time
            self.frame = int(self.Frames_Attack + 1) % 7  # N개의 이미지를 반복
            if self.frame > 5:
                TitanCat.sound_hit.play(1)
                self.state = self.MOVE
        elif self.state == self.DIE:
            self.frame = 0
            self.Frames_Die += self.TIME_FOR_DIE * frame_time
            self.Frame_Die = int(self.Frames_Die + 1)
            self.x += 3
            if self.Frame_Die > 1:
                TitanCat.sound_die.play(1)
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


class MythicalTitanCat:
    pass


class JamieraCat:
    pass
