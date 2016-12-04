# Python Module : 파이썬의 정의와 문장을 담고 있는 파일
#                그 자체로도 실행 가능하며, 다른 모듈에서 import해서 사용할 수도 있음.
#                import되면 그 자체가 하나의 객체가 됨.
#                Module의 사용 : import 모듈이름

import GameFrameWork
import Scene_Stage1
from pico2d import*

name = "DefeatState"
image = None
BGM = None


def enter():
    global image
    global BGM  # 전역변수 선언
    BGM = load_music('Resources/Musics/TitleTheme.ogg')  # 생성한 전역변수에 음악 삽입
    BGM.set_volume(0)  # 음량
    BGM.repeat_play()  # 반복 재생
    image = load_image("Resources/DefeatState.png")


def exit():
    global image
    global BGM

    del image
    del BGM


def handle_events():

    events = get_events()

    for event in events:
        if event.type == SDL_QUIT:
            GameFrameWork.quit()
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_SPACE:
                GameFrameWork.change_state(Scene_Stage1)
            elif event.key == SDLK_ESCAPE:
                GameFrameWork.quit()


def draw():
    clear_canvas()
    image.draw(640, 360)
    update_canvas()


def update():
    pass


def pause():
    pass


def resume():
    pass
