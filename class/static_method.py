'''
파이썬 - 8 클래스
p. 19
정적 메소드(static method)
'''

class Calculator:
  @staticmethod
  def plus(a, b):
    return a + b

  @staticmethod
  def minus(a, b):
    return a - b

result = Calculator.plus(3, 5) # 클래스 이름으로 호출
print(result)
cal1 = Calculator()
print(cal1.plus(3, 5)) # 객체의 메소드로 호출