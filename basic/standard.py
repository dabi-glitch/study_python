
def set_weight(height, gender):
    if gender == "남자":
        return height * height * 22
    else :
        return height * height * 21

gender = input ("당신의 성별은 무엇입니까?")
height = int(input("당신의 키는 무엇입니까? "))
weight = round(set_weight(height / 100,gender),2)
print("케 {0}cm {1}의 표준 체중은 {2}kg입니다.".format(height, gender, weight))
