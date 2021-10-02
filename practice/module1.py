# 1. 원의 반지름을 사용자 입력으로 받아 원의 면적을 출력하는 프로그램을 작성하시오.

import math
r = int(input("반지름을 입력하세요: "))
area = r * r * math.pi

print("반지름이 {0}인 원의 면적은 {1}입니다.".format(r, area))