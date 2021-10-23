'''
파이썬 - 8 클래스
p. 7
메소드 호출하기
'''

class Player:
  def __init__(self, name, height):
    self.number = 100
    self.name = name
    self.height = height

  def print_info(self):
    print(self.number)
    print(self.name)
    print(self.height)

a = Player("gildong", "178")
a.print_info()