'''
파이썬 - 6 예외처리
p.11
사용자가 정의한 예외 발생
'''

# 사용자가 정의한 예외 발생(Exception) 사용
text = input()
if text.isdigit() == False:
  raise Exception("입력 문자열이 숫자가 아닙니다")

text = input()
if text.isdigit() == False:
  try:
    raise Exception("입력 문자열이 숫자가 아닙니다")
  except Exception:
    print("예외가 일어났습니다")