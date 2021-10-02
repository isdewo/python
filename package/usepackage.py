'''
파이썬 - 5 모듈 만들기
p. 13 ~ 14
패키지 만들기
'''
import sys
sys.path.append("C:\mypackage")
'''
import mypack.calc.myadd
mypack.calc.myadd.add(1, 2)

import mypack.report.myreport
mypack.report.myreport.outreport()
'''
from mypack.calc import myadd
myadd.add(1, 2)

from mypack.calc.myadd import add
add(1, 2)
