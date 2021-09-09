from typing import Coroutine


def open_aacount ():
    print("새로운 계좌가 생성되었습니다.") #함수는 정의만 해놓은 것이지 호출 안 하면 출력x

def deposit(balance, money):
    print("입금이 완료되었습니다. 잔액은 : {0} 원 입니다.".format(balance + money))
    return balance + money

def withdraw(balance, money):
    if balance > money :
        print("출금이 완료되었습니다. 잔액은 {0}원입니다.".format(balance-money))
        return(balance-money)
    else :
        print("출금이 완료되지 않았습니다. 잔액은 {}원 입니다.".format(balance))
        return(balance)
# return으로 총 금액을 반환해준다. -> balance에 저장

def withdraw_night(balance, money):
    commission = 100 #수수료
    return commission, balance - money - commission

# 두 개 이상의 값을 ,로 구분해서 튜플로 반환한다. 

balance = 0
balance = deposit(balance,8000)
balance = withdraw(balance,5000)
commission, balance = withdraw_night(balance,500)
print("수수료는 {}원 이며, 잔액은 {}원입니다.".format(commission,balance))

def profile(name, age, main_lang):
    print("이름 : {0}\t나이:{1}살\t 주 사용 언어 : {2}".format(name,age,main_lang))

profile("윤다빈", 23, "python")

#같은 학교 같은 학년 같은 반 같은 수업을 듣는다.
#기본 값을 만들어놓았을 경우에는 값을 적으면 들어가지만 적지 않으면 저게 들어간다.
def profile_2(name, age=17, main_lang= "파이썬"):
    print("이름 : {0}\t나이:{1}살\t 주 사용 언어 : {2}".format(name,age,main_lang))

profile_2("윤다빈")

#매개변수의 keyword을 이용해서 출력을 하면 순서가 섞여도 잘 출력된다.
def profile(name, age, main_lang):
    print(name, age, main_lang)

profile(name = "윤다빈", main_lang="python",age=23)


#가변인자 서로 다른 갯수의 변수를 넣고자 할 때! 

def profile(name, age, lang1, lang2, lang3, lang4, lang5):
    print("이름 : {0}\t 나이:{1}\t".format(name,age), end=" ")
    print(lang1, lang2, lang3, lang4, lang5)

profile("유재석",20,"python","java","c++","c","c#")
profile("김태호",25,"Kotlin","Swift","","","")


def profile(name, age, *language):
    print("이름 : {0}\t 나이:{1}\t".format(name,age), end=" ")
    for lang in language:
        print(lang, end=" ")
    print()

profile("유재석",20,"python","java","c++","c","c#","javascript")
profile("김태호",25,"Kotlin","Swift","","","")
