from random import*

people = range(1,21) #1부터 20까지 숫자 생성
people = list(people)

shuffle(people)

gift = sample(people,4)

print("-- 당첨자 발표 --\n")
print("치킨 당첨자 : {0}".format(gift[0]))
print("커피 당첨자 : {0}".format(gift[1:]))
print("-- 축하합니다 --")

