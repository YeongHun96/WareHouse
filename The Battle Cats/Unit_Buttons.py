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
        self.FRAMES_PER_CHARGE += self.ACTION_PER_TIME * frame_time
        self.frame = (self.FRAMES_PER_CHARGE + 1)
        print(self.frame)

    def draw(self):
        self.image.clip_draw(self.frame * 109, self.state * 150, 109, 150, self.x, self.y)

    def start(self):
        self.state = self.CHARGE_0


class ButtonNumber2:
    def __init__(self):
        self.x, self.y = 260, 60  # 생성 위치
        self.image = load_image('Resources/Buttons/2번_2.png')

    def update(self, frame_time):
        pass

    def draw(self):
        self.image.draw(self.x, self.y)


class ButtonNumber3:
    def __init__(self):
        self.x, self.y = 380, 60  # 생성 위치
        self.image = load_image('Resources/Buttons/3번_2.png')

    def update(self, frame_time):
        pass

    def draw(self):
        self.image.draw(self.x, self.y)


class ButtonNumber4:
    def __init__(self):
        self.x, self.y = 500, 60  # 생성 위치
        self.image = load_image('Resources/Buttons/4번_2.png')

    def update(self, frame_time):
        pass

    def draw(self):
        self.image.draw(self.x, self.y)


class ButtonNumber5:
    def __init__(self):
        self.x, self.y = 620, 60  # 생성 위치
        self.image = load_image('Resources/Buttons/5번_2.png')

    def update(self, frame_time):
        pass

    def draw(self):
        self.image.draw(self.x, self.y)


class ButtonNumber6:
    def __init__(self):
        self.x, self.y = 740, 60  # 생성 위치
        self.image = load_image('Resources/Buttons/6번_2.png')

    def update(self, frame_time):
        pass

    def draw(self):
        self.image.draw(self.x, self.y)


class ButtonNumber7:
    def __init__(self):
        self.x, self.y = 860, 60  # 생성 위치
        self.image = load_image('Resources/Buttons/7번_2.png')

    def update(self, frame_time):
        pass

    def draw(self):
        self.image.draw(self.x, self.y)


class ButtonNumber8:
    def __init__(self):
        self.x, self.y = 980, 60  # 생성 위치
        self.image = load_image('Resources/Buttons/8번_2.png')

    def update(self, frame_time):
        pass

    def draw(self):
        self.image.draw(self.x, self.y)


class ButtonNumber9:
    def __init__(self):
        self.x, self.y = 1100, 60  # 생성 위치
        self.image = load_image('Resources/Buttons/9번_2.png')

    def update(self, frame_time):
        pass

    def draw(self):
        self.image.draw(self.x, self.y)

