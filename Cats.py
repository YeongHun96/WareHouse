import random
from pico2d import*

class State:
    Left_Move = 0
    Right_Move = 1
    Left_Attack = 2
    Right_Attack = 3
    State_Count = 4

class BasicCat:
    image = None  # 클래스의 객체들이 공유하는 변수를 선언하고 None 값으로 초기화

    def __init__(self):
        self.x, self.y = 970, 170 + random.randint(0, 30)
        self.Health = 300
        self.Attack_Power = 8
        self.Attack_Range = 140
        self.Time_between_attacks = 1.23  # seconds
        self.Movement_Speed = 10
        self.Attack_animation = 8  #frame
        self.Recharging_Time = 2.33  #seconds

        self.state = State.Right_Move
        self.frame = 0
        if BasicCat.image == None:  # 만약 변수의 값이 None 이면
            BasicCat.image = load_image("resource/basic_cat.png") # 한 번의 이미지 로딩을 통해 모든 객체들이 이미지 리소스를 공유

    def update(self):
        self.frame = (self.frame + 1) % 3
        self.x -= 5

        if 1:# 적 팀 유닛을 만나면
            pass
        # 공격을 시작한다.



    #가로 46 세로 63
    def draw(self):
        self.image.clip_draw(self.frame * 46, (State.State_Count - self.state) * 63, 46, 63, self.x, self.y)

    def handle_right_move(self):
        self.x += 5
        self.run_frames +=1

class Warrior_Cat:
    image = None
    def __init__(self):
        self.health = 3000
        self.attack_power = 1000
        self.attack_range = 350
        self.time_between_attacks = 50
        self.movement_speed = 4
        self.attack_animation = 8
        self.frame = 0
        self.delay = 0

        self.x, self.y = 50, 200 + random.randint(0,30)
        if Warrior_Cat.image == None:  # 만약 변수의 값이 None 이면
            Warrior_Cat.image = load_image("resource/warrior_cat.png")  # 한 번의 이미지 로딩을 통해 모든 객체들이 이미지 리소스를 공유

    def update(self):
        self.delay += 1

        if self.delay > 1:
            self.delay = 0
            self.frame = (self.frame + 1) % 3
        self.x += 5

    def draw(self):
        self.image.clip_draw(self.frame * 112, 250, 112, 125, self.x, self.y)

    def handle_right_move(self):
        self.x += 5
        self.run_frames += 1