# Python Module : 파이썬의 정의와 문장을 담고 있는 파일
#                그 자체로도 실행 가능하며, 다른 모듈에서 import해서 사용할 수도 있음.
#                import되면 그 자체가 하나의 객체가 됨.
#                Module의 사용 : import 모듈이름
import random
from pico2d import *
import Scene_Stage1
import EnemySkills
import BackGround

class SkeleDog:
    # 프레임 시간에 따른 객체 이동 구현
    PIXEL_PER_METER = (10.0 / 0.3)  # 10픽셀이 0.3m라고 설정
    RUN_SPEED_KMPH = 15.0  # 시간당 15km
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0) / 60.0  # 분당 m
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)
    # 프레임 시간에 따른 액션 프레임의 조절
    TIME_PER_ACTION = 0.3
    TIME_FOR_DIE = 10
    ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
    FRAMES_PER_MOVE = 5
    FRAMES_PER_ATTACK = 1

    image = None  # 클래스의 객체들이 공유하는 변수를 선언하고 None 값으로 초기화
    sound_hit = None
    sound_die = None

    ATTACK, MOVE, HURT, DIE = 4, 3, 1, 0  # 상태 정의

    def __init__(self):  # 객체의 초기값 설정
        self.x, self.y = 80, 190 + random.randint(0, 15)  # 생성위치
        self.Health = 400  # 체력
        self.AttackPower = 50  # 공격력
        self.state = self.MOVE  # 초기상태
        self.frame = 0
        self.Frame = 0
        self.Frame_Die = 0
        self.Frames_Move = 0
        self.Frames_Attack = 0
        self.Frames_Die = 0

        if SkeleDog.image is None:  # 만약 변수의 값이 None 이면
            SkeleDog.image = load_image("Resources/EnemyUnits/Skeledog.png")  # 한 번의 이미지 로딩을 통해 모든 객체들이 이미지 리소스를 공유
        if SkeleDog.sound_hit is None:
            SkeleDog.sound_hit = load_wav('Resources/Musics/Hit3.wav')
            SkeleDog.sound_hit.set_volume(30)
        if SkeleDog.sound_die is None:
            SkeleDog.sound_die = load_wav('Resources/Musics/Die2.wav')
            SkeleDog.sound_die.set_volume(30)

    def update(self, frame_time):
        distance = self.RUN_SPEED_PPS * frame_time
        if self.Health < 0:
            self.state = self.DIE
        if self.x > 1200:
            print("Object Removed!")
            Scene_Stage1.Enemy_Units.remove(self)
        if self.state == self.MOVE:
            self.Frames_Move += self.FRAMES_PER_MOVE * self.ACTION_PER_TIME * frame_time
            self.frame = int(self.Frames_Move + 1) % 5  # N개의 이미지를 반복
            self.x += distance  # 오른쪽으로 10/s 의 속도로 이동
        elif self.state == self.ATTACK:
            self.Frames_Attack += self.FRAMES_PER_ATTACK * self.ACTION_PER_TIME * frame_time * 5
            self.frame = int(self.Frames_Attack + 1) % 6
            if self.frame > 4:
                SkeleDog.sound_hit.play(1)
                self.state = self.MOVE
        elif self.state == self.HURT:
            self.frame = (self.frame + 1) % 1
        elif self.state == self.DIE:
            self.Frame += self.FRAMES_PER_ATTACK * self.ACTION_PER_TIME * frame_time * 5
            self.frame = int(self.Frame + 1) % 7
            self.Frames_Die += self.TIME_FOR_DIE * frame_time
            self.Frame_Die = int(self.Frames_Die + 1)
            if self.Frame_Die > 1 and self.Frame > 5:
                SkeleDog.sound_die.play(1)
                Scene_Stage1.Enemy_Units.remove(self)

    def draw(self):
        self.image.clip_draw(self.frame * 83, self.state * 77, 83, 77, self.x, self.y)
        # Width = 83, Height = 77

    def get_attack_range(self):
        return self.x - 35, self.y - 35, self.x + 35, self.y + 30

    def get_defense_size(self):
        return self.x - 35, self.y - 35, self.x + 35, self.y + 30

    def draw_bb(self):
        draw_rectangle(*self.get_attack_range())
        draw_rectangle(*self.get_defense_size())

    def attack(self, enemy):
        self.state = self.ATTACK
        enemy.Health -= self.AttackPower
        print("공격중인 객체의 체력: ", enemy.Health)


