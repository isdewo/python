'''
파이썬 - 8 클래스
p. 21
상속(inheritance)
'''

class BaseA: # class 기반 클래스
  def print_string(self):
    print("This is base")

class DerivedA(BaseA): # class 파생 클래스(기반 클래스)
  pass

a = BaseA()
a.print_string()

b = DerivedA()
b.print_string()