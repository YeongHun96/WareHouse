import GameFrameWork
import TitleState
from pico2d import*

# Module의 이름을 가지게 됨.
# 하지만 Module을 import하지 않고 직접 실행하는 경우 "__main__"이라는 문자열값을 갖게 되어,
# 현재 Module이 단독적으로 실행되는 상황을 구분함.

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


def update(frame_time):
    global logo_time  # 전역변수 선언

    if logo_time > 1.0:  # StartState 화면이 1초 지속되면
        logo_time = 0  # 시간을 0으로 만들고
        GameFrameWork.push_state(TitleState)  # 게임 상태를 TitleState로 전환. 이전 게임 상태는 남아있음.
    logo_time += 0.01


def draw():
    global image
    clear_canvas()  # 캔버스 지우고
    image.draw(640, 360)  # 이미지를 640, 360의 위치에 삽입
    update_canvas()  # 캔버스를 업데이트 함


def handle_events(frame_time):
    events = get_events()
    pass


def pause():  # 다른 상태로 잠깐 이동
    pass


def resume():  # 현재 상태로 복귀
    pass


def identify():
    print("이 함수는 단독으로 모듈을 실행할 경우에만 실행됩니다.")

    if __name__ == '__main__':
        identify()

# run(state): # state를 첫 상태로 게임을 시작함.
# change_state(state):  # 게임 상태를 state로 바꿈. 이전 상태를 완전히 나옴.
# push_state(state):  # 게임 상태를 state로 변화. 이전 상태는 남아있음.
# pop_state(): 이전 게임 상태로 복귀
# quit(): 게임을 중단
