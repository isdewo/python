'''
파이썬 - 8 클래스
p. 13
클래스 멤버 - 연습문제
'''

class CalCounter:
  count = 0 # 클래스 멤버
  def __init__(self):
    CalCounter.count += 1 # 클래스 멤버인 count의 값을 접근

  def print_count(self):
    print(self.count)

a = CalCounter()
a.print_count() # 1
b = CalCounter()
b.print_count() # 2