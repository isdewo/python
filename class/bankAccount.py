'''
파이썬 - 8 클래스
p. 8 ~ 9
연습문제
'''

class BankAccount:
  # 초기화
  def __init__(self, balance, name, number):
    self.balance = balance # 잔액(int)
    self.name = name # 소유자 이름(string)
    self.number = number # 계좌번호(int)

  # 출금
  def withdraw(self):
    money = int(input("출력할 액수를 입력하시오: "))
    if self.balance >= money:
      self.balance -= money
      ("출금이 완료되었습니다.")
      return self.balance
    else:
      print("잔액이 부족합니다.")

  # 입금
  def deposit(self):
    money = int(input("입금할 금액을 입력하시오: "))
    self.balance += money
    print("입금이 완료되었습니다.")
    return self.balance

  # 계좌내역
  def print_account(self):
    print(self.name + "의 계좌")
    print("계좌번호: ", str(self.number))
    print("현재 잔액은 " + str(self.balance) + " 입니다.")

a1 = BankAccount(10000, "홍길동", 123456)
a1.print_account()
a1.deposit()
a1.print_account()
# a1.withdraw()
# a1.print_account()