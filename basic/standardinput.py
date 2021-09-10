# #sep를 통해서 값의 사이에 뭘 넣을 지 결정할 수 있다.
# #end를 통해서 문장의 끝에 뭘 넣을 지 결정할 수 있다.

# print("Python","java","javascript", sep = ",", end="?")
# print("무엇이 더 재밌을까요?")

# #stdout : 표준출력으로 문장이 나온다
# #stderr : 확인을 해서 프로그램 코드를 수정해야한다. 
# # import sys
# # print("Python", "Java", file=sys.stdout)
# # print("Python", "Java", file=sys.stderr)

# # 시험 성적
# # ljust(8) : 8개의 공간을 확보하고 왼쪽 정렬 해줘
# scores = {"수학":0, "영어":50, "코딩":100}

# for subject, score in scores.items():
#     print(subject.ljust(8), str(score).rjust(4), sep = ":")

# #은행의 대기 순번표
# #zfill 3크기 만큼의 공간을 확보하고 빈 공간을 0을 채운다.
# for num in range(1,21):
#     print("대기번호 : " + str(num).zfill(3))


# #표준 입력 - input을 했을 경우, 모든 글자가 str 처리가 된다. 

#다양한 출력 포맷

#1. 빈 자리는 빈 공간으로 두고, 오른쪽 정렬을 하되, 총 10자리 공간을 확보

print("{0: >10}".format(500))


#2. 양수일 땐 +로 표시, 음수일 땐 -로 표시 

print("{0: >+10}".format(500))
print("{0: >+10}".format(-500))

#왼쪽 정렬 하고, 빈칸을 _로 채움
print("{0:_<10}".format(500))

# 3자리 마다 콤마를 찍어주기
print("{0:,}".format(1000000000))


# 3자리 마다 콤마를 찍어주기, +-도 붙이기
print("{0:+,}".format(1000000000))
print("{0:+,}".format(-1000000000))

# 3자리 마다 콤마를 찍어주기, 부호도 붙이고, 자릿수 확보하기
# 돈이 많으면 빈자리는 ^

print("{0:^<+30,}".format(500000000000000))

# 소수점 출력
print("{0:f}".format(5/3))
print("{0:.2f}".format(5/3))