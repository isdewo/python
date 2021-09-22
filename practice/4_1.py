def var_pos_args(*args):
  print(type(args)) # 타입 출력
  print(locals()) # 지역변수 목록 출력

print(var_pos_args())
print(var_pos_args(1))
print(var_pos_args(1, 2))

