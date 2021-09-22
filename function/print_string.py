# 가변 매개변수(arbitary argument)
def print_string(*mytext):
  result = ''
  for s in mytext:
    result = result + s
  return result

print(print_string('파이썬은', '정말', '재미있다'))