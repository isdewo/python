'''
파이썬 - 8 클래스
p. 18
클래스 메소드(class method)
'''

class CalCounter:
  object_count = 0 # 객체 개수 생성
  def __init__(self):
    CalCounter.object_count += 1

  @classmethod
  def print_objectcount(cls): # cls: 클래스 자신을 매개변수로 받음
    print(cls.object_count)

a = CalCounter()
CalCounter.print_objectcount() # 1
b = CalCounter()
CalCounter.print_objectcount() # 2