#5-1 리스트 [] 

subway1 = 10
subway2 = 20
subway3 = 30

subway = [10,20,30]
print (subway)

subway = ["gom", "ru", "gem"]
print(subway)

#위치 print
print(subway.index("gom"))

#마지막에 추가
subway.append("hungry")
print(subway)

#사이에 추가
subway.insert(1, "U")
print(subway)

#뒤에서부터 제거
print(subway.pop())
print(subway)

print(subway.pop())
print(subway)

print(subway.pop())
print(subway)


#같은 것이 얼마나 있는지 확인
subway.append("gom")
print(subway)
print(subway.count("gom"))

#정렬
num_list = [5,4,3,2,1]
num_list.sort()
print(num_list)

#역정렬
num_list.reverse()
print(num_list)

#모두 지우기
num_list.clear()
print(num_list)

#다양한 자료형 함께 사용
mix_list = ["hungry", 24,True]
print(mix_list)

#하나의 list로 합치기
num_list2 = [5,4,3,2,1]
num_list2.extend(mix_list)
print(num_list2)

#5-2. 사전
