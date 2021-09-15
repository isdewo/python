# 딕셔너리 요소 삭제
a =  {'name': 'Park ISeul', 'sex': 'female', 'position': 'student'}
print('a = ', a)
print("a.pop('position') = ", a.pop('position'))
print('a = ', a)

del a['name']
print("del a['name'] = ", a)