class MummyDog:
    # 프레임 시간에 따른 객체 이동 구현
    PIXEL_PER_METER = (10.0 / 0.3)  # 100픽셀이 10m라고 설정
    RUN_SPEED_KMPH = 20.0  # 시간당 40km
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0) / 60.0  # 분당 m
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)
    # 프레임 시간에 따른 액션 프레임의 조절
    TIME_PER_ACTION = 0.5
    TIME_FOR_DIE = 10
    ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
    FRAMES_PER_MOVE = 5
    FRAMES_PER_ATTACK = 1

    image = None  # 클래스의 객체들이 공유하는 변수를 선언하고 None 값으로 초기화
    sound_hit = None
    sound_die = None

    ATTACK, MOVE, HURT, DIE = 4, 3, 1, 0  # 상태 정의

    def __init__(self):  # 객체의 초기값 설정
        self.x, self.y = 80, 190 + random.randint(0, 15)  # 생성위치
        self.Health = 500  # 체력
        self.AttackPower = 50  # 공격력
        self.state = self.MOVE  # 초기상태
        self.frame = 0
        self.Frame = 0
        self.Frame_Die = 0
        self.Frames_Move = 0
        self.Frames_Attack = 0
        self.Frames_Die = 0

        if MummyDog.image is None:  # 만약 변수의 값이 None 이면
            MummyDog.image = load_image("Resources/EnemyUnits/Mummydog.png")  # 한 번의 이미지 로딩을 통해 모든 객체들이 이미지 리소스를 공유
        if MummyDog.sound_hit is None:
            MummyDog.sound_hit = load_wav('Resources/Musics/Hit3.wav')
            MummyDog.sound_hit.set_volume(30)
        if MummyDog.sound_die is None:
            MummyDog.sound_die = load_wav('Resources/Musics/Die2.wav')
            MummyDog.sound_die.set_volume(30)

    def update(self, frame_time):
        distance = self.RUN_SPEED_PPS * frame_time
        if self.Health < 0:
            self.state = self.DIE
        if self.x > 1200:
            print("Object Removed!")
            Scene_Stage1.Enemy_Units.remove(self)
        if self.state == self.MOVE:
            self.Frames_Move += self.FRAMES_PER_MOVE * self.ACTION_PER_TIME * frame_time
            self.frame = int(self.Frames_Move + 1) % 5  # N개의 이미지를 반복
            self.x += distance  # 오른쪽으로 10/s 의 속도로 이동
        elif self.state == self.ATTACK:
            self.Frames_Attack += self.FRAMES_PER_ATTACK * self.ACTION_PER_TIME * frame_time * 5
            self.frame = int(self.Frames_Attack + 1) % 6
            if self.frame > 4:
                MummyDog.sound_hit.play(1)
                self.state = self.MOVE
        elif self.state == self.HURT:
            self.frame = int(self.frame + 1) % 1
        elif self.state == self.DIE:
            self.Frame += self.FRAMES_PER_ATTACK * self.ACTION_PER_TIME * frame_time * 5
            self.frame = int(self.Frame + 1) % 7
            self.Frames_Die += self.TIME_FOR_DIE * frame_time
            self.Frame_Die = int(self.Frames_Die + 1)
            if self.Frame_Die > 1 and self.Frame > 5:
                MummyDog.sound_die.play(1)
                Scene_Stage1.Enemy_Units.remove(self)

    def draw(self):
        self.image.clip_draw(self.frame * 82, self.state * 79, 82, 79, self.x, self.y)
        # Width = 83, Height = 77

    def get_attack_range(self):
        return self.x - 35, self.y - 35, self.x + 35, self.y + 35

    def get_defense_size(self):
        return self.x - 35, self.y - 35, self.x + 35,  self.y + 35

    def draw_bb(self):
        draw_rectangle(*self.get_attack_range())
        draw_rectangle(*self.get_defense_size())

    def attack(self, enemy):
        self.state = self.ATTACK
        enemy.Health -= self.AttackPower
        print("공격중인 객체의 체력: ", enemy.Health)


