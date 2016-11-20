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

running = True
Back_Ground = None
My_Castle, Enemy_Castle = None, None
Basic_Cat, Tank_Cat, Axe_Cat, Gross_Cat, Cow_Cat, Bird_Cat, UFO_Cat, Fish_Cat, Lizard_Cat, Titan_Cat = None, None, None, None, None, None, None, None, None, None
Skele_Dog, Mummy_Dog, Officer_Skeleton, Commander_Skeleton = None, None, None, None
Headless_Knight = None
Headless_Knight_Skill = None
Lizard_Cat_Skill, UFO_Cat_SKill = None, None
Come_Headless = True

Cat_Units = []  # 아군 유닛들을 관리할 리스트 생성
Enemy_Units = []  # 적군 유닛들을 관리할 리스트 생성
Cat_Skills = []
Enemy_Skills = []  # 스킬들

BGM = None


def enter():  # 게임 상태 ( 인게임 ) 에 들어올 때 초기화
    global Back_Ground  # 전역변수 선언
    Back_Ground = BackGround.BackGround()  # 생성한 전역변수로 BackGround 객체를 가리킴
    global BGM  # 전역변수 선언
    BGM = load_music('Resources/Musics/DefaultBattle.ogg')  # 생성한 전역변수에 음악 삽입
    BGM.set_volume(0)  # 음량
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


def exit():  # 게임 상태 ( 인게임 ) 에서 나갈 때 종료화
    global Back_Ground  # 전역변수임을 명시
    global Basic_Cat, Tank_Cat, Axe_Cat, Gross_Cat, Cow_Cat, Bird_Cat, UFO_Cat, Fish_Cat, Lizard_Cat, Titan_Cat  # 전역변수임을 명시
    global My_Castle, Enemy_Castle  # 전역변수임을 명시
    global Skele_Dog, Mummy_Dog, Officer_Skeleton, Commander_Skeleton
    global Headless_Knight
    global Headless_Knight_Skill
    global BGM
    global Lizard_Cat_Skill, UFO_Cat_SKill
    global Come_Headless

    del Back_Ground  # 생성했던 객체 소멸
    del Basic_Cat, Tank_Cat, Axe_Cat, Gross_Cat, Cow_Cat, Bird_Cat, UFO_Cat, Fish_Cat, Lizard_Cat, Titan_Cat  # 생성했던 객체 소멸
    del My_Castle, Enemy_Castle  # 생성했던 객체 소멸
    del Skele_Dog, Mummy_Dog, Officer_Skeleton, Commander_Skeleton
    del Headless_Knight
    del Headless_Knight_Skill
    del BGM
    del Lizard_Cat_Skill, UFO_Cat_SKill
    del Come_Headless


def update():  # 업데이트
    global My_Castle
    global Enemy_Castle
    global Come_Headless
    for Cat in Cat_Units:  # 리스트에 속하는 아군 유닛
        Cat.update()  # 업데이트
    for Enemy in Enemy_Units:  # 리스트에 속하는 적군 유닛
        Enemy.update()  # 업데이트
    My_Castle.update()
    Enemy_Castle.update()
    delay(0.05)  # 프레임 업데이트 속도

    for Cat in Cat_Units:  # 리스트에 속하는 아군 유닛들
        for Enemy in Enemy_Units:  # 리스트에 속하는 적군 유닛들에 대해
            if Functions.collide(Enemy, Cat) is True:
                Enemy.attack(Cat)
            elif Functions.collide(Cat, Enemy and Enemy_Castle):
                Cat.attack(Enemy_Castle)
            else:
                Enemy.walk()
        if Functions.collide(Cat, Enemy_Castle) is True:  # 아군 유닛과 적군 성 간 충돌 있으면
            Cat.attack(Enemy_Castle)  # 적군 성 공격

    for Enemy in Enemy_Units:
        for Cat in Cat_Units:
            if Functions.collide(Cat, Enemy) is True:  # 적군 유닛과 아군 유닛간 충돌 있으면
                Cat.attack(Enemy)  # 적군 -> 아군 공격
            else:
                Cat.walk()
        if Functions.collide(Enemy, My_Castle) is True:
            Enemy.attack(My_Castle)

    for Cat in Cat_Units:
        if Functions.die_check(Cat) is True:
            Cat.state = Cat.HURT

    for Enemy in Enemy_Units:
        if Functions.die_check(Enemy) is True:
            Enemy.state = Enemy.DIE

    for CatSkill in Cat_Skills:
        CatSkill.update()

    for CatSkill in Cat_Skills:
        if Functions.collide(CatSkill, Enemy_Castle) is True:
            CatSkill.attack(Enemy_Castle)

    for EnemySkill in Enemy_Skills:
        EnemySkill.update()

    for EnemySkill in Enemy_Skills:
        if Functions.collide(EnemySkill, My_Castle) is True:
            EnemySkill.attack(My_Castle)


def draw():
    global My_Castle
    global Enemy_Castle
    global Back_Ground
    clear_canvas()  # 캔버스 지우기
    Back_Ground.draw()  # 배경화면 그리기
    My_Castle.draw()  # 아군 성 그리기
    My_Castle.draw_bb()  # 아군 성의 충돌범위 그리기
    Enemy_Castle.draw()  # 적군 성 그리기
    Enemy_Castle.draw_bb()  # 적군 성의 충돌범위 그리기
    for Cat in Cat_Units:  # 리스트에 속하는 아군 유닛 모두를
        Cat.draw()  # 그리기
        Cat.draw_bb()  # 충돌범위 그리기

    for Enemy in Enemy_Units:  # 리스트에 속하는 적군 유닛 모두를
        Enemy.draw()  # 그리기
        Enemy.draw_bb()  # 충돌범위 그리기

    for CatSkill in Cat_Skills:
        CatSkill.draw()
        CatSkill.draw_bb()

    for EnemySkill in Enemy_Skills:
        EnemySkill.draw()
        EnemySkill.draw_bb()

    update_canvas()  # 캔버스 업데이트


def handle_events():  # 입력신호를 관리하는 함수
    global Cat_Units  # 전역으로 선언된 리스트를 사용할 것을 명시
    global Enemy_Units
    global BGM
    global Back_Ground
    global Come_Headless
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
                Cat_Units.append(Cats.UFOCat())  # 물고기 고양이 객체 생성
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
                Come_Headless = False
                Back_Ground.image = load_image('Resources/BackGround_Final.png')
                for Enemy in Enemy_Units:
                    Enemy.state = Enemy.DIE
                Enemy_Units.append(Enemies.HeadlessKnight())
                del BGM
                BGM = load_music('Resources/Musics/CarminaBurana.ogg')  # 생성한 전역변수에 음악 삽입
                BGM.set_volume(100)  # 음량
                BGM.repeat_play()  # 반복 재생
            elif event.key == SDLK_r:
                Enemy_Units.append(Enemies.MummyDog())
            elif event.key == SDLK_t:
                Enemy_Units.append(Enemies.SkeleDog())


def pause():
    pass


def resume():
    pass





