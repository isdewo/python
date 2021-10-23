'''
파이썬 - 8 클래스
p. 25
다중상속(inheritance)
'''

class Add:
  def add(self, a, b):
    return a + b

class Multiply:
  def multiply(self, a, b):
    return a * b

class Calculator(Add, Multiply): # 다중 상속
  def sub(self, a, b):
    return a - b

c = Calculator()
print(c.add(1, 2))
print(c.multiply(2, 10))

