'''
파이썬 - 8 클래스
실습6
__str__() 메소드
'''

class Character:
  def __init__(self, name, role):
    self.name = name
    self.role = role

  def __str__(self):
    return "내 이름은 %s. %s이죠."%(self.name, self.role)

conan = Character("코난", "탐정")
thomas = Character("토마스", "기관차")
tayo = Character("타요", "꼬마버스")
print(conan) # 객체를 print하면 __str__ 메소드가 호출된다.
print(thomas)
print(tayo)

