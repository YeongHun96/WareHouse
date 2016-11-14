# Python Module : 파이썬의 정의와 문장을 담고 있는 파일
#                그 자체로도 실행 가능하며, 다른 모듈에서 import해서 사용할 수도 있음.
#                import되면 그 자체가 하나의 객체가 됨.
#                Module의 사용 : import 모듈이름
from pico2d import *


class BackGround:  # 배경 클래스

    def __init__(self):  # 초기화
        self.image = load_image('Resources/BackGround.png')  # 이미지 불러오기

    def draw(self):
        self.image.draw(640, 360)  # 불러온 이미지를 후면 버퍼의 좌표 (x,y)의 위치에 삽입
