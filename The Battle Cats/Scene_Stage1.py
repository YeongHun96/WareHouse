# 인게임 상태를 관리하는 파일

from pico2d import*
import BackGround
import Castle
import Cats
import GameFrameWork
import Enemies
import Functions
import EnemySkills
import CatSkills
import Unit_Buttons
import Skills

# *******************전역변수들 초기화**********************#
running = True
Back_Ground = None
My_Castle, Enemy_Castle = None, None
Basic_Cat, Tank_Cat, Axe_Cat, Gross_Cat, Cow_Cat, Bird_Cat, UFO_Cat, Fish_Cat, Lizard_Cat, Titan_Cat = None, None, None, None, None, None, None, None, None, None
Skele_Dog, Mummy_Dog, Officer_Skeleton, Commander_Skeleton = None, None, None, None
Headless_Knight = None
Headless_Knight_Skill = None
Lizard_Cat_Skill, UFO_Cat_SKill = None, None
BGM = None
Number_1, Number_2, Number_3, Number_4, Number_5, Number_6, Number_7, Number_8, Number_9 = None, None, None, None, None, None, None, None, None
Laser_Beam = None
Skill_Button = None
TIME_PER_ACTION = None
ACTION_PER_TIME = None
Frames = None
Frame = None
Count_Number = None

# **********************리스트들**********************#
Cat_Units = []  # 아군 유닛들을 관리할 리스트 생성
Enemy_Units = []  # 적군 유닛들을 관리할 리스트 생성
Cat_Skills = []  # 아군 유닛의 스킬들을 관리할 리스트 생성
Enemy_Skills = []  # 적군 유닛의 스킬들을 관리할 리스트 생성
Buttons = []


def enter():  # 게임 상태 ( 인게임 ) 에 들어올 때 초기화
    global Back_Ground  # 전역변수 선언
    Back_Ground = BackGround.BackGround()  # 생성한 전역변수로 BackGround 객체를 가리킴
    global BGM  # 전역변수 선언
    BGM = load_music('Resources/Musics/DefaultBattle.ogg')  # 생성한 전역변수에 음악 삽입
    BGM.set_volume(50)  # 음량
    BGM.repeat_play()  # 반복 재생
    global My_Castle, Enemy_Castle  # 전역변수 선언
    My_Castle = Castle.MyCastle()  # 생성한 전역변수로 MyCastle 객체를 가리킴
    Enemy_Castle = Castle.EnemyCastle()  # 생성한 전역변수로 EnemyCastle 객체를 가리킴
    global Basic_Cat, Tank_Cat, Axe_Cat, Gross_Cat, Cow_Cat, Bird_Cat, UFO_Cat, Fish_Cat, Lizard_Cat, Titan_Cat  # 전역변수 선언
    Basic_Cat = Cats.BasicCat()  # 생성한 전역변수로 BasicCat 객체를 가리킴
    Tank_Cat = Cats.TankCat()
    Axe_Cat = Cats.AxeCat()  # 생성한 전역변수로 AxeCat 객체를 가리킴
    Gross_Cat = Cats.GrossCat()
    Cow_Cat = Cats.CowCat()
    Bird_Cat = Cats.BirdCat()
    UFO_Cat = Cats.UFOCat()
    Fish_Cat = Cats.FishCat()
    Lizard_Cat = Cats.LizardCat()
    Titan_Cat = Cats.TitanCat()
    global Skele_Dog, Mummy_Dog, Officer_Skeleton, Commander_Skeleton
    Skele_Dog = Enemies.SkeleDog()
    Mummy_Dog = Enemies.MummyDog()
    Officer_Skeleton = Enemies.OfficerSkeleton()
    Commander_Skeleton = Enemies.CommanderSkeleton()
    global Headless_Knight
    Headless_Knight = Enemies.HeadlessKnight()
    global Headless_Knight_Skill
    Headless_Knight_Skill = EnemySkills.HeadlessKnightSkill(None, None)
    global Lizard_Cat_Skill, UFO_Cat_SKill
    Lizard_Cat_Skill = CatSkills.LizardCatSkill(None, None)
    UFO_Cat_SKill = CatSkills.UFOCatSkill(None, None)
    global Number_1, Number_2, Number_3, Number_4, Number_5, Number_6, Number_7, Number_8, Number_9
    global Skill_Button
    Number_1 = Unit_Buttons.ButtonNumber1()
    Number_2 = Unit_Buttons.ButtonNumber2()
    Number_3 = Unit_Buttons.ButtonNumber3()
    Number_4 = Unit_Buttons.ButtonNumber4()
    Number_5 = Unit_Buttons.ButtonNumber5()
    Number_6 = Unit_Buttons.ButtonNumber6()
    Number_7 = Unit_Buttons.ButtonNumber7()
    Number_8 = Unit_Buttons.ButtonNumber8()
    Number_9 = Unit_Buttons.ButtonNumber9()
    Skill_Button = Unit_Buttons.SkillButton()
    Buttons.append(Number_1)
    Buttons.append(Number_2)
    Buttons.append(Number_3)
    Buttons.append(Number_4)
    Buttons.append(Number_5)
    Buttons.append(Number_6)
    Buttons.append(Number_7)
    Buttons.append(Number_8)
    Buttons.append(Number_9)
    Buttons.append(Skill_Button)
    global Laser_Beam
    Laser_Beam = Skills.LaserBeam()
    global TIME_PER_ACTION
    global ACTION_PER_TIME
    TIME_PER_ACTION = 0.5
    ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
    global Frame
    global Frames
    Frame = 0
    Frames = 0
    global Count_Number
    Count_Number = 0


