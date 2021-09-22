# 가변 매개변수(arbitary argument)
# **를 사용하면 딕셔너리 타입의 매개변수

def print_age(**persons):
  for s in persons.keys():
    print('{0} = {1}'.format(s, persons[s]))

print_age(kim=22, lee=23, choi=21)