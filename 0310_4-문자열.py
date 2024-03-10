#4-1 문자열
sentence = '우우 붐따'
print(sentence)
sentence2 = "우우 붐따~"
print(sentence2)
sentence3 = """
오우예~
씨몬
""" # 맨 앞과 뒤의 줄바꿈까지 포함된 결과 출력 
print(sentence3)

#4-2 슬라이싱
jumin = "980614-1234567"
print("성별 : " + jumin[7])
print("연 " + jumin[0:2]) #0부터 2자리 전까지.. 즉 0과 1번째 출력 
print("월 " + jumin[2:4]) #2 & 3 출력 
print("일 " + jumin[4:6]) #4 & 5 출력

print("생년월일 : " + jumin[0:6])
print("생년월일 : " + jumin[:6]) # 아무것도 안쓸시에 처음부터 6직전까지 

print("뒤 7자리 : " + jumin[7:14]) 
print("뒤 7자리 : " + jumin[7:]) # 아무것도 X -> 마지막까지  
print("뒤 7자리 (뒤에서부터): " + jumin[-7:])  #맨 뒤 7번째부터 끝까지

#4-3 문자열처리함수
python = "Python is Amazing"
print(python.lower()) #소문자로 출력
print(python.upper()) #대문자로 출력
print(python[0].isupper()) #대문자 여부 확인
print(len(python)) #문자열 길이
print(python.replace("Python", "Java")) #문자열 대체

index = python.index("n") #n의 위치
print(index)
index = python.index("n", index+1) #위에서 찾은 index 이후에서 n을 찾기
print(index)

print(python.find("n")) #n의 위치 
print(python.find("Java")) #원하는 것이 없으면 -1 출력
#print(python.index("Java")) #error 발생
#print("hi") #error 발생 시 뒤에 있는 내용 출력 X

print(python.count("n")) #n이 나온 횟수 

#4-4 문자열포맷
print("a" + "b") #ab
print("a" , "b") #a b

#방법1
print("나는 %d살입니다." % 20) #%d 값을 맨 뒤에서 적어준다. d는 int형
print("나는 %s를 좋아함" % "자기") # %s -> str
print("Apple is start with %c" % "A") # %c -> char
print("나는 %s살입니다." % 20) #%d 대신 %s로 적어도 문제 X
print("I like %s and %s" %("red", "blue")) #2개 이상의 값 

#방법2
print("나는 {}살입니다".format(20))
print("I like {} and {}".format("blue", "red"))
print("I like {0} and {1}".format("blue", "red"))
print("I like {1} and {0}".format("blue", "red")) #순서

#방법3
print("나는 {age}살이며, {color}색을 좋아함".format(age=20, color = "빨간"))
print("나는 {age}살이며, {color}색을 좋아함".format(color = "빨간", age=20))

#방법4
age = 20
color = "빨간"
print(f"나는 {age}살이며, {color}색을 좋아함") #f로 시작한다면 변수로 저장된 값을 불러온다.

#4-5 탈출문자
print("우루는 천재일까요 \n 바보일까요")
print('우루는 "천재"입니다') 
print("우루는 \"천재\"입니다") 
print("우루는 \'천재\'입니다") 

# \\ : \로 출력
print("C:\\Python312\\python.exe")

#\r: 커서를 맨앞으로 이동
print("Red Apple \rPine") #PineApple
#Red 를 Pine으로 바꿨음...

#\b: backspace (한글자 삭제)
print("Redd\bApple") #RedApple

#\t : 탭
print("Apple\tRed") #Apple    Red

#4-6 퀴즈 #3

web = "https://naver.com"

#내 풀이
name = web[8:-4]
len_num = len(name)
e_num = name.count('e')
name = name[0:3]

print(f"{name}{len_num}{e_num}!")

#정답
my_str = web.replace("https://","")
my_str = my_str[:my_str.index(".")] #처음부터 처음 나오는 .이 나오기 전까지
password = my_str[:3] + str(len(my_str)) + str(my_str.count("e")) + "!"
print("{0}의 비밀번호는 {1}입니다".format(web, password))