def exit():  # 게임 상태 ( 인게임 ) 에서 나갈 때 종료화
    # 전역변수를 사용함을 선언
    global Back_Ground
    global Basic_Cat, Tank_Cat, Axe_Cat, Gross_Cat, Cow_Cat, Bird_Cat, UFO_Cat, Fish_Cat, Lizard_Cat, Titan_Cat
    global My_Castle, Enemy_Castle  # 전역변수임을 명시
    global Skele_Dog, Mummy_Dog, Officer_Skeleton, Commander_Skeleton
    global Headless_Knight
    global Headless_Knight_Skill
    global BGM
    global Lizard_Cat_Skill, UFO_Cat_SKill
    global Number_1, Number_2, Number_3, Number_4, Number_5, Number_6, Number_7, Number_8, Number_9
    global Laser_Beam

    # 전역변수들을 소멸
    del Back_Ground
    del Basic_Cat, Tank_Cat, Axe_Cat, Gross_Cat, Cow_Cat, Bird_Cat, UFO_Cat, Fish_Cat, Lizard_Cat, Titan_Cat
    del My_Castle, Enemy_Castle
    del Skele_Dog, Mummy_Dog, Officer_Skeleton, Commander_Skeleton
    del Headless_Knight
    del Headless_Knight_Skill
    del BGM
    del Lizard_Cat_Skill, UFO_Cat_SKill
    del Number_1, Number_2, Number_3, Number_4, Number_5, Number_6, Number_7, Number_8, Number_9
    del Laser_Beam


