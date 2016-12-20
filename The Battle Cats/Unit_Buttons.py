from pico2d import *


class ButtonNumber1:

    CHARGE_FULL, CHARGE_0, CHARGE_33, CHARGE_66 = 0, 1, 2, 3
    FRAMES_PER_CHARGE = 0
    TIME_PER_ACTION = 0.5
    ACTION_PER_TIME = 1 / TIME_PER_ACTION

    def __init__(self):
        self.x, self.y = 100, 60  # 생성 위치
        self.image = load_image('Resources/Buttons/Button_1.png')
        self.state = self.CHARGE_FULL
        self.frame = 0

    def update(self, frame_time):
        if self.state == self.CHARGE_FULL:
            print(self.frame)
        elif self.state == self.CHARGE_0:
            self.FRAMES_PER_CHARGE += self.ACTION_PER_TIME * frame_time
            self.frame = int(self.FRAMES_PER_CHARGE + 1)
            print(self.frame)
            if self.frame > 1:
                self.state = self.CHARGE_33
        elif self.state == self.CHARGE_33:
            self.FRAMES_PER_CHARGE += self.ACTION_PER_TIME * frame_time
            self.frame = int(self.FRAMES_PER_CHARGE + 1)
            print(self.frame)
            if self.frame > 2:
                self.state = self.CHARGE_66
        elif self.state == self.CHARGE_66:
            self.FRAMES_PER_CHARGE += self.ACTION_PER_TIME * frame_time
            self.frame = int(self.FRAMES_PER_CHARGE + 1)
            print(self.frame)
            if self.frame > 3:
                self.state = self.CHARGE_FULL
                self.frame = 0
                self.FRAMES_PER_CHARGE = 0

    def draw(self):
        self.image.clip_draw(self.state * 100, 0, 100, 74, self.x, self.y)

    def start(self):
        self.state = self.CHARGE_0


class ButtonNumber2:

    CHARGE_FULL, CHARGE_0, CHARGE_33, CHARGE_66 = 0, 1, 2, 3
    FRAMES_PER_CHARGE = 0
    TIME_PER_ACTION = 0.5
    ACTION_PER_TIME = 1 / TIME_PER_ACTION

    def __init__(self):
        self.x, self.y = 220, 60  # 생성 위치
        self.image = load_image('Resources/Buttons/Button_2.png')
        self.state = self.CHARGE_FULL
        self.frame = 0

    def update(self, frame_time):
        if self.state == self.CHARGE_FULL:
            print(self.frame)
        elif self.state == self.CHARGE_0:
            self.FRAMES_PER_CHARGE += self.ACTION_PER_TIME * frame_time
            self.frame = int(self.FRAMES_PER_CHARGE + 1)
            print(self.frame)
            if self.frame > 2:
                self.state = self.CHARGE_33
        elif self.state == self.CHARGE_33:
            self.FRAMES_PER_CHARGE += self.ACTION_PER_TIME * frame_time
            self.frame = int(self.FRAMES_PER_CHARGE + 1)
            print(self.frame)
            if self.frame > 4:
                self.state = self.CHARGE_66
        elif self.state == self.CHARGE_66:
            self.FRAMES_PER_CHARGE += self.ACTION_PER_TIME * frame_time
            self.frame = int(self.FRAMES_PER_CHARGE + 1)
            print(self.frame)
            if self.frame > 6:
                self.state = self.CHARGE_FULL
                self.frame = 0
                self.FRAMES_PER_CHARGE = 0

    def draw(self):
        self.image.clip_draw(self.state * 100, 0, 100, 74, self.x, self.y)

    def start(self):
        self.state = self.CHARGE_0


class ButtonNumber3:
    CHARGE_FULL, CHARGE_0, CHARGE_33, CHARGE_66 = 0, 1, 2, 3
    FRAMES_PER_CHARGE = 0
    TIME_PER_ACTION = 0.5
    ACTION_PER_TIME = 1 / TIME_PER_ACTION

    def __init__(self):
        self.x, self.y = 340, 60  # 생성 위치
        self.image = load_image('Resources/Buttons/Button_3.png')
        self.state = self.CHARGE_FULL
        self.frame = 0

    def update(self, frame_time):
        if self.state == self.CHARGE_FULL:
            print(self.frame)
        elif self.state == self.CHARGE_0:
            self.FRAMES_PER_CHARGE += self.ACTION_PER_TIME * frame_time
            self.frame = int(self.FRAMES_PER_CHARGE + 1)
            print(self.frame)
            if self.frame > 3:
                self.state = self.CHARGE_33
        elif self.state == self.CHARGE_33:
            self.FRAMES_PER_CHARGE += self.ACTION_PER_TIME * frame_time
            self.frame = int(self.FRAMES_PER_CHARGE + 1)
            print(self.frame)
            if self.frame > 6:
                self.state = self.CHARGE_66
        elif self.state == self.CHARGE_66:
            self.FRAMES_PER_CHARGE += self.ACTION_PER_TIME * frame_time
            self.frame = int(self.FRAMES_PER_CHARGE + 1)
            print(self.frame)
            if self.frame > 9:
                self.state = self.CHARGE_FULL
                self.frame = 0
                self.FRAMES_PER_CHARGE = 0

    def draw(self):
        self.image.clip_draw(self.state * 100, 0, 100, 74, self.x, self.y)

    def start(self):
        self.state = self.CHARGE_0


