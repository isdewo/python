'''
파이썬 - 8 클래스
실습6 - 사칙연산
'''

class Add:
  def add(self, a, b):
    return a + b

class Sub:
  def sub(self, a, b):
    return a - b

class Multiply:
  def multiply(self, a, b):
    return a * b

class Devide:
  def devide(self, a, b):
    return a / b

class Calculator(Add, Sub, Multiply, Devide): # 다중 상속
  pass

c = Calculator()
print(c.add(1, 2)) # 3
print(c.sub(5, 2)) # 3
print(c.multiply(3, 1)) # 3
print(c.devide(9, 3)) # 3
