import GameFrameWork
import TitleState
from pico2d import*

name = "StartState"
image = None
logo_time = 0.0  # 변수 선언


def enter():  # 게임 상태에 들어올 때 초기화
    global image
    open_canvas(1280, 720)  # (x, y)의 크기로 캔버스 생성
    image = load_image('Resources/KPU_Credit.png')  # 이미지 불러오기


def exit():  # 게임 상태에서 나갈 때 종료화
    global image
    del image
    close_canvas()


def update():
    global logo_time  # 전역변수 선언

    if logo_time > 1.0:  # StartState 화면이 1초 지속되면
        logo_time = 0  # 시간을 0으로 만들고
        GameFrameWork.push_state(TitleState)  # 게임 상태를 TitleState로 전환. 이전 게임 상태는 남아있음.
    delay(0.01)
    logo_time += 0.01


def draw():
    global image
    clear_canvas()  # 캔버스 지우고
    image.draw(640, 360)  # 이미지를 640, 360의 위치에 삽입
    update_canvas()  # 캔버스를 업데이트 함


def handle_events():
    events = get_events()
    pass


def pause():  # 다른 상태로 잠깐 이동
    pass


def resume():  # 현재 상태로 복귀
    pass
