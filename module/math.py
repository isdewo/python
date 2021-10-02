'''
파이썬 -4 모듈과 패키지
p.4 ~ 6

import 선언 방법

import math
import math as m
from math import sqrt
from math import sqrt, pow
from math import *
from math import sqrt as sq
'''

import math
print(math.sqrt(4))

import math as m
print(m.sqrt(4))

from math import sqrt
print(sqrt(4))

from math import sqrt, pow
print(sqrt(4), pow(2, 3))

from math import sqrt as sq, pow as pp
print(sq(4), pp(2, 3))
