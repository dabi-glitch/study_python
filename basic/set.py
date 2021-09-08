# #집합
# #중복 값은 무시된다.
# my_set = {1,2,3,3,3}
# print(my_set)

# #집합을 만들 수 있는 두 가지 방법

# java = {"유재석","김태호","양세형"}
# python = set(["유재석","박명수"])

# #교집합 출력하기
# print(java & python)
# print(java.intersection(python))

# #합집합 출력하기
# print(java | python)
# print(java.union(python))

# #차집합 출력하기
# print(java - python)
# print(java.difference(python))

# #python을 할 줄 아는 사람이 늘어남
# python.add("김태호")
# print(python)

# #java를 까먹음
# java.remove("김태호")
# print(java)

#자료구조의 변경

menu = {"커피", "우유", "주스"}
print(menu, type(menu))

menu = list(menu)
print(menu, type(menu))

menu = tuple(menu)
print(menu, type(menu))

menu = set(menu)
print(menu, type(menu))