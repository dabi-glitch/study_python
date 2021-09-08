from random import*

index = 0 #총 탑승 승객

for people in range(1,51):
    taxi = randint(5,50)
    if 5<= taxi <= 15:
        print("{0}번째 손님 : [o] 소요시간 {1}분".format(people,taxi))
        index += 1
    else :
        print("{0}번째 손님 : [ ] 소요시간 {1}분".format(people,taxi))

print("총 탑승 승객 : {0}분".format(index))