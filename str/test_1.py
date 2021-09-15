# 'a:b:c:d'의 문자열을 replace 함수를 사용하여 'a#b#c#d'로 바꾸어 출력하라
str = 'a:b:c:d'
print('str = {}'.format(str))
re = str.replace(':', '#')
print("str.replace(':', '#') = {}".format(re))