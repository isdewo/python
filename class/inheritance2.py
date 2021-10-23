'''
파이썬 - 8 클래스
p. 22
상속(inheritance)
'''

class Add:
  def add(self, a, b):
    return a + b

class Calculator(Add):
  def sub(self, a, b):
    return a - b

c = Calculator()
print(c.add(1, 2))
print(c.sub(2, 1))