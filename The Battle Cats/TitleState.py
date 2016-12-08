import GameFrameWork
import Scene_Stage1
from pico2d import*

name = "TitleState"
image = None
BGM = None
x = 0
y = 0


class SelectedButton:  # 버튼이 선택됐을때의 이미지 클래스
    def __init__(self):
        self.image = load_image("Resources/Selected.png")  # 이미지 로드
        self.x, self.y = 640, -200  # 초기위치
        self.width, self.height = 215, 40  # 이미지 크기

    def get_size(self):
        return (self.x-self.width), (self.y-self.height), (self.x+self.width), (self.y+self.height)  # 이미지 크기 반환

    def draw(self):
        self.image.draw(self.x, self.y)  # 이미지 출력


def enter():
    global image, bt, x, y
    global BGM  # 전역변수 선언
    BGM = load_music('Resources/Musics/TitleTheme.ogg')  # 생성한 전역변수에 음악 삽입
    BGM.set_volume(50)  # 음량
    BGM.repeat_play()  # 반복 재생
    image = load_image("Resources/TitleImage.png")
    bt = SelectedButton()


def exit():
    global image, bt
    global BGM

    del image
    del bt
    del BGM


def handle_events(frame_time):
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


def update(frame_time):
    pass


def pause():
    pass


def resume():
    pass
