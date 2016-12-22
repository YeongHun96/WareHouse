# Python Module : 파이썬의 정의와 문장을 담고 있는 파일
#                그 자체로도 실행 가능하며, 다른 모듈에서 import해서 사용할 수도 있음.
#                import되면 그 자체가 하나의 객체가 됨.
#                Module의 사용 : import 모듈이름

import GameFrameWork
import TitleState
from pico2d import*

name = "DefeatState"
image = None
BGM = None


def enter():
    global image
    global BGM  # 전역변수 선언
    BGM = load_music('Resources/Musics/Defeat.ogg')  # 생성한 전역변수에 음악 삽입
    BGM.set_volume(50)  # 음량
    BGM.play(1)
    image = load_image("Resources/DefeatState2.png")


def exit():
    global image
    global BGM

    del image
    del BGM


def handle_events(frame_time):

    events = get_events()

    for event in events:
        if event.type == SDL_QUIT:
            GameFrameWork.quit()
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_SPACE:
                GameFrameWork.quit()
            elif event.key == SDLK_ESCAPE:
                GameFrameWork.quit()


def draw():
    clear_canvas()
    image.draw(640, 360)
    update_canvas()


def update(frame_time):
    pass


def pause():
    pass


def resume():
    pass
