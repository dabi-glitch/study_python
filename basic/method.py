#상속 : 물려받는 것
#부모클래스 -> 자식클래스 // 다중상속 : 부모가 둘 이상이다

class Unit:
    def __init__(self, name, hp, speed):
        self.name = name
        self.hp = hp
        self.speed = speed
    
    def move(self, location):
        print("[지상 유닛 이동")
        print("{0} : {1} 방향으로 이동합니다. [속도 : {2}]".format(self.name, location, self.speed))

class AttackUnit(Unit):
    def __init__(self, name, hp, speed, damage):
        Unit.__init__(self,name,hp, speed)
        self.damage = damage

# self : 자기 자신을 의마하며, class안의 메소드에는 항상 self를 적어줘야해
# self.xx를 이용해서 자기 자신의 변수에 접근하는 것이다.

    def attack(self, location):
        print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 {2}]".format(self.name, location, self.damage))

    def damaged(self, damage):
        print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0} : 파괴되었습니다".format(self.name))

class Flyable :
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed

    def fly(self, name, location) :
        print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]".format(name, location, self.flying_speed))

class FlyableAttackUnit(AttackUnit, Flyable):
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, 0, damage)
        Flyable.__init__(self, flying_speed)

vulture = AttackUnit("벌쳐", 80,10,20)

battlecruiser = FlyableAttackUnit("배틀크루저",500,25,3)

vulture.move("11시")
battlecruiser.fly(battlecruiser.name, "9시")