class ButtonNumber4:
    CHARGE_FULL, CHARGE_0, CHARGE_33, CHARGE_66 = 0, 1, 2, 3
    FRAMES_PER_CHARGE = 0
    TIME_PER_ACTION = 0.5
    ACTION_PER_TIME = 1 / TIME_PER_ACTION

    def __init__(self):
        self.x, self.y = 460, 60  # 생성 위치
        self.image = load_image('Resources/Buttons/Button_4.png')
        self.state = self.CHARGE_FULL
        self.frame = 0

    def update(self, frame_time):
        if self.state == self.CHARGE_FULL:
            print(self.frame)
        elif self.state == self.CHARGE_0:
            self.FRAMES_PER_CHARGE += self.ACTION_PER_TIME * frame_time
            self.frame = int(self.FRAMES_PER_CHARGE + 1)
            print(self.frame)
            if self.frame > 4:
                self.state = self.CHARGE_33
        elif self.state == self.CHARGE_33:
            self.FRAMES_PER_CHARGE += self.ACTION_PER_TIME * frame_time
            self.frame = int(self.FRAMES_PER_CHARGE + 1)
            print(self.frame)
            if self.frame > 8:
                self.state = self.CHARGE_66
        elif self.state == self.CHARGE_66:
            self.FRAMES_PER_CHARGE += self.ACTION_PER_TIME * frame_time
            self.frame = int(self.FRAMES_PER_CHARGE + 1)
            print(self.frame)
            if self.frame > 12:
                self.state = self.CHARGE_FULL
                self.frame = 0
                self.FRAMES_PER_CHARGE = 0

    def draw(self):
        self.image.clip_draw(self.state * 100, 0, 100, 74, self.x, self.y)

    def start(self):
        self.state = self.CHARGE_0


class ButtonNumber5:
    CHARGE_FULL, CHARGE_0, CHARGE_33, CHARGE_66 = 0, 1, 2, 3
    FRAMES_PER_CHARGE = 0
    TIME_PER_ACTION = 0.5
    ACTION_PER_TIME = 1 / TIME_PER_ACTION

    def __init__(self):
        self.x, self.y = 580, 60  # 생성 위치
        self.image = load_image('Resources/Buttons/Button_5.png')
        self.state = self.CHARGE_FULL
        self.frame = 0

    def update(self, frame_time):
        if self.state == self.CHARGE_FULL:
            print(self.frame)
        elif self.state == self.CHARGE_0:
            self.FRAMES_PER_CHARGE += self.ACTION_PER_TIME * frame_time
            self.frame = int(self.FRAMES_PER_CHARGE + 1)
            print(self.frame)
            if self.frame > 5:
                self.state = self.CHARGE_33
        elif self.state == self.CHARGE_33:
            self.FRAMES_PER_CHARGE += self.ACTION_PER_TIME * frame_time
            self.frame = int(self.FRAMES_PER_CHARGE + 1)
            print(self.frame)
            if self.frame > 10:
                self.state = self.CHARGE_66
        elif self.state == self.CHARGE_66:
            self.FRAMES_PER_CHARGE += self.ACTION_PER_TIME * frame_time
            self.frame = int(self.FRAMES_PER_CHARGE + 1)
            print(self.frame)
            if self.frame > 15:
                self.state = self.CHARGE_FULL
                self.frame = 0
                self.FRAMES_PER_CHARGE = 0

    def draw(self):
        self.image.clip_draw(self.state * 100, 0, 100, 74, self.x, self.y)

    def start(self):
        self.state = self.CHARGE_0


