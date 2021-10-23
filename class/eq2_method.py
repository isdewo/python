'''
파이썬 - 8 클래스
p. 17
연습문제1
'''

class Human:
  def __init__(self, age, name):
    self.age = age
    self.name = name

  # 이름이 같은지 판단
  def __eq__(self, other):
    return self.name == other.name

kim = Human(28, "홍길동")
sang = Human(29, "홍길동")
moon = Human(30, "이순신")
print(kim == sang)
print(kim == moon)

