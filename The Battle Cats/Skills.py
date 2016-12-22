from pico2d import *
import Castle
import Scene_Stage1

My_Castle = None


class LaserBeam:
    TIME_PER_ACTION = 0.9
    ACTION_PER_TIME = 1.0 / TIME_PER_ACTION

    NORMAL, ATTACK = -1, 1

    def __init__(self):
        self.x, self.y = 870, 300
        self.AttackPower = 200
        self.image = load_image("Resources/Laser5.png")
        self.frame = -1
        self.Frame_Attack = 0
        self.Frames_Attack = 0
        self.state = self.ATTACK
        self.sound_hit = load_wav('Resources/Musics/Charging.wav')  # 생성한 전역변수에 음악 삽입
        self.sound_hit.set_volume(50)  # 음량
        global My_Castle
        My_Castle = Castle.MyCastle()

    def update(self, frame_time):
        if self.state == self.ATTACK:
            self.Frames_Attack += self.ACTION_PER_TIME * frame_time
            self.Frame_Attack = int(self.Frames_Attack + 1)
            self.sound_hit.play(1)
            self.frame = (self.frame + 1)  # N개의 이미지를 반복
            delay(0.05)
            if self.frame == 5:
                self.sound_hit = load_wav('Resources/Musics/Shot.wav')
                self.sound_hit.play(1)
                pass
            if self.frame > 12 and self.Frame_Attack > 2:
                self.state = self.NORMAL
                My_Castle.state = My_Castle.NORMAL
                Scene_Stage1.Cat_Skills.remove(self)

    def draw(self):
        self.image.clip_draw(self.frame * 667, 0, 667, 260, self.x, self.y)

    def get_attack_range(self):
        return self.x - 340, self.y - 130, self.x + 340, self.y + 130

    def draw_bb(self):
        draw_rectangle(*self.get_attack_range())

    def attack(self, e):
        self.state = self.ATTACK
        e.Health -= self.AttackPower
        print("공격중인 객체의 체력: ", e.Health)
