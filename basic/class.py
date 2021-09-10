

#클래스 안에 정의된 변수 = 멤버변수

class Unit:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage
        print("{0} 유닛이 생성 되었습니다".format(self.name))
        print("체력 {0}, 공격력 {1}".format(self.hp, self.damage))

#마린, 탱크 = 자동으로 호출된다
# 클래스로 만들어짐 -> 객체, 마린과 탱크 -> 클래스의 인스턴스 
# init 함수에 정의된 것만큼 값을 던져줘야 해 

marine1 = Unit("마린", 40, 5)
marine2 = Unit("마린", 40, 5)
tank = Unit("탱크",150,35)

wraith1 = Unit("레이스",80,5)
print("유닛 이름 : {0}, 공격력 : {1}".format(wraith1.name, wraith1.damage))

# 변수를 추가로 할당 가능하다. 
# 확장된 변수는 확장을 한 객체에만 적용된다.

wraith2 = Unit("빼앗은 레이스",80,5)
wraith2.clocking = True
    
if wraith2.clocking == True :
    print("{0}는 현재 클로킹 상태입니다".format(wraith2.name))