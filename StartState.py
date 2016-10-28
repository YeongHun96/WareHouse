import GameFrameWork
import title_state
from pico2d import*

name = "StartState"
image = None
logo_time = 0.0

array = []


def enter():  # 게임 상태에 들어올 때 초기화
    global image
    open_canvas(1026, 682)  # (x, y)의 크기로 캔버스 생성
    image = load_image('Resources/kpu_credit.png')  # 이미지 불러오기


def exit():  # 게임 상태에서 나갈 때 종료화
    global image
    del image
    close_canvas()


def update():
    global logo_time

    if(logo_time > 1.0):
        logo_time = 0
        #game_framework.quit()  게임을 중단
        GameFrameWork.push_state(title_state)  # 게임 상태를 state로 변화. 이전 게임 상태는 남아있음.
    delay(0.01)
    logo_time += 0.01

def draw():
    global image
    clear_canvas()
    image.draw(513, 341)
    update_canvas()

def handle_events():
    events = get_events()
    pass

def pause():  # 다른 상태로 잠깐 이동
    pass

def resume():  # 현재 상태로 복귀
    pass
