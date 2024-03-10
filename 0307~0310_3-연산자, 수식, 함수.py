#3-1 연산자
print(1+1) #2
print(3-2) #1
print(5*2) #10
print(6/3) #2

print(2**3) #2^3 = 8
print(5 % 3) #5 / 3 나머지 = 2
print(10 % 3) # 1
print(5 // 3) #5를 3으로 나눌 때 몫 = 1
print(10 // 3) # 3

print(10 > 3) # True
print(4 >= 7) # False
print(10 < 3) # False
print(5 <= 5) # True

print(3 == 3) # True
print(4 == 2) # False
print(3 + 4 == 7) # True
print( 1 != 3 ) #True
print( not (1 != 3) ) #False -> not : 결과의 반대 

print((3>0) and (3<5)) # 모두 만족할 때 True
print((3>0) & (3<5)) # 위와 동일

print((3>0) or (3>5)) # 둘 중 하나만 만족해도 True
print((3>0) | (3>5)) # 위와 동일

print( 5 > 4 > 3) # True
print( 5 > 4 > 7) # False

#3-2 간단한 수식
print(2 + 3 * 4) # 14
print((2 + 3) * 4) # 20
number = 2 + 3 * 4
print(number) # 14
number = number + 2
print(number) # 16
number += 2
print(number) # 18
number *= 2
print(number) # 36
number /= 2 
print(number) # 18
number -= 2
print(number) # 16
number %= 5
print(number) #1

#3-3 숫자처리함수
print(abs(-5)) #절대값 - 5
print(pow(4,2)) #4^2 = 16
print(max(5,12)) #큰값 return 12
print(min(5,12)) #작은값 return 5
print(round(3.14)) #반올림 3
print(round(4.99)) #5

#math library 사용
from math import *
print(floor(4.99)) #내림 4
print(ceil(3.14)) #올림 4
print(sqrt(16)) #제곱근 4


#3-4 랜덤함수 (난수)
from random import *
print(random()) # 0.0~1.0 미만의 임의의 값 생성
print(random()*10) #0.0~10.0 미만의 임의의 값 생성
print(int(random()*10)) #0~10 미만의 임의의 값 생성
print(int(random()*10)+1) #1~10 이하의 임의의 값 생성
print(int(random()*45)+1) #1~45 이하의 임의의 값 생성
print(randrange(1, 46)) #1~45 이하의 임의의 값 생성
print(randint(1,45)) #1~45 이하의 임의의 값 생성

#3-5 Quiz #2
'''
1: 랜덤으로 날짜
2: 최수일수 28일 이내로
3: 1~3은 제외
'''
date1 = int(random()*24)+4
date2 = randint(4,28)
date3 = randrange(4, 29)

print(str(date1))
print(date2)
print(date3)