# range : 0에서부터 5미만까지 , (1,6) ->시작, 끝직전

# for waiting_no in range(1,6):
#     print("대기번호 : {0}".format(waiting_no)) 

# starbucks = ["아이언맨","토르","아이엠 그루트"]

# for customer in starbucks:
#     print("{0}, 커피가 준비되었습니다.".format(customer))


#while
#무한루프에 빠졌을 경우에는 컨트롤 + c
# customer = "토리"
# index = 5
# while index >=  1:
#     print("{0}, 커피가 준비 되었습니다. {1}번 남았어요".format(customer,index))
#     index -= 1
#     if index == 0:
#         print("카피는 폐기 처분 되었습니다.")



# person = "unknown"

# while person != customer :
#     print("{},커피가 준비되었습니다".format(customer))
#     person = input("이름이 어떻게 되세요? ")


absent = [2,5]
no_book = [7]

for student in range(1,11):
    if student in absent :
        continue
    elif student in no_book :
        print("오늘 수업 여기까지. {}은 교수실로 따라와".format(student))
        break
    print("{}, 책을 읽어봐".format(student))


#한 줄 for문

student = ["iron man", "thor"]
student = [i.upper() for i in student]
print(student)