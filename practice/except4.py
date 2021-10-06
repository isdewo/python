# 사용자 정의 예외(Exception)를 사용하여
# 예외처리 예제 프로그램을 작성하시오.


str = input("오늘은 파이썬 공부를 해볼까요?? (O 또는 X로 답하세요): ")
if str != "O":
  raise Exception("공부하지 않겠다고요?????????")
else:
  print("좋은 생각입니다!!")