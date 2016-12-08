# Python Module : 파이썬의 정의와 문장을 담고 있는 파일
#                그 자체로도 실행 가능하며, 다른 모듈에서 import해서 사용할 수도 있음.
#                import되면 그 자체가 하나의 객체가 됨.
#                Module의 사용 : import 모듈이름

from pico2d import *
#def collide(a, b):
    #left_a, bottom_a, right_a, top_a = a.get_size()
    #left_b, bottom_b, right_b, top_b = b.get_size()

    #if left_a > right_b: return False
    #if right_a < left_b: return False
    #if top_a < bottom_b: return False
    #if bottom_a > top_b: return False

    #return True


def collide_cat(cat, enemy):

    left_cat, bottom_cat, right_cat, top_cat = cat.get_attack_range()
    left_enemy, bottom_enemy, right_enemy, top_enemy = enemy.get_defense_size()

    if left_cat > right_enemy: return False
    if bottom_cat > top_enemy: return False

    return True


def collide_enemy(enemy, cat):
    #left_cat, bottom_cat, right_cat, top_cat = cat.get_size()  # 방어판정 바운딩 박스 사이즈
    #left_enemy, bottom_enemy, right_enemy, top_enemy = enemy.get_size()  # 공격판정 바운딩 박스 사이즈

    left_cat, bottom_cat, right_cat, top_cat = cat.get_defense_size()
    left_enemy, bottom_enemy, right_enemy, top_enemy = enemy.get_attack_range()
    if right_enemy < left_cat: return False
    if bottom_enemy > top_cat: return False

    return True


def get_frame_time():
    global current_time

    frame_time = get_time() - current_time
    current_time += frame_time

    return frame_time


