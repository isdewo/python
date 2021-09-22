# 매개변수 전달 방식
def spam(eggs): # call-by-reference
  eggs.append(1) # ham = [0, 1]
  eggs = [2, 3] # 형식 매개변수 eggs와 다른 객체 생성

ham = [0]
spam(ham)
print(ham)  # ham = [0, 1]