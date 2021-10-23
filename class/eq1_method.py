'''
파이썬 - 8 클래스
p. 16
특별한 메소드: 연산자 메소드
'''

class Human:
  def __init__(self, age, name):
    self.age = age
    self.name = name

  # 나이와 이름이 같은지 판단
  def __eq__(self, other):
    return self.age == other.age and self.name == other.name

kim = Human(29, "홍길동")
sang = Human(29, "홍길동")
moon = Human(30, "이순신")
print(kim == sang)
print(kim == moon)
