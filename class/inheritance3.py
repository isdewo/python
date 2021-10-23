'''
파이썬 - 8 클래스
p. 23
상속(inheritance) - super
'''

class BaseA:
  def __init__(self):
    print("BaseA.__init__()")

class B(BaseA):
  def __init__(self):
    print("B.__init__()")
    super().__init__()

b = B()