'''
파이썬 - 8 클래스
p. 17
연습문제2
'''

class Human:
  def __init__(self, age, name):
    self.age = age
    self.name = name

  # 나이와 이름이 같은지 판단
  def __eq__(self, other):
    return self.age == other.age and self.name == other.name

  # self의 나이가 other의 나이보다 작거나 같은지 판단
  def __le__(self, other):
    return self.age <= other.age

kim = Human(29, "홍길동")
sang = Human(29, "홍길동")
moon = Human(30, "이순신")
Lee = Human(27, "이순신")
# print(kim == sang)
# print(kim == moon)
print(kim.__eq__(sang)) # True
print(kim.__eq__(moon)) # False
print(kim.__le__(sang)) # True
print(kim.__le__(moon)) # True
print(kim.__le__(Lee)) # False