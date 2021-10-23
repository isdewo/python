'''
파이썬 - 8 클래스
실습6
__call__() 메소드
'''

class Lamp:
  call_genie = 0
  def __init__(self):
    print("주인님~ 소원이 무엇인가요???????????????????")

  def __call__(self):
    Lamp.call_genie += 1
    print("주인님 " + str(Lamp.call_genie) + "번 부르셨습니다~~")



Genie = Lamp() # 객체 생성
Genie() # __call__() 호출
Genie()
Genie()

