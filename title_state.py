import GameFrameWork
import scene_stage1
from pico2d import*

name = "TitleState"
image = None


def enter():
    global image

    image = load_image("Resources/Titleimage.jpg")


def exit():
    global image
    del(image)


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            GameFrameWork.quit()
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_SPACE:
                GameFrameWork.change_state(scene_stage1)
            elif event.key == SDLK_ESCAPE:
                GameFrameWork.quit()


def draw():
    clear_canvas()
    image.draw(513, 341)
    update_canvas()


def update():
    pass


def pause():
    pass


def resume():
    pass