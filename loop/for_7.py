# break문
coffee = 10
money = 300
while money:
  print("커피가 나옵니다")
  coffee = coffee - 1
  print("남은 커피의 양은 %d개 입니다." %coffee)
  if coffee == 0:
    print("커피 재고 소진. 판매중단.")
    break