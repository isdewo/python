# 입력한 데이터와 일치하는 첫 번째 요소의 첨자 구하기.
a = ['abc', 'def', 'ghi']
print('a = ', a)

print("a.index('def') = ", a.index('def'))

# 찾고자 하는 데이터가 없으면 오류 발생
print('\n오류 발생')
print("a.index('jkl') = ", a.index('jkl'))