class ButtonNumber6:
    CHARGE_FULL, CHARGE_0, CHARGE_33, CHARGE_66 = 0, 1, 2, 3
    FRAMES_PER_CHARGE = 0
    TIME_PER_ACTION = 0.5
    ACTION_PER_TIME = 1 / TIME_PER_ACTION

    def __init__(self):
        self.x, self.y = 700, 60  # 생성 위치
        self.image = load_image('Resources/Buttons/Button_6.png')
        self.state = self.CHARGE_FULL
        self.frame = 0

    def update(self, frame_time):
        if self.state == self.CHARGE_FULL:
            print(self.frame)
        elif self.state == self.CHARGE_0:
            self.FRAMES_PER_CHARGE += self.ACTION_PER_TIME * frame_time
            self.frame = int(self.FRAMES_PER_CHARGE + 1)
            print(self.frame)
            if self.frame > 6:
                self.state = self.CHARGE_33
        elif self.state == self.CHARGE_33:
            self.FRAMES_PER_CHARGE += self.ACTION_PER_TIME * frame_time
            self.frame = int(self.FRAMES_PER_CHARGE + 1)
            print(self.frame)
            if self.frame > 12:
                self.state = self.CHARGE_66
        elif self.state == self.CHARGE_66:
            self.FRAMES_PER_CHARGE += self.ACTION_PER_TIME * frame_time
            self.frame = int(self.FRAMES_PER_CHARGE + 1)
            print(self.frame)
            if self.frame > 18:
                self.state = self.CHARGE_FULL
                self.frame = 0
                self.FRAMES_PER_CHARGE = 0

    def draw(self):
        self.image.clip_draw(self.state * 100, 0, 100, 74, self.x, self.y)

    def start(self):
        self.state = self.CHARGE_0


class ButtonNumber7:
    CHARGE_FULL, CHARGE_0, CHARGE_33, CHARGE_66 = 0, 1, 2, 3
    FRAMES_PER_CHARGE = 0
    TIME_PER_ACTION = 0.5
    ACTION_PER_TIME = 1 / TIME_PER_ACTION

    def __init__(self):
        self.x, self.y = 820, 60  # 생성 위치
        self.image = load_image('Resources/Buttons/Button_7.png')
        self.state = self.CHARGE_FULL
        self.frame = 0

    def update(self, frame_time):
        if self.state == self.CHARGE_FULL:
            print(self.frame)
        elif self.state == self.CHARGE_0:
            self.FRAMES_PER_CHARGE += self.ACTION_PER_TIME * frame_time
            self.frame = int(self.FRAMES_PER_CHARGE + 1)
            print(self.frame)
            if self.frame > 7:
                self.state = self.CHARGE_33
        elif self.state == self.CHARGE_33:
            self.FRAMES_PER_CHARGE += self.ACTION_PER_TIME * frame_time
            self.frame = int(self.FRAMES_PER_CHARGE + 1)
            print(self.frame)
            if self.frame > 14:
                self.state = self.CHARGE_66
        elif self.state == self.CHARGE_66:
            self.FRAMES_PER_CHARGE += self.ACTION_PER_TIME * frame_time
            self.frame = int(self.FRAMES_PER_CHARGE + 1)
            print(self.frame)
            if self.frame > 21:
                self.state = self.CHARGE_FULL
                self.frame = 0
                self.FRAMES_PER_CHARGE = 0

    def draw(self):
        self.image.clip_draw(self.state * 100, 0, 100, 74, self.x, self.y)

    def start(self):
        self.state = self.CHARGE_0


class ButtonNumber8:
    CHARGE_FULL, CHARGE_0, CHARGE_33, CHARGE_66 = 0, 1, 2, 3
    FRAMES_PER_CHARGE = 0
    TIME_PER_ACTION = 0.5
    ACTION_PER_TIME = 1 / TIME_PER_ACTION

    def __init__(self):
        self.x, self.y = 940, 60  # 생성 위치
        self.image = load_image('Resources/Buttons/Button_8.png')
        self.state = self.CHARGE_FULL
        self.frame = 0

    def update(self, frame_time):
        if self.state == self.CHARGE_FULL:
            print(self.frame)
        elif self.state == self.CHARGE_0:
            self.FRAMES_PER_CHARGE += self.ACTION_PER_TIME * frame_time
            self.frame = int(self.FRAMES_PER_CHARGE + 1)
            print(self.frame)
            if self.frame > 8:
                self.state = self.CHARGE_33
        elif self.state == self.CHARGE_33:
            self.FRAMES_PER_CHARGE += self.ACTION_PER_TIME * frame_time
            self.frame = int(self.FRAMES_PER_CHARGE + 1)
            print(self.frame)
            if self.frame > 16:
                self.state = self.CHARGE_66
        elif self.state == self.CHARGE_66:
            self.FRAMES_PER_CHARGE += self.ACTION_PER_TIME * frame_time
            self.frame = int(self.FRAMES_PER_CHARGE + 1)
            print(self.frame)
            if self.frame > 24:
                self.state = self.CHARGE_FULL
                self.frame = 0
                self.FRAMES_PER_CHARGE = 0

    def draw(self):
        self.image.clip_draw(self.state * 100, 0, 100, 74, self.x, self.y)

    def start(self):
        self.state = self.CHARGE_0


