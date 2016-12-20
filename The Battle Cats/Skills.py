from pico2d import *
import Castle

My_Castle = None


class LaserBeam:

    NORMAL, ATTACK = -1, 1

    def __init__(self):
        self.x, self.y = 870, 300
        self.AttackPower = 100
        self.image = load_image("Resources/Laser5.png")
        self.frame = -1
        self.state = self.NORMAL
        self.BGM = load_wav('Resources/Musics/Charging.wav')  # 생성한 전역변수에 음악 삽입
        self.BGM.set_volume(50)  # 음량
        global My_Castle
        My_Castle = Castle.MyCastle()

    def update(self):
        if self.state == self.ATTACK:
            My_Castle.charge()
            self.BGM.play(1)  # 반복 재생
            self.frame = (self.frame + 1) % 13  # N개의 이미지를 반복
            delay(0.05)
            if self.frame > 5:
                self.BGM = load_wav('Resources/Musics/Shot.wav')
                self.BGM.play(1)  # 반복 재생
            if self.frame > 11:
                self.state = self.NORMAL
                My_Castle.state = My_Castle.NORMAL

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
