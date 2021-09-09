#지역 변수 : 함수 내에서만 사용 가능하다
#전역 변수 : 모든 공간에서 사용 가능하다

gun = 10

# 초기화가 안되었기 때문에 쓸 수가 없다. 
# 안에 있는 gun 변수의 값이 변한다.
# 전역변수를 사용하려면 gloabl gun 이라고 적으면 된다.
# 전역변수를 많이 쓰면 코드가 어려워져서 다른 방법을 사용한다.

def checkpoint(soliders):
    global gun #전역 공간에 있는 gun 사용하겠다.
    gun = gun - soliders
    print("[함수 내] 남은 총 : {0}".format(gun))

print("전체 총 : {0}".format(gun))
checkpoint(2)
print("남은 총 : {0}".format(gun))

def checkpoint_ret(gun, soliders):
    gun = gun - soliders
    return gun

#return을 통해 바뀌어진 gun을 밖으로 던진다.

gun = checkpoint_ret(gun,2)
print("남은 총 : {0}".format(gun))