class ButtonNumber9:
    CHARGE_FULL, CHARGE_0, CHARGE_33, CHARGE_66 = 0, 1, 2, 3
    FRAMES_PER_CHARGE = 0
    TIME_PER_ACTION = 0.5
    ACTION_PER_TIME = 1 / TIME_PER_ACTION

    def __init__(self):
        self.x, self.y = 1060, 60  # 생성 위치
        self.image = load_image('Resources/Buttons/Button_9.png')
        self.state = self.CHARGE_FULL
        self.frame = 0

    def update(self, frame_time):
        if self.state == self.CHARGE_FULL:
            print(self.frame)
        elif self.state == self.CHARGE_0:
            self.FRAMES_PER_CHARGE += self.ACTION_PER_TIME * frame_time
            self.frame = int(self.FRAMES_PER_CHARGE + 1)
            print(self.frame)
            if self.frame > 9:
                self.state = self.CHARGE_33
        elif self.state == self.CHARGE_33:
            self.FRAMES_PER_CHARGE += self.ACTION_PER_TIME * frame_time
            self.frame = int(self.FRAMES_PER_CHARGE + 1)
            print(self.frame)
            if self.frame > 18:
                self.state = self.CHARGE_66
        elif self.state == self.CHARGE_66:
            self.FRAMES_PER_CHARGE += self.ACTION_PER_TIME * frame_time
            self.frame = int(self.FRAMES_PER_CHARGE + 1)
            print(self.frame)
            if self.frame > 27:
                self.state = self.CHARGE_FULL
                self.frame = 0
                self.FRAMES_PER_CHARGE = 0

    def draw(self):
        self.image.clip_draw(self.state * 100, 0, 100, 74, self.x, self.y)

    def start(self):
        self.state = self.CHARGE_0


class SkillButton:

    CHARGE_FULL, CHARGE_0, CHARGE_10, CHARGE_30, CHARGE_40, CHARGE_50, CHARGE_70, CHARGE_90 = 0, 1, 2, 3, 4, 5, 6, 7

    FRAMES_PER_CHARGE = 0
    TIME_PER_ACTION = 0.5
    ACTION_PER_TIME = 1 / TIME_PER_ACTION

    def __init__(self):
        self.x, self.y = 1200, 100  # 생성 위치
        self.image = load_image('Resources/Buttons/Button_Skill.png')
        self.state = self.CHARGE_FULL
        self.frame = 0

    def update(self, frame_time):
        if self.state == self.CHARGE_FULL:
            pass
        elif self.state == self.CHARGE_0:
            self.FRAMES_PER_CHARGE += self.ACTION_PER_TIME * frame_time
            self.frame = int(self.FRAMES_PER_CHARGE + 1)
            print(self.frame)
            if self.frame > 10:
                self.state = self.CHARGE_10
        elif self.state == self.CHARGE_10:
            self.FRAMES_PER_CHARGE += self.ACTION_PER_TIME * frame_time
            self.frame = int(self.FRAMES_PER_CHARGE + 1)
            print(self.frame)
            if self.frame > 20:
                self.state = self.CHARGE_30
        elif self.state == self.CHARGE_30:
            self.FRAMES_PER_CHARGE += self.ACTION_PER_TIME * frame_time
            self.frame = int(self.FRAMES_PER_CHARGE + 1)
            print(self.frame)
            if self.frame > 30:
                self.state = self.CHARGE_40
        elif self.state == self.CHARGE_40:
            self.FRAMES_PER_CHARGE += self.ACTION_PER_TIME * frame_time
            self.frame = int(self.FRAMES_PER_CHARGE + 1)
            print(self.frame)
            if self.frame > 40:
                self.state = self.CHARGE_50
        elif self.state == self.CHARGE_50:
            self.FRAMES_PER_CHARGE += self.ACTION_PER_TIME * frame_time
            self.frame = int(self.FRAMES_PER_CHARGE + 1)
            print(self.frame)
            if self.frame > 50:
                self.state = self.CHARGE_70
        elif self.state == self.CHARGE_70:
            self.FRAMES_PER_CHARGE += self.ACTION_PER_TIME * frame_time
            self.frame = int(self.FRAMES_PER_CHARGE + 1)
            print(self.frame)
            if self.frame > 60:
                self.state = self.CHARGE_90
        elif self.state == self.CHARGE_90:
            self.FRAMES_PER_CHARGE += self.ACTION_PER_TIME * frame_time
            self.frame = int(self.FRAMES_PER_CHARGE + 1)
            print(self.frame)
            if self.frame > 70:
                self.state = self.CHARGE_FULL
                self.frame = 0
                self.FRAMES_PER_CHARGE = 0

    def draw(self):
        self.image.clip_draw(self.state * 200, 0, 200, 200, self.x, self.y)

    def start(self):
        self.state = self.CHARGE_0
