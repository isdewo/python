'''
파이썬 - 8 클래스
p. 26
오버라이딩(overriding)
'''

class A:
  def print_str(self):
    print("A")

class B(A):
  def print_str(self):
    print("B")

A().print_str() # A객체를 만들면서 print_str 호출
B().print_str() # B객체를 만들면서 print_str 호출