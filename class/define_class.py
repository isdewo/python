'''
파이썬 - 8 클래스
p. 5
클래스 정의하기
'''

class Human:
  # 초기화
  def __init__(self, age, name):
    self.age = age
    self.name = name

  def intro(self):
    print(str(self.age) + "살 " + self.name + "입니다")

# 객체 생성
kim = Human(29, "김유신")
kim.intro()

hong = Human(25, "홍길동")
hong.intro()