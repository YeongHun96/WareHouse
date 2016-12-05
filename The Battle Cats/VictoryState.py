import GameFrameWork
import TitleState
from pico2d import*

name = "VictoryState"
image = None
BGM = None


def enter():
    global image
    global BGM  # 전역변수 선언
    BGM = load_music('Resources/Musics/Victory.ogg')  # 생성한 전역변수에 음악 삽입
    BGM.set_volume(50)  # 음량
    BGM.play(1)
    image = load_image("Resources/VictoryState2.png")


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
                GameFrameWork.change_state(TitleState)
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
