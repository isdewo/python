# 리스트의 마지막 요소를 뽑아내어 리스트에서 제거
a = [1, 2, 3, 4, 5]
print('a = ', a)

print('a.pop() = ', a.pop())
print('a = ', a)

print('a.pop() = ', a.pop())
print('a = ', a)

# 마지막이 아닌 특정 요소를 제거할 때는 제거하고자 하는 요소의 인덱스 입력
print("-------------\n특정 요소 제거")
print('a.pop(1) = ', a.pop(1))
print('a = ', a)