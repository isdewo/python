'''
파이썬 - 8 클래스
p. 28
__str__() 메소드
'''

class Human:
  def __init__(self, age, name):
    self.age = age
    self.name = name

  def __str__(self):
    return "이름 %s, 나이 %d"%(self.name, self.age)

kim = Human(29, "홍길동")
print(kim) # 객체 kim을 print하면 __str__ 메소드가 호출된다.