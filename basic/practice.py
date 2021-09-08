from math import *

print(floor(4.99)) #내림
print(ceil(3.14)) #올림
print(sqrt(16)) #제곱근


#랜덤함수 

from random import *
print(random()) #0.0 이상 1.0 미만의 임의의 값 생성
print(random()*10) #: 0.0 이상 10.0 미만의 임의의 값 생성
print(int(random())) # 0~10 미만의 임의의 값 생성
print(int(random()*10)+1) # 1부터 10이하의 임의의 값 생성


#로또 출력
print(int(random()*45)+1) #1부터 45이하의 임의의 값 생성

#예제
print(int(random()*50)+3) #3부터 50이하의 임의의 값 생성

print(randrange(1,45)) #1부터 45미만의 임의의 값 생성

print(randint(1,45)) #1부터 45이하의 임의의 값 생성


# quiz 2

# 숫자를 print문에서 쓰려면 str 써야 하는 것 잊지 말자!

from random import *

offline = randint(4,28)

print("오프라인 스터디 모임 날짜는 매월" + str(offline) + "일로 선정되었습니다.")