def update(frame_time):  # 업데이트
    global My_Castle
    global Enemy_Castle
    global Laser_Beam
    global Frame, Frames
    global Count_Number

    for Cat in Cat_Units:  # 리스트에 속하는 아군 유닛
        Cat.update(frame_time)  # 업데이트
    for Enemy in Enemy_Units:  # 리스트에 속하는 적군 유닛
        Enemy.update(frame_time)  # 업데이트
    My_Castle.update(frame_time)
    Enemy_Castle.update()
    for CatSkill in Cat_Skills:
        CatSkill.update(frame_time)
    for EnemySkill in Enemy_Skills:
        EnemySkill.update(frame_time)
    for Button in Buttons:
        Button.update(frame_time)
    # **************************Collision Check**************************************#
    for Cat in Cat_Units:  # 리스트에 속하는 아군 유닛들
        for Enemy in Enemy_Units:  # 리스트에 속하는 적군 유닛들에 대해
            if Functions.collide_cat(Cat, Enemy and Enemy_Castle):  # 적군 유닛과 적군 성 모두 충돌체크 된 상황
                Cat.attack(Enemy_Castle)  # 적군 성을 먼저 공격한다
            elif Functions.collide_cat(Cat, Enemy):  # 아군 유닛과 적군 유닛간 충돌
                Cat.attack(Enemy)  # 아군 유닛 -> 적군 유닛 공격
        if Functions.collide_cat(Cat, Enemy_Castle):  # 아군 유닛과 적군 성 간 충돌
            Cat.attack(Enemy_Castle)  # 아군 유닛 -> 적군 성 공격

    for Enemy in Enemy_Units:  # 모든 적군들이
        for Cat in Cat_Units:  # 모든 아군들에 대해
            if Functions.collide_enemy(Enemy, Cat and My_Castle):  # 아군 유닛과 아군 성이 동시에 사정거리에 있는 상황
                Enemy.attack(My_Castle)  # 아군 성을 먼저 공격한다
            elif Functions.collide_enemy(Enemy, Cat):  # 적군 유닛과 아군 유닛간 충돌 있으면
                Enemy.attack(Cat)  # 적군 유닛 -> 아군 유닛 공격
        if Functions.collide_enemy(Enemy, My_Castle):  # 적군 유닛과 아군 성간 충돌
            Enemy.attack(My_Castle)  # 적군 유닛 -> 아군 성 공격

    for CatSkill in Cat_Skills:
        for Enemy in Enemy_Units:
            if Functions.collide_cat(CatSkill, Enemy and Enemy_Castle):  # 적군 유닛과 적군 성 모두 충돌체크 된 상황
                CatSkill.attack(Enemy_Castle)  # 적군 성을 먼저 공격한다
            elif Functions.collide_cat(CatSkill, Enemy):  # 아군 유닛과 적군 유닛간 충돌
                CatSkill.attack(Enemy)  # 아군 유닛 -> 적군 유닛 공격
        if Functions.collide_cat(CatSkill, Enemy_Castle):  # 아군 유닛과 적군 성 간 충돌
            CatSkill.attack(Enemy_Castle)  # 아군 유닛 -> 적군 성 공격

    for EnemySkill in Enemy_Skills:
        for Cat in Cat_Units:  # 모든 아군들에 대해
            if Functions.collide_enemy(EnemySkill, Cat and My_Castle):  # 아군 유닛과 아군 성이 동시에 사정거리에 있는 상황
                EnemySkill.attack(My_Castle)  # 아군 성을 먼저 공격한다
            elif Functions.collide_enemy(EnemySkill, Cat):  # 적군 유닛과 아군 유닛간 충돌 있으면
                EnemySkill.attack(Cat)  # 적군 유닛 -> 아군 유닛 공격
        if Functions.collide_enemy(EnemySkill, My_Castle):  # 적군 유닛과 아군 성간 충돌
            EnemySkill.attack(My_Castle)  # 적군 유닛 -> 아군 성 공격
    # *******************************적 유닛 생성**************************************#

    Frames += ACTION_PER_TIME * frame_time * 100
    Frame = int(Frames + 1)
    # 분당 12000 F
    print(Frame)
    if Frame % 50 == 0 and Count_Number == 0:
        Enemy_Units.append(Enemies.MummyDog())
        pass
    if Frame % 50 == 0:
        Enemy_Units.append(Enemies.SkeleDog())
        pass
    if Frame % 100 == 0:
        Enemy_Units.append(Enemies.SkeletonSoldier())
        pass
    if Frame % 200 == 0:
        Enemy_Units.append(Enemies.OfficerSkeleton())
        pass
    if Frame % 500 == 0:
        Enemy_Units.append(Enemies.CommanderSkeleton())
        pass
    if Frame > 10000 and Count_Number == 0:
        Back_Ground.image = load_image('Resources/BackGround_Final.png')
        Enemies.HeadlessKnight.BGM.repeat_play()  # 반복 재생
        Enemy_Units.append(Enemies.HeadlessKnight())
        Count_Number = 1