class SkeletonSoldier:  # 스켈레톤 병사 클래스
    # 프레임 시간에 따른 객체 이동 구현
    PIXEL_PER_METER = (10.0 / 0.3)  # 100픽셀이 10m라고 설정
    RUN_SPEED_KMPH = 3.0  # 시간당 40km
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0) / 60.0  # 분당 m
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)
    # 프레임 시간에 따른 액션 프레임의 조절
    TIME_PER_ACTION = 0.5
    TIME_FOR_DIE = 10
    ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
    FRAMES_PER_MOVE = 4
    FRAMES_PER_ATTACK = 4

    image = None  # 클래스의 객체들이 공유하는 변수를 선언하고 None 값으로 초기화
    sound_hit = None
    sound_die = None

    STOP, MOVE, HURT, ATTACK, DIE = 4, 3, 2, 1, 0  # 상태 정의

    def __init__(self):  # 객체의 초기값 설정
        self.x, self.y = 80, 230 + random.randint(0, 15)  # 생성위치
        self.Health = 1000  # 체력
        self.AttackPower = 100  # 공격력
        self.state = self.MOVE  # 초기상태
        self.frame = 0
        self.Frame = 0
        self.Frame_Die = 0
        self.Frames_Move = 0
        self.Frames_Attack = 0
        self.Frames_Die = 0

        if SkeletonSoldier.image is None:  # 만약 변수의 값이 None 이면
            SkeletonSoldier.image = load_image("Resources/EnemyUnits/SkeletonSoldier.png")
            # 한 번의 이미지 로딩을 통해 모든 객체들이 이미지 리소스를 공유
        if SkeletonSoldier.sound_hit is None:
            SkeletonSoldier.sound_hit = load_wav('Resources/Musics/Hit3.wav')
            SkeletonSoldier.sound_hit.set_volume(30)
        if SkeletonSoldier.sound_die is None:
            SkeletonSoldier.sound_die = load_wav('Resources/Musics/Die2.wav')
            SkeletonSoldier.sound_die.set_volume(30)

    def update(self, frame_time):
        distance = self.RUN_SPEED_PPS * frame_time
        if self.Health < 0:
            self.state = self.DIE
        if self.x > 1200:
            print("Object Removed!")
            Scene_Stage1.Enemy_Units.remove(self)
        if self.state == self.MOVE:
            self.Frames_Move += self.FRAMES_PER_MOVE * self.ACTION_PER_TIME * frame_time
            self.frame = int(self.Frames_Move + 1) % 4  # N개의 이미지를 반복
            self.x += distance  # 오른쪽으로 10/s 의 속도로 이동
        elif self.state == self.STOP:
            self.frame = (self.frame + 1) % 4  # N개의 이미지를 반복
        elif self.state == self.HURT:
            self.x -= 3
            self.frame = (self.frame + 1) % 1
        elif self.state == self.ATTACK:
            self.Frames_Attack += self.FRAMES_PER_ATTACK * self.ACTION_PER_TIME * frame_time
            self.frame = int(self.Frames_Attack + 1) % 4
            if self.frame > 2:
                SkeletonSoldier.sound_hit.play(1)
                self.state = self.MOVE
        elif self.state == self.DIE:
            self.Frame += self.FRAMES_PER_ATTACK * self.ACTION_PER_TIME * frame_time
            self.frame = int(self.Frame + 1) % 6
            self.Frames_Die += self.TIME_FOR_DIE * frame_time
            self.Frame_Die = int(self.Frames_Die + 1)
            if self.Frame_Die > 1 and self.Frame > 4:
                SkeletonSoldier.sound_die.play(1)
                Scene_Stage1.Enemy_Units.remove(self)

    def draw(self):
        self.image.clip_draw(self.frame * 150, self.state * 137, 140, 137, self.x, self.y)
        # Width = 150, Height = 137

    def get_attack_range(self):
        return self.x - 65, self.y - 70, self.x + 30, self.y + 25

    def get_defense_size(self):
        return self.x - 65, self.y - 70, self.x + 5, self.y + 25

    def draw_bb(self):
        draw_rectangle(*self.get_attack_range())
        draw_rectangle(*self.get_defense_size())

    def attack(self, enemy):
        self.state = self.ATTACK
        enemy.Health -= self.AttackPower
        print("공격중인 객체의 체력: ", enemy.Health)


