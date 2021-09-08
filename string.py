#1. 문자열 함수

python = "Python is Amazing"

print(python.lower())
print(python.upper())
print(python[0].isupper())
print(len(python))
print(python.replace("Python","Java")) #값 바꾸기

index = python.index("n")
print(index)

index = python.index("n", index + 1)
print(index)

print(python.find("n"))
print(python.find("JAVA")) #원하는 값이 없으면 -1, index에는 원하는 값이 없으면 오류를 낸다.

print(python.count("n"))

#2.문자열 포맷

#방법1

print("나는 %d살 입니다." %20) 
print("나는 %s를 좋아해요" %"python")
print("Apple 은 %c로 시작해요" %'A')

# %S를 이용하면 정수, 문자열, 문자 다 가능하다.

print("나는 %s색과 %s색을 좋아해요" %("빨간","파란"))

#방법2

print("나는 {}살 입니다.".format(20))
print("나는 {1}색과 {0}색을 좋아해요.".format("파란", "빨간"))
print("나는 {0}색과 {1}색을 좋아해요.".format("파란", "빨간"))

#방법3 변수처럼 가져다가 쓸 수 있다.
print("나는 {age}살이며, {color}색을 좋아해요".format(age = 20, color = "빨간"))

#방법4 실제 변수에서 사용된 값을 쓸 수 있다.
age = 20
color = "빨간"

print(f"나는 {age}살이며, {color}색을 좋아해요")


