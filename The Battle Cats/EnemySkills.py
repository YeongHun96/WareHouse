from pico2d import *
import Scene_Stage1


class HeadlessKnightSkill:
    # 프레임 시간에 따른 객체 이동 구현
    PIXEL_PER_METER = (10.0 / 0.3)  # 100픽셀이 10m라고 설정
    RUN_SPEED_KMPH = 30.0  # 시간당 5km
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0) / 60.0
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)
    # 프레임 시간에 따른 액션 프레임의 조절
    TIME_PER_ACTION = 0.5
    ACTION_PER_TIME = 1 / TIME_PER_ACTION
    FRAMES_PER_MOVE = 6

    image = None
    sound_hit = None

    def __init__(self, x, y):
        self.x, self.y = x, y
        self.MovementSpeed = 10
        self.AttackPower = 2
        self.frame = 0
        self.Frames_Move = 0

        if HeadlessKnightSkill.image is None:
            HeadlessKnightSkill.image = load_image("Resources/EnemyUnits/SkillEffects/Headless_Skill.png")
        if HeadlessKnightSkill.sound_hit is None:
            HeadlessKnightSkill.sound_hit = load_wav("Resources/Musics/Hit3.wav")

    def update(self, frame_time):
        distance = self.RUN_SPEED_PPS * frame_time
        if self.x > 1400:
            Scene_Stage1.Enemy_Skills.remove(self)
            print("Object Removed!")
        self.Frames_Move += self.FRAMES_PER_MOVE * self.ACTION_PER_TIME * frame_time
        self.frame = int(self.Frames_Move + 1) % 3  # N개의 이미지를 반복 (이동 = 3 공격 = 4)
        self.x += distance  # 왼쪽으로 10/s 의 속도로 이동

    def draw(self):
        self.image.clip_draw(self.frame * 225, 0, 220, 160, self.x, self.y)
        # 0: 오른쪽 바라보며 공격  1: 왼쪽 바라보며 공격 2 : 오른쪽바라봄 3 : 왼쪽 바라봄

    def get_attack_range(self):
        return self.x - 100, self.y - 80, self.x + 100, self.y + 90

    def draw_bb(self):
        draw_rectangle(*self.get_attack_range())

    def attack(self, enemy):
        enemy.Health -= self.AttackPower
        print("공격중인 객체의 체력: ", enemy.Health)