class OfficerSkeleton:
    # 프레임 시간에 따른 객체 이동 구현
    PIXEL_PER_METER = (10.0 / 0.3)  # 100픽셀이 10m라고 설정
    RUN_SPEED_KMPH = 3.0  # 시간당 40km
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0) / 60.0  # 분당 m
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)
    # 프레임 시간에 따른 액션 프레임의 조절
    TIME_PER_ACTION = 1.0
    TIME_FOR_DIE = 10
    ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
    FRAMES_PER_MOVE = 4
    FRAMES_PER_ATTACK = 4

    image = None  # 클래스의 객체들이 공유하는 변수를 선언하고 None 값으로 초기화
    sound_hit = None
    sound_die = None

    STOP, MOVE, HURT, ATTACK, DIE = 4, 3, 2, 1, 0  # 상태 정의

    def __init__(self):  # 객체의 초기값 설정
        self.x, self.y = 80, 230 + random.randint(0, 15)  # 생성위치
        self.Health = 1500  # 체력
        self.AttackPower = 200  # 공격력
        self.state = self.MOVE  # 초기상태
        self.frame = 0
        self.Frame = 0
        self.Frame_Die = 0
        self.Frames_Move = 0
        self.Frames_Attack = 0
        self.Frames_Die = 0

        if OfficerSkeleton.image is None:  # 만약 변수의 값이 None 이면
            OfficerSkeleton.image = load_image("Resources/EnemyUnits/OfficerSkeleton3.png")  # 한 번의 이미지 로딩을 통해 모든 객체들이 이미지 리소스를 공유
        if OfficerSkeleton.sound_hit is None:
            OfficerSkeleton.sound_hit = load_wav('Resources/Musics/Hit3.wav')
            OfficerSkeleton.sound_hit.set_volume(30)
        if OfficerSkeleton.sound_die is None:
            OfficerSkeleton.sound_die = load_wav('Resources/Musics/Die2.wav')
            OfficerSkeleton.sound_die.set_volume(30)

    def update(self, frame_time):
        distance = self.RUN_SPEED_PPS * frame_time
        if self.Health < 0:
            self.state = self.DIE
        if self.x > 1200:
            print("Object Removed!")
            Scene_Stage1.Enemy_Units.remove(self)
        if self.state == self.MOVE:
            self.Frames_Move += self.FRAMES_PER_MOVE * self.ACTION_PER_TIME * frame_time
            self.frame = int(self.Frames_Move + 1) % 4  # N개의 이미지를 반복
            self.x += distance  # 오른쪽으로 10/s 의 속도로 이동
        elif self.state == self.STOP:
            self.frame = (self.frame + 1) % 4  # N개의 이미지를 반복
        elif self.state == self.HURT:
            self.x -= 3
            self.frame = (self.frame + 1) % 1
        elif self.state == self.ATTACK:
            self.Frames_Attack += self.FRAMES_PER_ATTACK * self.ACTION_PER_TIME * frame_time
            self.frame = int(self.Frames_Attack + 1) % 4
            if self.frame > 2:
                OfficerSkeleton.sound_hit.play(1)
                self.state = self.MOVE
        elif self.state == self.DIE:
            self.Frame += self.FRAMES_PER_ATTACK * self.ACTION_PER_TIME * frame_time
            self.frame = int(self.Frame + 1) % 6
            self.Frames_Die += self.TIME_FOR_DIE * frame_time
            self.Frame_Die = int(self.Frames_Die + 1)
            if self.Frame_Die > 1 and self.Frame > 4:
                OfficerSkeleton.sound_die.play(1)
                Scene_Stage1.Enemy_Units.remove(self)

    def draw(self):
        self.image.clip_draw(self.frame * 150, self.state * 156, 150, 156, self.x, self.y)
        # Width = 150, Height = 156

    def get_attack_range(self):
        return self.x - 65, self.y - 80, self.x + 30, self.y + 15

    def get_defense_size(self):
        return self.x - 65, self.y - 80, self.x + 5, self.y + 15

    def draw_bb(self):
        draw_rectangle(*self.get_attack_range())
        draw_rectangle(*self.get_defense_size())

    def attack(self, e):
        self.state = self.ATTACK
        e.Health -= self.AttackPower
        print("공격중인 객체의 체력: ", e.Health)

    def walk(self):
        self.state = self.MOVE


