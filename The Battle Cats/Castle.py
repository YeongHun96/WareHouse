# Python Module : 파이썬의 정의와 문장을 담고 있는 파일
#                그 자체로도 실행 가능하며, 다른 모듈에서 import해서 사용할 수도 있음.
#                import되면 그 자체가 하나의 객체가 됨.
#                Module의 사용 : import 모듈이름

from pico2d import *


class MyCastle:  # 우리 팀의 성

    def __init__(self):  # 초기화
        self.x, self.y = 1200, 300  # 객체의 초기 위치
        self.image = load_image("Resources/MyCastle.png")  # 성의 이미지 불러오기
        self.Health = 1000000  # 성의 체력

    def draw(self):
        self.image.draw(self.x, self.y)  # 이미지를 후면 버퍼의 좌표 (x,y)위치에 삽입

    def update(self):
        if self.Health < 0:  # 성의 체력이 0 이하가 되면
            self.x, self.y = -1000, -1000  # 성의 위치를 옮김 ( 임시 )

    def get_size(self):  # 충돌체크를 위한 이미지 크기 반환
        return self.x - 60, self.y - 123, self.x + 60,  self.y + 127
        # 왼쪽: 65, 아래쪽: 123, 오른쪽: 60, 위쪽: 127

    def draw_bb(self):  # 충돌범위를 나타내는 박스 그리기
        draw_rectangle(*self.get_size())


class EnemyCastle:  # 적 팀의 성

    def __init__(self):  # 초기화
        self.x, self.y = 60, 270  # 객체의 초기 위치
        self.image = load_image("Resources/EnemyCastle.png")  # 성의 이미지 불러오기
        self.Health = 1000  # 성의 체력

    def draw(self):
        self.image.draw(self.x, self.y)  # 이미지를 후면버퍼의 x, y 위치에 그림

    def update(self):
        if self.Health < 0:  # 성의 체력이 0 이하가 되면
            self.x, self.y = -1000, -1000 # 성의 위치를 옮김 ( 임시 )

    def get_size(self):  # 충돌체크를 위한 이미지 크기 반환
        return self.x - 60, self.y - 100,self.x + 60,  self.y + 100
        # 왼쪽: 90, 아래쪽: 100, 오른쪽: 60, 위쪽: 100

    def draw_bb(self):  # 충돌범위를 나타내는 박스 그리기
        draw_rectangle(*self.get_size())
