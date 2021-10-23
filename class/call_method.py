'''
파이썬 - 8 클래스
p. 29
__call__() 메소드
'''

class A:
  def __init__(self):
    print("A")

  def __call__(self):
    print("__call__()")

b = A() # 객체 생성 -> __init__호출 -> A 출력
b() # __call__() 호출