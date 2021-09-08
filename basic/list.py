# subway = ["유재석", "조세호", "박명수"]

# print(subway.index("조세호"))

# subway.append("하하")
# print(subway)

# subway.insert(1,"정형돈")
# print(subway)

# print(subway.pop())
# print(subway)

# #같은 이름의 사람이 몇 명 있는지 확인
# subway.append("유재석")
# print(subway)
# print(subway.count("유재석"))


# #정렬도 가능

# num_list = [5,2,4,1,3]
# num_list.sort()
# print(num_list)

# num_list.reverse()
# print(num_list)

# #모두 지우기
# num_list.clear()
# print(num_list)

# #리스트 확장도 가능
# # num_list.extend(mix_list)



#사전 
#key에는 숫자 뿐만 아니라 문자열, 문자 모두 가능하다

cabinet = { 3: "유재석", 100:"김태호"}
print(cabinet[3])
print(cabinet.get(5, "사용 가능"))


# dictionary에 있는 key의 존재 확인하기

print(3 in cabinet) 

#새로운 key와 value 추가하기

cabinet[200] = "조세호"
print(cabinet) 

# key 삭제학
del cabinet[200]
print(cabinet)

#원하는 것만 출력
print(cabinet.keys())
print(cabinet.values())
print(cabinet.items())

#모두 지우기
print(cabinet.clear())


#튜플 : 이렇게 나열해서 넣을 수 있다. 
(name,age,hobby) = ("김종국", 20, "코딩")
print(name,age,hobby)