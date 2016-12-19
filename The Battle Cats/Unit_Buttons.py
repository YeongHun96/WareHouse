from pico2d import *


class ButtonNumber1:

    CHARGE_FULL, CHARGE_0, CHARGE_33, CHARGE_66 = 0, 1, 2, 3
    FRAMES_PER_CHARGE = 0
    TIME_PER_ACTION = 0.5
    ACTION_PER_TIME = 1 / TIME_PER_ACTION

    def __init__(self):
        self.x, self.y = 140, 60  # 생성 위치
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


class ButtonNumber2:

    CHARGE_FULL, CHARGE_0, CHARGE_33, CHARGE_66 = 0, 1, 2, 3
    FRAMES_PER_CHARGE = 0
    TIME_PER_ACTION = 0.5
    ACTION_PER_TIME = 1 / TIME_PER_ACTION

    def __init__(self):
        self.x, self.y = 260, 60  # 생성 위치
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


class ButtonNumber3:
    CHARGE_FULL, CHARGE_0, CHARGE_33, CHARGE_66 = 0, 1, 2, 3
    FRAMES_PER_CHARGE = 0
    TIME_PER_ACTION = 0.5
    ACTION_PER_TIME = 1 / TIME_PER_ACTION

    def __init__(self):
        self.x, self.y = 380, 60  # 생성 위치
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


class ButtonNumber4:
    CHARGE_FULL, CHARGE_0, CHARGE_33, CHARGE_66 = 0, 1, 2, 3
    FRAMES_PER_CHARGE = 0
    TIME_PER_ACTION = 0.5
    ACTION_PER_TIME = 1 / TIME_PER_ACTION

    def __init__(self):
        self.x, self.y = 500, 60  # 생성 위치
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


class ButtonNumber5:
    CHARGE_FULL, CHARGE_0, CHARGE_33, CHARGE_66 = 0, 1, 2, 3
    FRAMES_PER_CHARGE = 0
    TIME_PER_ACTION = 0.5
    ACTION_PER_TIME = 1 / TIME_PER_ACTION

    def __init__(self):
        self.x, self.y = 620, 60  # 생성 위치
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
        self.x, self.y = 740, 60  # 생성 위치
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


class ButtonNumber7:
    CHARGE_FULL, CHARGE_0, CHARGE_33, CHARGE_66 = 0, 1, 2, 3
    FRAMES_PER_CHARGE = 0
    TIME_PER_ACTION = 0.5
    ACTION_PER_TIME = 1 / TIME_PER_ACTION

    def __init__(self):
        self.x, self.y = 860, 60  # 생성 위치
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


class ButtonNumber8:
    CHARGE_FULL, CHARGE_0, CHARGE_33, CHARGE_66 = 0, 1, 2, 3
    FRAMES_PER_CHARGE = 0
    TIME_PER_ACTION = 0.5
    ACTION_PER_TIME = 1 / TIME_PER_ACTION

    def __init__(self):
        self.x, self.y = 980, 60  # 생성 위치
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


class ButtonNumber9:
    CHARGE_FULL, CHARGE_0, CHARGE_33, CHARGE_66 = 0, 1, 2, 3
    FRAMES_PER_CHARGE = 0
    TIME_PER_ACTION = 0.5
    ACTION_PER_TIME = 1 / TIME_PER_ACTION

    def __init__(self):
        self.x, self.y = 1100, 60  # 생성 위치
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
