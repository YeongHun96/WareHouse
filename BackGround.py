# Python Module : 파이썬의 정의와 문장을 담고 있는 파일
#                 그 자체로도 실행 가능하며, 다른 모듈에서 Import 해서 사용할 수도 있음
#                 Import 되면, 그 자체가 하나의 객체가 됨.
from pico2d import *


class BackGround:

    def __init__(self):
        self.image = load_image('Resources/BackGround.png')  # 이미지 불러오기

    def draw(self):
        self.image.draw(640, 360)  # 불러온 이미지를 좌표 (x,y)의 위치에 삽입
