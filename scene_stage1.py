import gameframework
from pico2d import*

import BackGround
import Cats
import Castle

running = True
background = None

cats = []
warrior_cats = []



def enter():
    global background
    background = BackGround.BackGround()
    global castle
    global castle2
    castle = Castle.OurCastle()
    castle2 = Castle.EnemyCastle()

def exit():
    global background
    global cats
    global warrior_cats
    global castle
    global castle2

    del (background)
    del (cats)
    del (warrior_cats)
    del (castle)
    del (castle2)


def update():
    for cat in cats:
        cat.update()
    delay(0.05)
    pass

def draw():
    clear_canvas()
    background.draw()
    castle.draw()
    castle2.draw()
    for cat in cats:
        cat.draw()
    update_canvas()

def handle_events():
    global cats
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            gameframework.quit()
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                gameframework.quit()
            elif event.key == SDLK_1:
                cats.append(Cats.BasicCat())
                pass
                # 기본 고양이 객체 생성
            elif event.key == SDLK_2:
                cats.append(Cats.Warrior_Cat())
                pass
                # 벽 고양이 객체 생성
            elif event.key == SDLK_3:
                pass
                # 전사 고양이 객체 생성
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
"""
눈물 발사 간격
이 전에 입력이 들어오면
저장
일정 간격 이후에 발사?
"""

def pause():
    pass

def resume():
    pass



