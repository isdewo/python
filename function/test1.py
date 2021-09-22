def spam(eggs):
  eggs = [2, 3] # 별도의 eggs 객체
  eggs.append(1) # 별도 객체에 1 삽입 -> eggs = [2, 3, 1]
  print(eggs) # 별도 객체 출력

ham = [0]
spam(ham)
print(ham) # ham 객체 출력 -> ham = [0]