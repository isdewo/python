'''
파이썬 - 8 클래스
p. 12
클래스 멤버
'''

class MyClass:
  var = "안녕하세요!!" # 클래스 멤버

  def sayHello(self):
    msg1 = "안녕"
    self.msg2 = "Hi"
    print(msg1)
    print(self.var) # 객체의 var를 새로 정의하여 사용

obj = MyClass()
print(obj.var)  # "안녕하세요!!"
obj.sayHello()  # "안녕" "안녕하세요!!"
print(MyClass.var)  # "안녕하세요!!"