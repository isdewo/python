'''
파이썬 - 5 모듈 만들기
p. 9
메인모듈과 하위모듈
'''
# 모듈이 최상위 수준에서 실행될 때 __name__의 값이 "__main__"으로 지정됨
# 다른 모듈에서 import하여 실행될 떄는 __name__의 값이 자신 이름으로 지정됨
print(__name__)