def draw():
    global My_Castle
    global Enemy_Castle
    global Back_Ground
    global Laser_Beam
    global Number_1, Number_2, Number_3, Number_4, Number_5, Number_6, Number_7, Number_8, Number_9

    clear_canvas()  # 캔버스 지우기

    Back_Ground.draw()  # 배경화면 그리기
    My_Castle.draw()  # 아군 성 그리기
    # My_Castle.draw_bb()  # 아군 성의 충돌범위 그리기
    Enemy_Castle.draw()  # 적군 성 그리기
    # Enemy_Castle.draw_bb()  # 적군 성의 충돌범위 그리기

    for Button in Buttons:
        Button.draw()

    for Cat in Cat_Units:  # 리스트에 속하는 아군 유닛 모두를
        Cat.draw()  # 그리기
        #Cat.draw_bb()  # 충돌범위 그리기

    for Enemy in Enemy_Units:  # 리스트에 속하는 적군 유닛 모두를
        Enemy.draw()  # 그리기
        #Enemy.draw_bb()  # 충돌범위 그리기

    for CatSkill in Cat_Skills:
        CatSkill.draw()
        #CatSkill.draw_bb()

    for EnemySkill in Enemy_Skills:
        EnemySkill.draw()
        #EnemySkill.draw_bb()

    update_canvas()  # 캔버스 업데이트


def handle_events(frame_time):  # 입력신호를 관리하는 함수
    global Cat_Units  # 전역으로 선언된 리스트를 사용할 것을 명시
    global Enemy_Units  # 전역으로 선언된 리스트를 사용할 것을 명시
    global Laser_Beam
    global Skill_Button
    global BGM
    global Back_Ground

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            GameFrameWork.quit()  # 게임을 중단
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:  # ESC 키 입력 시
                GameFrameWork.quit()  # 게임을 중단
            elif event.key == SDLK_1 and Number_1.state == Number_1.CHARGE_FULL:  # 1번 입력 시
                Cat_Units.append(Cats.BasicCat())  # 리스트에 기본 고양이 객체 추가
                Number_1.start()
                # SDLK_1번 입력 시 Unit_Buttons.Number1 객체에 신호를 주면
                # 그때부터 유닛의 생성 쿨타임을 Frame_time으로 계산해서
                # (유닛 생성 쿨타임 - frame_time) / 유닛 생성 쿨타임 의 공식으로
                # 100%, 66%, 33% 마다 쿨타임 이미지를 적용
            elif event.key == SDLK_2 and Number_2.state == Number_2.CHARGE_FULL:  # 2번 입력 시
                Cat_Units.append(Cats.TankCat())  # 리스트에 벽 고양이 객체 추가
                Number_2.start()
            elif event.key == SDLK_3 and Number_3.state == Number_3.CHARGE_FULL:  # 3번 입력 시1
                Cat_Units.append(Cats.AxeCat())   # 리스트에 전사 고양이 객체 추가
                Number_3.start()
            elif event.key == SDLK_4 and Number_4.state == Number_4.CHARGE_FULL:  # 4번 입력 시
                Cat_Units.append(Cats.GrossCat())  # 각선미 고양이 객체 생성
                Number_4.start()
            elif event.key == SDLK_5 and Number_5.state == Number_5.CHARGE_FULL:  # 5번 입력 시
                Cat_Units.append(Cats.CowCat())  # 황소 고양이 객체 생성
                Number_5.start()
            elif event.key == SDLK_6 and Number_6.state == Number_6.CHARGE_FULL:  # 6번 입력 시
                Cat_Units.append(Cats.UFOCat())  # 물고기 고양이 객체 생성
                Number_6.start()
            elif event.key == SDLK_7 and Number_7.state == Number_7.CHARGE_FULL:  # 7번 입력 시
                Cat_Units.append(Cats.FishCat())  # 천사 고양이 객체 생성
                Number_7.start()
            elif event.key == SDLK_8 and Number_8.state == Number_8.CHARGE_FULL:  # 8번 입력 시
                Cat_Units.append(Cats.LizardCat())  # 도마뱀 고양이 객체 생성
                Number_8.start()
            elif event.key == SDLK_9 and Number_9.state == Number_9.CHARGE_FULL:  # 9번 입력 시
                Cat_Units.append(Cats.TitanCat())  # 거인 고양이 객체 생성
                Number_9.start()
            elif event.key == SDLK_q and Skill_Button.state == Skill_Button.CHARGE_FULL:
                Cat_Skills.append(Skills.LaserBeam())
                My_Castle.state = My_Castle.CHARGE
                Skill_Button.start()


def pause():
    pass


def resume():
    pass
