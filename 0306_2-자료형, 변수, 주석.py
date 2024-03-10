#자료형

#2-1 숫자형 자료형
print(5) #정수
print(-10) #음수
print(3.14) #실수
print(10000) #큰 수
#연산
print(5+3) # 8 print
print(5*3) # 15 print
print(3*(3+1)) # 12 print

#2-2 문자열 자료형
print('풍선') #작은 따옴표
print("나비") #큰 따옴표
print("ㅋㅋㅋㅋㅋㅋㅋ")
print("ㅋ"*7) #위와 같은 결과

#2-3 boolean 자료형
print(5>10) #False
print(5<10) #True
print(False) #False
print(True) #True
print(not True) #False
print(not False) #True
print(not(5<10)) #False
print(not(5>10)) #True

#2-4 변수
#애완동물을 소개해 주세요
#변수 : 값을 저장하는 공간

print("우리집 강아지의 이름은 연탄")
print("연탄쓰 나이 4살, 산책 좋아함")
print("연탄쓰 어른? True")

animal = "강아지"
name = "연탄"
age = 4 #int
hobby = "산책"
is_adult = age>=3

print("우리집 "+ animal +"의 이름은 연탄")
#int형과 boolean형을 str형으로 바꿔주기!
hobby = "공놀이" #다시 선언 가능
print(name + "쓰 나이 " + str(age) + "살, "+ hobby +" 좋아함")
#만약에 +가 아닌 ,를 쓴다면 str을 사용하지 않을 수 있다. 
#,를 쓴다면 무조건 띄어쓰기가 된다.
print(name , "쓰 나이 " , age , "살, ", hobby," 좋아함")
print(name + "쓰 어른? " + str(is_adult))

#2-5 주석

'''여러 
문장을 
주석 처리하고
싶을 때'''

# c랑 비슷하게 ctrl+/ 사용 가능
# shift는 안눌러도 됨

#2-6 Quiz #1 -> 변수를 이용해서 다음 문장 출력
station = "사당"
print(station + "행 열차가 들어오고 있습니다.")
station = "신도림"
print(station + "행 열차가 들어오고 있습니다.")
station = "인천공항"
print(station + "행 열차가 들어오고 있습니다.")