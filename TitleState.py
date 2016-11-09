import GameFrameWork
import Scene_Stage1
from pico2d import*

name = "TitleState"
image = None
x = 0
y = 0


class SelectedButton:
    def __init__(self):
        self.image = load_image("Resources/Selected.png")
        self.x, self.y = 640, -200
        self.width, self.height = 215, 40

    def get_size(self):
        return (self.x-self.width), (self.y-self.height), (self.x+self.width), (self.y+self.height)

    def draw(self):
        self.image.draw(self.x, self.y)


def enter():
    global image, bt, x, y

    image = load_image("Resources/Titleimage.png")
    bt = SelectedButton()



def exit():
    global image, bt
    del(image)
    del(bt)


def handle_events():
    global bt
    global x, y

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            GameFrameWork.quit()
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_SPACE:
                GameFrameWork.change_state(Scene_Stage1)
            elif event.key == SDLK_ESCAPE:
                GameFrameWork.quit()
        elif event.type == SDL_MOUSEMOTION:  # 마우스를 움직였을 때
            x, y = event.x, 720 - event.y
            # x640/y287  215/40
            if (x > 640-215) & (x < 640+215) & (y > 287-40) & (y < 287+40):
                bt.y = 287
            else:
                bt.y = -200
        elif event.type == SDL_MOUSEBUTTONDOWN:
            if bt.y == 287:
                GameFrameWork.change_state(Scene_Stage1)


def draw():
    clear_canvas()
    image.draw(640, 360)
    bt.draw()
    update_canvas()


def update():
    pass


def pause():
    pass


def resume():
    pass
