# 인게임 상태를 관리하는 파일

from pico2d import*

import BackGround
import Castle
import Cats
import GameFrameWork
import Enemies
import Functions

running = True
Back_Ground = None
My_Castle, Enemy_Castle = None, None
Basic_Cat, Tank_Cat, Axe_Cat, Gross_Cat, Cow_Cat, Bird_Cat, Fish_Cat, Lizard_Cat, Titan_Cat = None, None, None, None, None, None, None, None, None
Officer_Skeleton, Commander_Skeleton = None, None
Headless_Knight = None
Headless_Knight_Skill = None

Cat_Units = []  # 아군 유닛들을 관리할 리스트 생성
Enemy_Units = []  # 적군 유닛들을 관리할 리스트 생성

BGM = None


def enter():  # 게임 상태 ( 인게임 ) 에 들어올 때 초기화
    global Back_Ground  # 전역변수 선언
    Back_Ground = BackGround.BackGround()  # 생성한 전역변수로 BackGround 객체를 가리킴
    global BGM  # 전역변수 선언
    BGM = load_music('Resources/Musics/DefaultBattle.ogg')  # 생성한 전역변수에 음악 삽입
    BGM.set_volume(64)  # 음량
    BGM.repeat_play()  # 반복 재생
    global My_Castle, Enemy_Castle  # 전역변수 선언
    My_Castle = Castle.MyCastle()  # 생성한 전역변수로 MyCastle 객체를 가리킴
    Enemy_Castle = Castle.EnemyCastle()  # 생성한 전역변수로 EnemyCastle 객체를 가리킴
    global Basic_Cat, Tank_Cat, Axe_Cat, Gross_Cat, Cow_Cat, Bird_Cat, Fish_Cat, Lizard_Cat, Titan_Cat  # 전역변수 선언
    Basic_Cat = Cats.BasicCat()  # 생성한 전역변수로 BasicCat 객체를 가리킴
    Tank_Cat = Cats.TankCat()
    Axe_Cat = Cats.AxeCat()  # 생성한 전역변수로 AxeCat 객체를 가리킴
    Gross_Cat = Cats.GrossCat()
    Cow_Cat = Cats.CowCat()
    Bird_Cat = Cats.BirdCat()
    Fish_Cat = Cats.FishCat()
    Lizard_Cat = Cats.LizardCat()
    Titan_Cat = Cats.TitanCat()
    global Officer_Skeleton, Commander_Skeleton
    Officer_Skeleton = Enemies.OfficerSkeleton()
    Commander_Skeleton = Enemies.CommanderSkeleton()
    global Headless_Knight
    Headless_Knight = Enemies.HeadlessKnight()
    global Headless_Knight_Skill
    Headless_Knight_Skill = Enemies.HeadlessKnightSkill()


def exit():  # 게임 상태 ( 인게임 ) 에서 나갈 때 종료화
    global Back_Ground  # 전역변수임을 명시
    global Basic_Cat, Tank_Cat, Axe_Cat, Gross_Cat, Cow_Cat, Bird_Cat, Fish_Cat, Lizard_Cat, Titan_Cat  # 전역변수임을 명시
    global My_Castle, Enemy_Castle  # 전역변수임을 명시
    global Officer_Skeleton, Commander_Skeleton
    global Headless_Knight
    global Headless_Knight_Skill
    global BGM

    del Back_Ground  # 생성했던 객체 소멸
    del Basic_Cat, Tank_Cat, Axe_Cat, Gross_Cat, Cow_Cat, Bird_Cat, Fish_Cat, Lizard_Cat, Titan_Cat  # 생성했던 객체 소멸
    del My_Castle, Enemy_Castle  # 생성했던 객체 소멸
    del Officer_Skeleton,Commander_Skeleton
    del Headless_Knight
    del Headless_Knight_Skill
    del BGM


def update():
    for Cat in Cat_Units:  # 리스트에 속하는 모두의
        Cat.update()  # 프레임 업데이트
    for Enemy in Enemy_Units:
        Enemy.update()
    delay(0.05)  # 프레임 업데이트 속도