class CommanderSkeleton:
    # 프레임 시간에 따른 객체 이동 구현
    PIXEL_PER_METER = (10.0 / 0.3)  # 100픽셀이 10m라고 설정
    RUN_SPEED_KMPH = 5.0  # 시간당 40km
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0) / 60.0  # 분당 m
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)
    # 프레임 시간에 따른 액션 프레임의 조절
    TIME_PER_ACTION = 0.5
    TIME_FOR_DIE = 3
    ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
    FRAMES_PER_MOVE = 4
    FRAMES_PER_ATTACK = 8

    image = None  # 클래스의 객체들이 공유하는 변수를 선언하고 None 값으로 초기화
    sound_hit = None
    sound_die = None

    STOP, MOVE, HURT, ATTACK, DIE = 4, 3, 2, 1, 0  # 상태 정의

    def __init__(self):  # 객체의 초기값 설정
        self.x, self.y = 80, 230 + random.randint(0, 15)  # 생성위치
        self.Health = 3000  # 체력
        self.AttackPower = 1  # 공격력 ( 범위형 지속공격 )
        self.state = self.MOVE  # 초기상태
        self.frame = 0
        self.Frame = 0
        self.Frame_Die = 0
        self.Frames_Move = 0
        self.Frames_Attack = 0
        self.Frames_Die = 0

        if CommanderSkeleton.image is None:  # 만약 변수의 값이 None 이면
            CommanderSkeleton.image = load_image("Resources/EnemyUnits/CommanderSkeleton.png")  # 한 번의 이미지 로딩을 통해 모든 객체들이 이미지 리소스를 공유
        if CommanderSkeleton.sound_hit is None:
            CommanderSkeleton.sound_hit = load_wav('Resources/Musics/Hit3.wav')
            CommanderSkeleton.sound_hit.set_volume(30)
        if CommanderSkeleton.sound_die is None:
            CommanderSkeleton.sound_die = load_wav('Resources/Musics/Die2.wav')
            CommanderSkeleton.sound_die.set_volume(30)

    def update(self, frame_time):
        distance = self.RUN_SPEED_PPS * frame_time
        if self.Health < 0:
            self.state = self.DIE
        if self.x > 1200:
            print("Object Removed!")
            Scene_Stage1.Enemy_Units.remove(self)
        if self.state == self.STOP:
            self.frame = (self.frame + 1) % 4  # N개의 이미지를 반복
        elif self.state == self.MOVE:
            self.Frames_Move += self.FRAMES_PER_MOVE * self.ACTION_PER_TIME * frame_time
            self.frame = int(self.Frames_Move + 1) % 4  # N개의 이미지를 반복
            self.x += distance  # 오른쪽으로 10/s 의 속도로 이동
        elif self.state == self.HURT:
            self.frame = (self.frame + 1) % 1
        elif self.state == self.ATTACK:
            self.Frames_Attack += self.FRAMES_PER_ATTACK * self.ACTION_PER_TIME * frame_time
            self.frame = int(self.Frames_Attack + 1) % 8
            if self.frame > 5:
                CommanderSkeleton.sound_hit.play(1)
                self.state = self.MOVE
        elif self.state == self.DIE:
            self.frame = (self.frame + 1) % 12
            if self.frame == 10:
                CommanderSkeleton.sound_die.play(1)
                Scene_Stage1.Enemy_Units.remove(self)

    def draw(self):
        self.image.clip_draw(self.frame * 151, self.state * 159, 151, 159, self.x, self.y)
        # Width = 151, Height = 159

    def get_attack_range(self):
        return self.x - 70, self.y - 73, self.x + 250, self.y + 50

    def get_defense_size(self):
        return self.x - 70, self.y - 73, self.x + 45, self.y + 50

    def draw_bb(self):
        draw_rectangle(*self.get_attack_range())
        draw_rectangle(*self.get_defense_size())

    def attack(self, enemy):
        self.state = self.ATTACK
        enemy.Health -= self.AttackPower
        print("공격중인 객체의 체력: ", enemy.Health)


