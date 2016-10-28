# 인게임 상태를 관리하는 파일

from pico2d import*

import BackGround
import Castle
import Cats
import GameFrameWork

running = True
background = None

Cat_Units = []  # 아군 유닛들을 관리할 리스트 생성


def enter():  # 게임 상태 ( 인게임 ) 에 들어올 때 초기화
    global Back_Ground  # 전역변수 선언
    Back_Ground = BackGround.BackGround()  # 생성한 전역변수로 BackGround 객체를 가리킴
    global My_Castle, Enemy_Castle  # 전역변수 선언
    My_Castle = Castle.MyCastle()  # 생성한 전역변수로 MyCastle 객체를 가리킴
    Enemy_Castle = Castle.EnemyCastle()  # 생성한 전역변수로 EnemyCastle 객체를 가리킴
    global Basic_Cat, Axe_Cat  # 전역변수 선언
    Basic_Cat = Cats.BasicCat()  # 생성한 전역변수로 BasicCat 객체를 가리킴
    Axe_Cat = Cats.AxeCat()  # 생성한 전역변수로 AxeCat 객체를 가리킴


def exit():  # 게임 상태 ( 인게임 ) 에서 나갈 때 종료화
    global Back_Ground  # 전역변수임을 명시
    global Basic_Cat, Axe_Cat  # 전역변수임을 명시
    global My_Castle, Enemy_Castle  # 전역변수임을 명시

    del Back_Ground  # 생성했던 객체 소멸
    del Basic_Cat, Axe_Cat  # 생성했던 객체 소멸
    del My_Castle, Enemy_Castle  # 생성했던 객체 소멸


def update():
    for Cat in Cat_Units:  # 리스트에 속하는 모두의
        Cat.update()  # 프레임 업데이트
    delay(0.05)  # 프레임 업데이트 속도


def draw():
    clear_canvas()  # 캔버스 지우기
    Back_Ground.draw()  # 배경화면 그리기
    My_Castle.draw()  # 아군 성 그리기
    Enemy_Castle.draw()  # 적군 성 그리기
    for Cat in Cat_Units:  # 리스트에 속하는 모두를
        Cat.draw()  # 그리기
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
                pass
            elif event.key == SDLK_2:  # 2번 입력 시
                pass    # 리스트에 벽 고양이 객체 추가
            elif event.key == SDLK_3:
                Cat_Units.append(Cats.AxeCat())   # 리스트에 전사 고양이 객체 추가
                pass
            elif event.key == SDLK_4:
                pass
                # 각선미 고양이 객체 생성
            elif event.key == SDLK_5:
                pass
                # 황소 고양이 객체 생성
            elif event.key == SDLK_6:
                pass
                # 물고기 고양이 객체 생성
            elif event.key == SDLK_7:
                pass
                # 천사 고양이 객체 생성
            elif event.key == SDLK_8:
                pass
                # 도마뱀 고양이 객체 생성
            elif event.key == SDLK_9:
                pass
                # 거인 고양이 객체 생성


def pause():
    pass

def resume():
    pass


