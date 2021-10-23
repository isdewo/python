'''
파이썬 - 8 클래스
p. 11
프라이빗 멤버(private member) & 퍼블릭 멤버(public member)
'''

class TestPrivate:
  def __init__(self):
    self.a = 100 # public 멤버
    self.__b = 200 # private 멤버

  def print_member(self):
    print(self.a)
    print(self.__b)

obj = TestPrivate()
obj.print_member()
100
200
print(obj.a)
print(obj.__b) # b는 private 멤버이므로 에러가 발생한다.