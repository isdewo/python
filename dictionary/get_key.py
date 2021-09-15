# Key에 대응되는 Value를 돌려줌
# 존재하지 않는 키(nokey)로 값을 가져오라고 할경우
# a['nokey']는 Key 오류를 발생시키고
# a.get('nokey')라는 None을 돌려줌
a =  {'name': 'Park ISeul', 'sex': 'female', 'position': 'student'}
print("a.get('name') = ", a.get('name'))