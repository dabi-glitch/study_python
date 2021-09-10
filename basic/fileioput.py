# 파일입출력

score_file = open("score.txt","w", encoding="utf8")
print("수학 : 0", file=score_file)
print("영어 : 50", file=score_file)
score_file.close()

# 이어서 쓰기
# print는 자동으로 줄바꿈이 되지만, 이거는 해줘야해
score_file = open("score.txt","a",encoding="utf8")
score_file.write("과학 : 80")
score_file.write("\n코딩 : 100")
score_file.close()

#읽어 오기(한 번에 다)
score_file = open("score.txt","r",encoding="utf8")
print(score_file.read())
score_file.close()

#한 줄 읽어오기, 한 줄 읽고 커서는 다음으로 이동
score_file = open("score.txt","r",encoding="utf8")
print(score_file.readline(),end="")
print(score_file.readline(),end="")
print(score_file.readline(),end="")
print(score_file.readline(),end="")
score_file.close()

#파일이 몇 줄인지 모를 때
score_file = open("score.txt","r",encoding="utf8")
while True :
    line = score_file.readline()
    if not line:
        break
    print(line, end="")
score_file.close()

#list에 값을 넣어 처리
score_file = open("score.txt","r",encoding="utf8")
lines = score_file.readlines()
for line in lines:
    print(line,end="")
score_file.close()