def draw():

    clear_canvas()  # 캔버스 지우기
    Back_Ground.draw()  # 배경화면 그리기
    My_Castle.draw()  # 아군 성 그리기
    My_Castle.draw_bb()
    Enemy_Castle.draw()  # 적군 성 그리기
    Enemy_Castle.draw_bb()
    for Cat in Cat_Units:  # 리스트에 속하는 모두를
        Cat.draw()  # 그리기
        Cat.draw_bb()

    for Enemy in Enemy_Units:
        Enemy.draw()
        Enemy.draw_bb()

    # 에러 일어나는 부분 ~
    for Cat in Cat_Units:
        if collide(Cat, Enemy_Castle):
            Cat.attack(Enemy_Castle)
        for Enemy in Enemy_Units:
            if collide(Cat, Enemy):
                Cat.attack(Enemy)

    for Enemy in Enemy_Units:
        for Cat in Cat_Units:
            if collide(Enemy, Cat):
                Enemy.attack(Cat)
    # ~ 에러 일어나는 부분
    for Cat in Cat_Units:
        if Cat.check_Hurt():
            Cat.Hurt()
    for Cat in Cat_Units:
        if Cat.check_die():
            Cat_Units.remove(Cat)
    update_canvas()  # 캔버스 업데이트


def handle_events():  # 입력신호를 관리하는 함수
    global Cat_Units  # 전역으로 선언된 리스트를 사용할 것을 명시
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            GameFrameWork.quit()  # 게임을 중단
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:  # ESC 키 입력 시
                GameFrameWork.quit()  # 게임을 중단
            elif event.key == SDLK_1:  # 1번 입력 시
                Cat_Units.append(Cats.BasicCat())  # 리스트에 기본 고양이 객체 추가
            elif event.key == SDLK_2:  # 2번 입력 시
                Cat_Units.append(Cats.TankCat())  # 리스트에 벽 고양이 객체 추가
            elif event.key == SDLK_3:  # 3번 입력 시
                Cat_Units.append(Cats.AxeCat())   # 리스트에 전사 고양이 객체 추가
            elif event.key == SDLK_4:  # 4번 입력 시
                Cat_Units.append(Cats.GrossCat())  # 각선미 고양이 객체 생성
            elif event.key == SDLK_5:  # 5번 입력 시
                Cat_Units.append(Cats.CowCat())  # 황소 고양이 객체 생성
            elif event.key == SDLK_6:  # 6번 입력 시
                Cat_Units.append(Cats.BirdCat())  # 물고기 고양이 객체 생성
            elif event.key == SDLK_7:  # 7번 입력 시
                Cat_Units.append(Cats.FishCat())  # 천사 고양이 객체 생성
            elif event.key == SDLK_8:  # 8번 입력 시
                Cat_Units.append(Cats.LizardCat())  # 도마뱀 고양이 객체 생성
            elif event.key == SDLK_9:  # 9번 입력 시
                Cat_Units.append(Cats.TitanCat())  # 거인 고양이 객체 생성
            elif event.key == SDLK_0:
                Enemy_Units.append(Enemies.SkeletonSoldier())
            elif event.key == SDLK_q:
                Enemy_Units.append(Enemies.OfficerSkeleton())
            elif event.key == SDLK_w:
                Enemy_Units.append(Enemies.CommanderSkeleton())
            elif event.key == SDLK_e:
                Enemy_Units.append(Enemies.HeadlessKnight())
            elif event.key == SDLK_r:
                Enemy_Units.append(Enemies.HeadlessKnightSkill())


def pause():
    pass


def resume():
    pass


def collide(a, b):
    left_a, bottom_a, right_a, top_a = a.get_size()
    left_b, bottom_b, right_b, top_b = b.get_size()

    if left_a > right_b: return False
    if right_a < left_b: return False
    if top_a < bottom_b: return False
    if bottom_a > top_b: return False

    return True