class HeadlessKnight:  # 보스 몬스터 - 헤들리스나이트의 클래스
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
    FRAMES_PER_MOVE = 6
    FRAMES_PER_ATTACK = 10

    image = None  # 클래스의 객체들이 공유하는 변수를 선언하고 None 값으로 초기화
    sound_hit = None
    sound_die = None
    BGM = None

    RUN_ATTACK, RUN_SLOW, RUN_SKILL, STAND_SKILL, DIE, STAND, RUN_FAST, MOVE, STAND_ATTACK = 0, 1, 2, 3, 4, 5, 6, 7, 8
    # 상태 정의

    def __init__(self):  # 객체의 초기값 설정
        self.x, self.y = 80, 300  # 생성위치
        self.Health = 5999999  # 체력
        self.AttackPower = 20  # 공격력
        self.state = self.MOVE
        self.frame = 0
        self.Frame = 0
        self.Frame_Die = 0
        self.attack_count = 0
        self.Frames_Move = 0
        self.Frames_Attack = 0
        self.Frames_Die = 0

        if HeadlessKnight.image is None:
                HeadlessKnight.image = load_image("Resources/EnemyUnits/HeadlessKnight.png")
        if HeadlessKnight.sound_hit is None:
            HeadlessKnight.sound_hit = load_wav('Resources/Musics/Hit3.wav')
            HeadlessKnight.sound_hit.set_volume(30)
        if HeadlessKnight.sound_die is None:
            HeadlessKnight.sound_die = load_wav('Resources/Musics/Die2.wav')
            HeadlessKnight.sound_die.set_volume(30)
        if HeadlessKnight.BGM is None:
            HeadlessKnight.BGM = load_music('Resources/Musics/CarminaBurana.ogg')  # 생성한 전역변수에 음악 삽입
            HeadlessKnight.BGM.set_volume(50)  # 음량

    def update(self, frame_time):
        distance = self.RUN_SPEED_PPS * frame_time
        if (frame_time * 100) % 5 == 0:
            Scene_Stage1.Enemy_Units.append(self)
        if self.Health < 0:
            self.state = self.DIE
        if self.state == self.RUN_ATTACK:
            self.frame = (self.frame + 1) % 6
            self.x += distance
            if self.frame > 4:
                self.state = self.RUN_FAST
        elif self.state == self.RUN_SLOW:
            self.frame = (self.frame + 1) % 6  # N개의 이미지를 반복 (이동 = 3 공격 = 4)
            self.x += distance  # 왼쪽으로 10/s 의 속도로 이동
        elif self.state == self.RUN_SKILL:
            self.x += distance
            self.frame = (self.frame + 1) % 6  # N개의 이미지를 반복 (이동 = 3 공격 = 4)
            if self.frame > 4:
                self.state = self.MOVE
        elif self.state == self.STAND_SKILL:
            self.Frames_Attack += self.FRAMES_PER_ATTACK * self.ACTION_PER_TIME * frame_time
            self.frame = int(self.Frames_Attack + 1) % 10
            if self.frame > 8:
                Scene_Stage1.Enemy_Skills.append(EnemySkills.HeadlessKnightSkill(self.x, self.y - 65))
                self.state = self.MOVE
        elif self.state == self.DIE:
            self.Frame += 4 * self.ACTION_PER_TIME * frame_time
            self.frame = int(self.Frame + 1) % 8
            self.Frames_Die += self.TIME_FOR_DIE * frame_time
            self.Frame_Die = int(self.Frames_Die + 1)
            if self.Frame_Die > 1 and self.Frame > 6:
                CommanderSkeleton.sound_die.play(1)
                Scene_Stage1.Enemy_Units.remove(self)
        elif self.state == self.STAND:
            self.frame = (self.frame + 1) % 4
        elif self.state == self.RUN_FAST:
            self.Frames_Move += self.FRAMES_PER_MOVE * self.ACTION_PER_TIME * frame_time
            self.frame = int(self.Frames_Move + 1) % 6
            self.x += distance
        elif self.state == self.MOVE:
            self.Frames_Move += self.FRAMES_PER_MOVE * self.ACTION_PER_TIME * frame_time
            self.frame = int(self.Frames_Move + 1) % 7
            self.x += distance
        elif self.state == self.STAND_ATTACK:
            self.frame = (self.frame + 1) % 7
            if self.frame > 5:
                self.state = self.MOVE

    def draw(self):
        self.image.clip_draw(self.frame * 336, self.state * 362, 336, 362, self.x, self.y)
        # 336,362

    def get_attack_range(self):
        return self.x - 130, self.y - 150, self.x + 40, self.y + 70

    def get_defense_size(self):
        return self.x - 130, self.y - 150, self.x + 40, self.y + 70

    def draw_bb(self):
        draw_rectangle(*self.get_attack_range())
        draw_rectangle(*self.get_defense_size())

    def attack(self, e):
        self.attack_count += 1
        #if self.attack_count % 4 == 0:
        self.state = self.STAND_SKILL
        #else:
            #self.state = self.STAND_ATTACK
        e.Health -= self.AttackPower
        print("공격중인 객체의 체력: ", e.Health)

    def walk(self):
        self.state = self.RUN_FAST







