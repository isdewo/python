# 데이터를 {키:값}을 하나의 쌍으로 하여 딕셔너리 생성
dic = {'boy': '소년', 'school': '명지', 'lecture': 'python'}

print(dic) # 생성된 딕셔너리 출력

# dic[key] = value의 형식으로 입력하여 딕셔너리에 해당 키, 값 쌍을 추가한다
# 만약 동일한 key가 딕셔너리에 존재할 경우 해당 key의 value값이 갱신된다.
dic['boy'] = '남자아이'
dic['girl'] = '여자아이'
print(dic)
print(dic.keys()) # 딕셔너리의 키(key)들을 모아 dict_keys 객체를 돌려준다.
print(dic.values()) # 딕셔너리의 값(value)들을 모아 dict_values 객체를 돌려준다.
print(dic.items()) # 딕셔너리의 키(key), 값(value) 쌍을 모아 dict_items 객체를 돌려준다.
del dic['lecture'] # 딕셔너리에서 key가 'lecture'인 요소를 삭제한다.
print(dic) # 딕셔너리를 출력한다.
